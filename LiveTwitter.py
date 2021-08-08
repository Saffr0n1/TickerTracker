import datetime
import time
import tweepy as tp
import sqlite3 as sl
import json

con = sl.connect("TickerTracker.db")
cur = con.cursor()

dbInsert = """INSERT INTO twitter_data (date, body, author) VALUES (?,?,?)"""

apiKeys = {'key_cons': 'xxxxx', 'sec_cons': 'xxxxx',
           'token_acc': 'xxxxx',
           'sec_acc': 'xxxxx'}


class myStreamListener(tp.StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        t = int(datetime.datetime.now().timestamp())
        author = str(all_data['user']['screen_name'])
        body = str(all_data["text"])
        data = (t, body, author)
        cur.execute(dbInsert, data)
        con.commit()

    def on_error(self, status):
        print(status)


endTime = time.time() + 7.5*3600
while time.time() < endTime:
    try:
        auth = tp.OAuthHandler(apiKeys['key_cons'], apiKeys['sec_cons'])
        auth.set_access_token(apiKeys['token_acc'], apiKeys['sec_acc'])
        myStream = tp.Stream(auth, myStreamListener())
        myStream.filter(track=["$"])
    except Exception as e:
        print(str(e))
        time.sleep(20)
