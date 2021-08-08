import datetime
import time
import praw
import sqlite3 as sl

con = sl.connect("TickerTracker.db")
cur = con.cursor()

dbInsert = """INSERT INTO comment_data (date, postID, body, num_upvotes) VALUES (?,?,?,?)"""

reddit = praw.Reddit(client_id = "client_id",
                     client_secret="client_secret",
                     user_agent="user_agent")

subList = "wallstreetbets+stocks+stockmarket"

sub = reddit.subreddit(subList)

endTime = time.time() + 7.5*3600
counter = 0
while time.time() < endTime:
    try:
        for submission in sub.stream.comments(skip_existing=True):
            t = int(datetime.datetime.now().timestamp())
            postID = str(submission.id)
            body = str(submission.body)
            num_upvotes = int(submission.score)
            data = (t, postID, body, num_upvotes)
            cur.execute(dbInsert, data)
            con.commit()
            counter+=1
            print(counter)
    except Exception as e:
        print(str(e))
        time.sleep(20)
