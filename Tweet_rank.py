import urllib.request
from requests_oauthlib import OAuth1Session # ライブラリ(1)
from bs4 import BeautifulSoup
import TwitterAPI
from twitter import Twitter, OAuth
import datetime
import requests
import tweepy
import os
import time

#ツイートのHTML情報取得関数
def get_today_embed(twiId,perId):
    my_url = "https://twitter.com/";
    embed_list = []
    embed_list.append(twitter.statuses.oembed(url=my_url + str(perId) + "/status/" + str(twiId))['html'])
    return embed_list


#html取得で使うアクセスアカウント
twitter = Twitter(auth=OAuth(
        consumer_key='nsk0dbVCmwJZUcjSA3iCsQYxa',
        consumer_secret='HtBZygeCZX20wQo700PQcNsHrtwMsRBUN7gWitf7e9gyTCVNOd',
        token='785221365192273920-EdB3nIcz103ADjOhYSbfYsunewqZE3M',
        token_secret='R7RQDBTYJBuxMjSZ2k8b9QpJGH7vjkaJ7mFbjCIHotsfG'
    ))

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
#検索キーワード入力
q = "min_retweets:10000 min_faves:2000 lang:ja since:" + str(datetime.date.today())
#検索件数
count = 40000
#検索
search_results = api.search(q=q, count=count)
#結果をテキストに保存
text = open("scr_text.txt","w")

userdata = []
counter = 0

#データ取得処理
for result in search_results:
    if counter == 0:
        time.sleep(10)
    userdata.append([result.user._json['screen_name'],result.id,result.user.name,result.text,result.created_at,result.favorite_count,result.favorite_count+(result.retweet_count*3)])
    #データをテキストに出力
    #text.write(str(userdata[counter]) + "\n")
    print(userdata[counter])
    counter += 1


counter = 0
text.write("今月のバズったツイートランキング！！\n")
#データのファボランキングをし、埋め込みHTMlをテキストに保存する処理
for result in search_results:
    userdata.sort(key=lambda x:x[6])
    userdata.reverse()
    text.write("ランキング " + str(counter + 1)+"位！！！\n")
    text.write("点数: " + str(userdata[counter][6]) + "点\n")
    text.write("https://twitter.com/" + userdata[counter][0] +"/status/"+ str(userdata[counter][1])  + "\n")
#    text.write(str(get_today_embed(result.id,result.user._json['screen_name'])) + "\n")
    counter += 1


text.close()
