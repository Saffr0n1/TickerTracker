# TickerTracker

Collection of scripts to determine trending tickers on Reddit and Twitter on a daily and real-time basis. Can be used to get an idea of market sentiment towards retail-traded names. MySQL and SQLite3 are used for the database and [Dash](https://dash.plotly.com/) is used for data visualization. Trending stocks are determined both by generic symbol matching and by searching through a dictionary of related names (i.e. "GameStop", "Game Stop", etc. for "$GME"). Currently supported features include determining stock popularity in Reddit posts (across any number of subreddits), real-time Reddit comment volume related to individual stocks, and real-time Tweets related to stocks.



The following APIs are used:
- [PRAW](https://praw.readthedocs.io/en/stable/) for pulling Reddit post history and real-time comments.
- [Tweepy](https://docs.tweepy.org/en/stable/) as the Python wrapper for the [Twitter API](https://developer.twitter.com/en/docs)
