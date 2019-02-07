from textblob import TextBlob

C = TextBlob("hello i am happy")

print(C.tags)

print(C.sentiment.polarity)