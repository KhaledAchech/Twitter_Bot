import tweepy
import random
# Authenticate to Twitter
auth = tweepy.OAuthHandler("API key", "API secret key")
auth.set_access_token("Access token", "Access token secret")

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hello Tweepy")
#get the last tweet of one of these ids 
user_id = ['IGN','GameSpot','UnrealEngine','JVCom']
tweets = api.user_timeline(screen_name=user_id[random.randint(0,3)], 
                           # 200 is the maximum allowed count
                           count = 1,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )


for info in tweets:
	status_id = info.id

#retweeting those tweets :)
api.retweet(status_id)


#automatic message to my best friend when am working :)
# ID of the recipient 
recipient = #put the id of the recipient here 
  
# text to be sent 
text = "write your text here "
api.send_direct_message(recipient,text)