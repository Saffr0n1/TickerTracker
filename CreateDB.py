import sqlite3 as sl

conn = sl.connect("TickerTracker.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE sub_data (
    date INTEGER, 
    postID TEXT, 
    title TEXT, 
    num_comments INTEGER, 
    num_upvotes INTEGER, 
    upvote_percent REAL)''')

cursor.execute('''CREATE TABLE comment_data (
    date INTEGER, 
    postID TEXT, 
    body TEXT, 
    num_upvotes INT)''')

cursor.execute('''CREATE TABLE twitter_data (
    date INTEGER, 
    body TEXT, 
    author TEXT)''')
