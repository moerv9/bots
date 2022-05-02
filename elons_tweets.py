# Imports
import streamlit as st

#Init Config with Twitter API Token
from config import ConfigAPI
newconf = ConfigAPI()
api = newconf.create_api("auth1")

def get_tweets():
    """Get Tweets from User Timeline

    Returns:
        list: List of Tweets (no Retweets!)
    """
    posts = api.user_timeline(screen_name="elonmusk", count=200,tweet_mode = "extended")
    
    list = []
    for tweet in posts:
        if tweet.full_text.startswith("@"):
            pass
            #TODO: check if tweet is a retweet and show the whole thread
            #full_thread = api.get_status(tweet.id).text
        else:
            list.append(tweet)
    return list

# Streamlit Setup
st.set_page_config(
    page_title="Bots", 
    )
st.title("Elon Musk latest Tweets")
btn = st.button("Refresh")

if btn:
    st.balloons()
    tweets = get_tweets()
    
    texts = [tweet.full_text for tweet in tweets]
    timestamps =[tweet.created_at.strftime("%d/%m/%Y, %H:%M:%S") for tweet in tweets]
    i=0
    for text in texts:
        newstr = text.replace("[","").replace("]","")
        st.subheader("Tweets")
        st.write(timestamps[i])
        st.write(newstr)
        i+=1
    
    st.markdown("---")
    st.markdown("[Visit the Github Repo](https://github.com/moerv9/bots)")