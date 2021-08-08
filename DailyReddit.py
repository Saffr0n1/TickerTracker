import datetime
import praw
import sqlite3 as sl

con = sl.connect("TickerTracker.db")
cur = con.cursor()

dbInsert = """INSERT INTO sub_data (date, postID, title, num_comments, num_upvotes, upvote_percent) 
    VALUES (?,?,?,?,?,?)"""

reddit = praw.Reddit(client_id = "client_id",
                     client_secret="client_secret",
                     user_agent="user_agent")

subList = "wallstreetbets+stocks+stockmarket"

sub = reddit.subreddit(subList)

for submission in sub.top("day", limit=650):
    t = int(datetime.datetime.now().timestamp())
    postID = str(submission.id)
    title = str(submission.title)
    num_comments = int(submission.num_comments)
    num_upvotes = int(submission.score)
    upvote_percent = float(submission.upvote_ratio)
    data = (t, postID, title, num_comments, num_upvotes, upvote_percent)
    cur.execute(dbInsert, data)
    con.commit()
