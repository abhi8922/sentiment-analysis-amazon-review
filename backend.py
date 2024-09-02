import pandas as pd
import plotly.express as px
df=pd.read_csv("results.csv")
posper=(len(df[df['Sentiment']=='Positive'])/len(df))*100
negper=(len(df[df['Sentiment']=='Negative'])/len(df))*100
neuper=(len(df[df['Sentiment']=='Neutral'])/len(df))*100
fig=px.pie(values=[posper,negper,neuper],names=['Positive','Negative','Neutral'])
fig.show()
