import os ,sys
sys.path.append(os.pardir)
from gnip_insights_interface import engagement_api

from twitter import Twitter, OAuth
import TwitterAPI
import tweepy
import os


#ツイート情報取得で使うアクセスアカウント
CONSUMER_KEY = 'nsk0dbVCmwJZUcjSA3iCsQYxa'
CONSUMER_SECRET = 'HtBZygeCZX20wQo700PQcNsHrtwMsRBUN7gWitf7e9gyTCVNOd'
ACCESS_TOKEN = '785221365192273920-EdB3nIcz103ADjOhYSbfYsunewqZE3M'
ACCESS_SECRET = 'R7RQDBTYJBuxMjSZ2k8b9QpJGH7vjkaJ7mFbjCIHotsfG'

#アクセス処理
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンスを作成
api = tweepy.API(auth)
