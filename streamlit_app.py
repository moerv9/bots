import streamlit as st
import schedule, time
from smart_words import SmartWords
from elons_tweets import Tweets


st.set_page_config(
    page_title="Moerv9 Bots", 
    layout="wide",
    )
st.title("Useful Bots")

#Init Classes
smart_words = SmartWords()
tweets = Tweets()

def get_values():
    print("updated")
    smart_words.get_new_random_word()
    
    
#refresh_rate = st.selectbox("Refresh every...",("Day","Hour","Minute"))
btn = st.button("Refresh")
if btn:
    get_values()


col1, col2 = st.columns(2)
with col1:
    st.subheader("Be smarter by using this word:")
    st.markdown(smart_words.random_word, unsafe_allow_html=True)
    st.markdown("[Source](https://www.der-karriereguru.de/blog/intelligenter-wirken-mit-diesen-50-fremdwortern)")
# schedule.every(10).seconds.do(get_values)

with col2:
    st.subheader("Elon Musks latest Tweets:")
    texts, timestamps = tweets.get_elons_tweets()
    i=0
    for text in texts:
        newstr = text.replace("[","").replace("]","")

        st.write(timestamps[i])
        st.write(newstr)
        i+=1
    st.markdown("[Visit the Github Repo](https://github.com/moerv9/bots)")
    
st.markdown("---")
# while True:
#     schedule.run_pending()
#     time.sleep(1)
