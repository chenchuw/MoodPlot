# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# For the use of BU EC601 Project 2, with prof. Osama

import os
from matplotlib import pyplot as plt
from google.cloud import language_v1
import tweepy

# Setting the path for the Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/francischen/Desktop/EC601/google_credential.json"

#Twitter API credentials
consumer_key = "8KMps10UjAdfCZoLzUMOjJtaX"
consumer_secret = "wstgm1dNVCgnPWKiBJ1Z7EPnIjQGzrYgLwvUwvC6N2tQ7z1zFv"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL5iUAEAAAAAmo6FYRjqdKlI3cNziIm%2BHUQB9Xs%3DS31pj0mxARMTOk2g9dvQ1yP9wknvY4FPBPUlE00smJcncw4dPR"

# Instantiate the client
client = language_v1.LanguageServiceClient()

class Twitter_feed:

    def __init__(self,comsumer_Key, consumer_Secret):
        self.consumer_key = comsumer_Key
        self.consumer_secret = consumer_Secret
        self.bearer_token = bearer_token
        self.sentiments = []
        self.invalid = 0

    def sentiment_analysis(self, keyword, count):
        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        try:
            api = tweepy.API(auth)               
            for tweet in api.search_tweets(q = keyword, count = count):
                text = tweet.text
                document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
                # Error handling: invalid tweet text for Google NLP
                try:
                    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
                except:
                    self.invalid += 1
                    print("ERROR: Current tweet's text is invalid for Google NLP analysis...\n-------------------------")
                print("Text: {}".format(text))
                print("Sentiment: {:.1f}, {:.1f}\n-------------------------".format(sentiment.score, sentiment.magnitude))
                self.sentiments.append(round(sentiment.score,3))
        except:
            print("ERROR! Current analysis failed due to some reasons...")

def analysis(keyword, count):
    # Type error check
    if (not count.isdigit()):
        print("Sorry, please give a positive number for number of tweets...")
        return ("Sorry, please give a positive number for number of tweets...")

    # Empty input error handling
    if (not keyword) or (int(count) <= 0):
        print ('Sorry, please try again and enter a valid topic and number of tweets...')
        return ('Sorry, please try again and enter a valid topic and number of tweets...')

    # Conduct the analysis
    twitter_acount = Twitter_feed(consumer_key, consumer_secret)
    twitter_acount.sentiment_analysis(keyword,count)

    # Calculate the average sentiment score and Check empty searched tweets
    if len(twitter_acount.sentiments) != 0:
        avg_sentiment = round(sum(twitter_acount.sentiments)/len(twitter_acount.sentiments),3)
    else:
        print ("No results found with the given topic... Please try again with another topic :)")
        return ("No results found with the given topic... Please try again with another topic :)")

    # Print out the results
    print(f"{len(twitter_acount.sentiments)} tweets are analyzed.")
    print(f"{twitter_acount.invalid} tweets are invalid.")
    print("The user's sentiment score trend is: ",*twitter_acount.sentiments)
    print("The user's average sentiment score is: ", avg_sentiment)

    # Plot the trend
    plt.plot(twitter_acount.sentiments, label = "sentiments trend")
    plt.axhline(y=avg_sentiment, color = 'r', linestyle = '-', label = "average sentiment")
    plt.legend(loc = "upper left")
    plt.xlabel("Number of the Tweet")
    plt.ylabel("Sentiment score")
    plt.ylim(-1,1)
    plt.title(f"Sentiment trend of the topic '{keyword}' over {count} most-recent tweets")
    plt.grid(True)
    plt.show()

def main():
    # Ask user for inputs
    keyword = input("Happy to see you here!\nPlease enter a topic that you are interested in: ")
    count = input("Number of tweets you want to analyze for: ")

    # Call the analysis func!
    analysis(keyword, count)

if __name__ == '__main__':
    main()
