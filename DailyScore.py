import datetime
import sqlite3 as sl
import pandas as pd
import reticker
import collections

# 750: DailyReddit
# 755: DailyScore
# 800: Live start
# Hourly: Live output
# 3:00 Live stop

today = datetime.date.today()
a = datetime.datetime(year=today.year, month=today.month, day=today.day-1, hour=9)
b = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=8, minute=30)

lb = int(datetime.datetime.timestamp(a))
ub = int(datetime.datetime.timestamp(b))

con = sl.connect("TickerTracker.db")
cur = con.cursor()

dbReadPosts = """SELECT * FROM sub_data WHERE date >= %d AND date <= %d""" % (lb, ub)
dbReadComments = """SELECT * FROM comment_data WHERE date >= %d AND date <= %d""" % (lb, ub)
dbReadTweets = """SELECT * FROM twitter_data WHERE date >= %d AND date <= %d""" % (lb, ub)

dfPosts = pd.read_sql(dbReadPosts, con)
dfComments = pd.read_sql(dbReadComments, con)
dfTweets = pd.read_sql(dbReadTweets, con)

ticker_match_config = reticker.TickerMatchConfig(prefixed_uppercase=True, unprefixed_uppercase=True,
                                                 prefixed_lowercase=True, prefixed_titlecase=True)
extractor = reticker.TickerExtractor(deduplicate=False, match_config=ticker_match_config)

blacklist = ["SUS", "AF", "DD", "FTC", "USA", "IPO", "EBITDA", "WSJ", "HUGE", "NEWS", "FROM", "STOCKS", "GOOD", "YOLO",
             "FOR", "WHY", "IM", "ON", "SOFLY", "IRA", "US", "BOUGHT", "DIP", "RT", "IDR", "FREE", "PM", "CST", "MLB",
             "EST", "AND", "TO", "NBA", "BTC", "ETH", "MY", "YOU", "IT", "ATENCI", "WHALE", "WITH", "USD", "AM", "GIVE",
             "ME", "GMT", "TG", "BEAST", "OLYMPE", "NMR", "EDIT", "RECAF", "ARN", "BSC", "HD", "ASK", "WANT", "FULL",
             "FINRA", "MODE", "EMA", "OF", "LEAP"]

output = []
flatCounts = []

for i in range(len(dfPosts)):
    for item in extractor.extract(dfPosts['title'][i]):
        output.append(item)
        score = int(dfPosts['num_comments'][i]*dfPosts['upvote_percent'][i])
        for j in range(score):
            flatCounts.append(item)

postScores = collections.Counter(flatCounts)

for i in range(len(dfComments)):
    for item in extractor.extract(dfComments['body'][i]):
        output.append(item)

for i in range(len(dfTweets)):
    for item in extractor.extract(dfTweets['body'][i]):
        output.append(item)

mentions = collections.Counter(output)

combined = mentions + postScores

print(mentions.most_common(20))
print(combined.most_common(20))




