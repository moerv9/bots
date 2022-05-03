#Init Config with Twitter API Token
from config import ConfigAPI
newconf = ConfigAPI()
api = newconf.create_api("auth1")

class Tweets():
    def __init__(self):
        pass

    def get_elons_tweets(self):
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
                
        texts = [tweet.full_text for tweet in list]
        timestamps =[tweet.created_at.strftime("%d/%m/%Y, %H:%M:%S") for tweet in list]
        return texts, timestamps