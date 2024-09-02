from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
mymodel=SentimentIntensityAnalyzer()
k=input("Enter the text")
pred=mymodel.polarity_scores(k)
if(pred['compound']>0.5):
    print("Sentiment is Posiive")
elif(pred['compound']<-0.5):
    print("Sentiment is Negative")
else:
    print("Sentiment is Neutral")

