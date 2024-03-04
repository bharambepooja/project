import streamlit as st
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px
st.title("SENTIMENT ANALYSIS SYSTEM")
st.sidebar.image("https://miro.medium.com/v2/resize:fit:1400/1*j2Br9DJ5s4yC3hZBzKsvZQ.png")
choice=st.sidebar.selectbox("My Menu",("Home","Analyze Sentiment","Visualize the Results","CSV FILE"))
if (choice=="Home"):
    st.image("https://miro.medium.com/v2/1*_JW1JaMpK_fVGld8pd1_JQ.gif")
    st.markdown("<center><h1>WELCOME</h1></center>",unsafe_allow_html=True)
elif(choice=="Analyze Sentiment"):
    url=st.text_input("Enter Google Sheet URL")
    r=st.text_input("Enter Range")
    c=st.text_input("Enter Column")
    btn=st.button("Analyze")
    if btn:
        if 'cred' not in st.session_state:
            f= InstalledAppFlow.from_client_secrets_file('key.json.json',['https://www.googleapis.com/auth/spreadsheets'])
            st.session_state['cred']=f.run_local_server(port=0)
        mymodel=SentimentIntensityAnalyzer()
        service=build('Sheets','v4',credentials=st.session_state['cred']).spreadsheets().values()
        d=service.get(spreadsheetId=url,range=r).execute()
        mycolumns=d['values'][0]
        mydata=d['values'][1:]
        df=pd.DataFrame(data=mydata,columns=mycolumns)
        l=[]
        for i in range(0,len(df)):
            k=df._get_value(i,c)
            pred=mymodel.polarity_scores(k)
            if(pred['compound']>0.5):
                l.append("Positive")
            elif(pred['compound']<-0.5):
                l.append("Negative")
            else:
                l.append("Neutral")
        df['Sentiment']=l
        st.dataframe(df)
        df.to_csv("Review.csv",index=False)
        st.header("This data has been saved by the name of review.csv")
elif(choice=="Visualize the Results"):
    choice2=st.selectbox("Choose Visualization",("None","Pie","Histogram"))
    if (choice2=="Pie"):
        df=pd.read_csv("Review.csv")
        posper=(len(df[df['Sentiment']=='Positive'])/len(df))*100
        negper=(len(df[df['Sentiment']=='Negative'])/len(df))*100
        neuper=(len(df[df['Sentiment']=='Neutral'])/len(df))*100
        fig=px.pie(values=[posper,negper,neuper],names=['Positive','Negative','Neutral'])
        st.plotly_chart(fig)
    elif(choice2=="Histogram"):
        t=st.text_input("Choose any Categorical Column")
        if t:
            df=pd.read_csv("Review.csv")
            fig=px.histogram(x=df['Sentiment'],color=df[t])
            st.plotly_chart(fig)
elif(choice=="CSV FILE"):
    path=st.text_input("Enter File Path")
    c=st.text_input("Enter Column")
    btn=st.button("Analyze")
    if btn:
        if 'cred' not in st.session_state:
            f= InstalledAppFlow.from_client_secrets_file('key.json.json',['https://www.googleapis.com/auth/spreadsheets'])
            st.session_state['cred']=f.run_local_server(port=0)
        mymodel=SentimentIntensityAnalyzer()
        df=pd.read_csv(path)
        l=[]
        for i in range(0,len(df)):
            k=df._get_value(i,c)
            pred=mymodel.polarity_scores(k)
            if(pred['compound']>0.5):
                l.append("Positive")
            elif(pred['compound']<-0.5):
                l.append("Negative")
            else:
                l.append("Neutral")
        df['Sentiment']=l
        st.dataframe(df)
        df.to_csv("Review.csv",index=False)
        st.header("This data has been saved by the name of review.csv")
