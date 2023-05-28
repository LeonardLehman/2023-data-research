import snscrape.modules.twitter as  sntwitter
import pandas as pd

query = "protest"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))
    if len(tweet) == limit:
        break
    else:
        tweets.append(tweet.date, tweet.user.username, tweet.content)

df = pd.DataFrame(tweets, columns=["Date", 'User', "Content"])
