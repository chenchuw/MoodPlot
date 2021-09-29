#!/usr/bin/env python
# encoding: utf-8

import requests
from requests import session
import tweepy # https://github.com/tweepy/tweepy
import json
#Twitter API credentials
consumer_key = "8KMps10UjAdfCZoLzUMOjJtaX"
consumer_secret = "wstgm1dNVCgnPWKiBJ1Z7EPnIjQGzrYgLwvUwvC6N2tQ7z1zFv"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL5iUAEAAAAAmo6FYRjqdKlI3cNziIm%2BHUQB9Xs%3DS31pj0mxARMTOk2g9dvQ1yP9wknvY4FPBPUlE00smJcncw4dPR"

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