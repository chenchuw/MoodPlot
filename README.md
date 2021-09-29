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
