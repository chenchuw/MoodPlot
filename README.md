### EC601_Project2

# Mood Plot

By using Google NLP and Twitter API, I made an naive product called "Mood Plot" that could summarize people's sentiment on a topic over a certain amount of tweets related to the topic. It could also plot the sentiment trend and the average sentiment score on a graph for visualization. The source code is in the file analyzer.py, also displayed below:

``` python
# Copyright 2021 Chuwei Chen chenchuw@bu.edu
# For the use of BU EC601 Project 2, with prof. Osama

import os
from matplotlib import pyplot as plt
from google.cloud import language_v1
import requests
from requests import session
import tweepy # https://github.com/tweepy/tweepy

#Twitter API credentials, which are hidden here for security
consumer_key = "XXXXXXXX"
consumer_secret = "XXXXXXXX"
bearer_token = "XXXXXXXX"

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
```
Sample I/O:

Happy to see you here!\
Please enter a keyword that you are interested in: tesla\
Number of tweets you want to analyze for: 20

20 tweets are analyzed.\
The user's sentiment score trend is:  -0.2 0.2 0.2 0.0 -0.4 -0.1 -0.4 -0.1 0.2 0.0 0.2 0.4 0.2 0.2 0.2 0.1 0.2 0.2 0.2 0.2\
The user's average sentiment score is:  0.07499999999999998

![output](https://github.com/chenchuw/EC601_Project2/blob/main/output_1.png?raw=true)

** In order to properly execute the moodplot.py, please prepare your Google NLP credential file first and replace my credential path with your credential file path in the 'Setting the path for the Google credentials' part in moodplot.py **
 
# User Story

Story #1

- I just heard the new that iPhone 13 was released and I am hesitating of whether I should update my old iPhone, and I'm too lazy to read the reviews about the product, so I use Moodplot to see people's feelings about iPhone 13 to help me decide buy it or not.

# MVP

- A module that can take inputs from user for topic and number of tweets for analysis

- A module that can analysis a given context and return a sentiment score
 
- A module that can retrieve text from social media posts

- A module that can plot the sentiment score over the number of tweets

# Modular Design

![modular_design](https://github.com/chenchuw/EC601_Project2/blob/main/module%20design.png?raw=true)

# Unit Testing

Since my python script involves user inputs and the outputs are uncertain (the outputs are obtained from the most recent tweets which are constantly changing), it is hard to, i.e. I have not yet found a way to implement a unit test for my script.

** The following sections explain the details of how my app works. **

# Cloud Natural Language API
First I used Google's Cloud Natural Language API. It is Google's proven pre-trained model for general content classification; sentiment analysis; entity recognition, etc. After getting access to the client library, I connected to the Cloud and tested sentiments for several sentences using my python script. The script is called language.py in this repository. 

*Code example*
```python

# Imports the Google Cloud client library
from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = input("Give me a sentence:\n")
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {:.1f}, {:.1f}".format(sentiment.score, sentiment.magnitude))
```

A snippet of the output is attached below:

(base) francischen@Ccws-Macbook-Pro EC601 % python language.py\
Give me a sentence:\
Professor Osama is the best!\
Text: Professor Osama is the best!\
Sentiment: 0.9, 0.9\
(base) francischen@Ccws-Macbook-Pro EC601 % python language.py\
Give me a sentence:\
Today's weather sucks\
Text: Today's weather sucks\
Sentiment: -0.7, 0.7\
(base) francischen@Ccws-Macbook-Pro EC601 % python language.py\
Give me a sentence:\
I hate this world.\
Text: I hate this world.\
Sentiment: -0.9, 0.9\
(base) francischen@Ccws-Macbook-Pro EC601 % python language.py\
Give me a sentence:\
Could you pass me the pen?\
Text: Could you pass me the pen?\
Sentiment: -0.3, 0.3

As we observed here, from a scale of -0.9 to 0.9, the NLP returns the sentiment score of the input sentences, following that more positive sentence get a higher score.

# Twitter API (Retrieving Tweets)

A program to retrive tweets. Python script is called Tweeter_Retrive.py in this repository. 

*Code example*
```python
#!/usr/bin/env python
# encoding: utf-8

import requests
from requests import session
import tweepy # https://github.com/tweepy/tweepy
import json
#Twitter API credentials
consumer_key = "XXXXXXXX"
consumer_secret = "XXXXXXX"
bearer_token = "XXXXXXX"

class twitter_access:

    def __init__(self,comsumer_Key, consumer_Secret):
        self.consumer_key = comsumer_Key
        self.consumer_secret = consumer_Secret
        self.bearer_token = bearer_token


    def build_connections(self):
        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        try:
            api = tweepy.API(auth)
            for tweet in tweepy.Cursor(api.search_tweets, q='tweepy').items(10):
                print(tweet.text)

        except tweepy.TweepError:
            print('Error! Failed to get request token.')

if __name__ == '__main__':

    web_app = twitter_access(consumer_key, consumer_secret)
    web_app.build_connections()
 ```
The output is below:

(base) francischen@Ccws-Macbook-Pro EC601 % python Twitter_Retreive.py\
tweepy + oauth!\
@CoderDrax  Latest Covid Updates:-\
                   Total Cases : 233,569,801 \
Active Cases :18,399,778    Closed… https://t.co/26sbqm3ZJd\
RT @chinryu: 日本のツイートトレンドTOP10は['ゴルゴ13', '岸田さん', '決選投票', 'さいとう・たかをさん死去', '高市さん', 'すい臓がんのため死去', '本人の遺志', 'オリコン', 'いとう先生',\ '#自民党総裁選']です #Pytho…\
日本のツイートトレンドTOP10は['ゴルゴ13', '岸田さん', '決選投票', 'さいとう・たかをさん死去', '高市さん', 'すい臓がんのため死去', '本人の遺志', 'オリコン', 'いとう先生', '#自民党総\裁選']です #Python #Tweepy\
hello tweepy ですよん\
@CoderDrax  Latest Covid Updates:-\
                   Total Cases : 233,569,801 \
Active Cases :18,399,778    Closed… https://t.co/1btK1p5Len\
hello tweepy tweet\
hello tweepy tweet https://t.co/9RsHR0XAIU\
日本のツイートトレンドTOP10は['ゴルゴ13', 'さいとう・たかをさん死去', 'オリコン', '本人の遺志', 'すい臓がんのため死去', 'いとう先生', '#出産直後の感想教えて', '#招き猫の日', '… \https://t.co/Tfa7oqPGQA\
hello tweepy\
