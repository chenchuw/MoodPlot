### EC601_Project2

# Cloud Natural Language API
First I used Google's Cloud Natural Language API. It is Google's proven pre-trained model for general content classification; sentiment analysis; entity recognition, etc. After getting access to the client library, I connected to the Cloud and tested sentiments for several sentences using my python script. The script is called language.py in this repository. A snippet of the output is attached below:

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

# AutoML Sentiment Analysis
Second, I investigated Google's AutoML sentiment analysis. In short, I built a machine learning model to analyze attitudes within text & documents. Following are some examples of the sentiment analysis:

![Sentiment#1](https://github.com/Mockingbirdzzz/EC601_Project2/blob/main/Screen%20Shot%202021-09-29%20at%2002.10.23.png?raw=true)
![Sentiment#2](https://github.com/Mockingbirdzzz/EC601_Project2/blob/main/Screen%20Shot%202021-09-29%20at%2002.12.41.png?raw=true)

# AutoML Text & Document Classification
I also tried the single text classification feature. In short, I built a machine learning model to classify content into a custom set of categories. Following are some exmpales of the text classification:

![Classification#1](https://github.com/Mockingbirdzzz/EC601_Project2/blob/main/Screen%20Shot%202021-09-29%20at%2002.17.07.png?raw=true)
![Classification#2](https://github.com/Mockingbirdzzz/EC601_Project2/blob/main/Screen%20Shot%202021-09-29%20at%2002.17.28.png?raw=true)

# Twitter API (Retrieving Tweets)

A program to retrive tweets. Python script is called Tweeter_Retrive.py in this repository. The output is below:

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
