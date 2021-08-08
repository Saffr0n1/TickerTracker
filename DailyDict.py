import datetime
import sqlite3 as sl
import reticker
import pandas as pd

today = datetime.date.today()
a = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=6)
b = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=9, minute=30)

lb = int(datetime.datetime.timestamp(a))
ub = int(datetime.datetime.timestamp(b))

con = sl.connect("TickerTracker.db")
cur = con.cursor()

dbReadPosts = """SELECT * FROM sub_data WHERE date >= %d AND date <= %d""" % (lb, ub)
dfPosts = pd.read_sql(dbReadPosts, con)

ticker_match_config = reticker.TickerMatchConfig(prefixed_uppercase=True, unprefixed_uppercase=True,
                                                 prefixed_lowercase=True, prefixed_titlecase=True)
extractor = reticker.TickerExtractor(deduplicate=False, match_config=ticker_match_config)

blacklist = ["SUS", "AF", "DD", "FTC", "USA", "IPO", "EBITDA", "WSJ", "HUGE", "NEWS", "FROM", "STOCKS", "GOOD", "YOLO",
             "FOR", "WHY", "IM", "ON", "SOFLY", "IRA", "US", "BOUGHT", "DIP", "RT", "IDR", "FREE", "PM", "CST", "MLB",
             "EST", "AND", "TO", "NBA", "BTC", "ETH", "MY", "YOU", "IT", "ATENCI", "WHALE", "WITH", "USD", "AM", "GIVE",
             "ME", "GMT", "TG", "BEAST", "OLYMPE", "NMR", "EDIT", "RECAF", "ARN", "BSC", "HD", "ASK", "WANT", "FULL"]

tickers = set()
dfT = pd.read_csv("Tickers.csv")
for i in range(len(dfPosts)):
    for item in extractor.extract(dfPosts['title'][i]):
        tickers.add("$"+item)

for j in range(len(dfT)):
    tickers.add(dfT['0'][j])

finalDF = pd.DataFrame(tickers)
finalDF.to_csv("Tickers.csv")
