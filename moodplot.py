# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# For the use of BU EC601 Project 2, with prof. Osama

import os
from matplotlib import pyplot as plt
from google.cloud import language_v1
import requests
from requests import session
import tweepy # https://github.com/tweepy/tweepy

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
bearer_token = ""

# Setting the path for the Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/francischen/Desktop/EC601/ec601.json"

class Twitter_feed:

    def __init__(self,comsumer_Key, consumer_Secret, keyword, count):
        self.consumer_key = comsumer_Key
        self.consumer_secret = consumer_Secret
        self.bearer_token = bearer_token
        self.sentiments = []
        self.keyword = keyword
        self.count = count

    def sentiment_analysis(self):
        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        try:
            api = tweepy.API(auth)               
            #for tweet in tweepy.Cursor(api.search_tweets, q='tweepy').items(10):
            for tweet in api.search_tweets(q = self.keyword, count = self.count):
                text = tweet.text
                document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
                sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
                print("Text: {}".format(text))
                print("Sentiment: {:.1f}, {:.1f}\n-------------------------".format(sentiment.score, sentiment.magnitude))
                self.sentiments.append(round(sentiment.score,3))

        except tweepy.TweepError:
            print('Error! Failed to get request token.')

if __name__ == '__main__':
    # Instantiate the client and conduct the analysis
    client = language_v1.LanguageServiceClient()
    keyword = input("Happy to see you here!\nPlease enter a keyword that you are interested in: ")
    count = input("Number of tweets you want to analyze for: ")
    twitter_acount = Twitter_feed(consumer_key, consumer_secret, keyword, count)
    twitter_acount.sentiment_analysis()

    # Calculate the average sentiment score
    avg_sentiment = sum(twitter_acount.sentiments)/len(twitter_acount.sentiments)

    # Print out the results
    print(f"{len(twitter_acount.sentiments)} tweets are analyzed.")
    print("The user's sentiment score trend is: ",*twitter_acount.sentiments)
    print("The user's average sentiment score is: ", avg_sentiment)

    # Plot the trend
    plt.plot(twitter_acount.sentiments, label = "sentiments trend")
    plt.axhline(y=avg_sentiment, color = 'r', linestyle = '-', label = "average sentiment")
    plt.legend(loc = "upper left")
    plt.xlabel("Number of the Tweet")
    plt.ylabel("Sentiment score")
    plt.ylim(-1,1)
    plt.title(f"Sentiment trend of the topic '{keyword}' over {count} tweets")
    plt.grid(True)
    plt.show()
