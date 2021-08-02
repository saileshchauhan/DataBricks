import logging,log
import re
from decouple import config
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    TwitterClient class for authenticating and listening from twitter server.
    '''
    def __init__(self):
        '''
        Description:
            Constructor method for intializing object of class TwitterClient.
        Parameters:
            No parameters.
        Returns:
            None.
        '''
        consumer_key=config('consumer_key')
        consumer_secret=config('consumer_secret')
        acess_token=config('acess_token')
        acess_token_secret=config('acess_token_secret')

        try:
            self.auth=OAuthHandler(consumer_key,consumer_secret)
            self.auth.set_access_token(acess_token,acess_token_secret)
            self.api=tweepy.API(self.auth)
            logging.info("connection succesful")
        except Exception as ex:
            logging.error("Error:Authentication Failed"+str(ex))

    def clean_tweet(self,tweet):
        '''
        Description:
            Method for cleaning fetched tweet based on regex.
        Parameters:
            tweets.
        Returns:
            None.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    def get_tweet_sentiment(self,tweet):
        '''
        Description:
            Method for ananlysing individual polarity of each tweet.
        Parameters:
            tweet.
        Returns:
            None.
        '''
        try:
            analysis=TextBlob(self.clean_tweet(tweet))
            if analysis.sentiment.polarity>0:
                return 'positive'
            elif analysis.sentiment.polarity==0:
                return 'neutral'
            else:
                return 'negative'
        except Exception as ex:
            logging.error('Did not get sentiment'+str(ex))

    def get_tweets(self,query,count=10):
        '''
        Description:
            Method for search keyword and default count of tweets.
        Parameters:
            query,default count of 10
        Returns:
            none.
        '''
        tweets=[]
        try:
            fetched_tweets=self.api.search(q=query,count=count)
            for tweet in fetched_tweets:
                parsed_tweet={}
                parsed_tweet['text']=tweet.text
                parsed_tweet['sentiment']=self.get_tweet_sentiment(tweet.text)

                if tweet.retweet_count>0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
                
            return tweets
        except tweepy.TweepError as ex:
            logging.error("Error : "+str(ex))
    
def main():
    '''
    Description:
    Parameters:
    Returns:
    '''
    api=TwitterClient()
    tweets=api.get_tweets(query='vaccine',count=500)

    ptweets=[tweet for tweet in tweets if tweet['sentiment']=='positive']

    print(f"Positive tweets percentage: {100*len(ptweets)/len(tweets)}")

    ntweets=[tweet for tweet in tweets if tweet['sentiment']=='negative']

    print(f"Negative tweets percentage: {100*len(ptweets)/len(tweets)}")

    print(f"Neutral tweets percentage : {100*(len(tweets)-(len(ntweets)+len(ptweets)))/len(tweets)}")

    print("\n\nPositive tweets:")
    for tweet in ptweets[:5]:
        print(tweet['text'])
    
    print("\n\nNegative tweets:")
    for tweet in ntweets[:5]:
        print(tweet['text'])

if __name__ == "__main__":
    main()