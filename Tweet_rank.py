import urllib.request
from requests_oauthlib import OAuth1Session # ライブラリ(1)
import pandas as pd
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

#ツイート情報取得で使うアクセスアカウント
keys = pd.read_csv("/Users/kudouhibiki/Desktop/python_program/twitter_keys.csv")
CONSUMER_KEY = keys['keys'][0]
CONSUMER_SECRET = keys['keys'][1]
ACCESS_TOKEN = keys['keys'][2]
ACCESS_SECRET = keys['keys'][3]

#アクセス処理
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンスを作成
api = tweepy.API(auth)
#検索キーワード入力
q = "min_retweets:10000 min_faves:2000 lang:ja" #11since: + str(datetime.date.yesterday())
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
    #検索読み込み待機時間
    if counter == 0:
        time.sleep(1)

        if 'media' in result.entities and len(result.extended_entities) > 0:
            for i in range(len(result.extended_entities)):
                print(result.extended_entities['media'][i]['media_url'])


    if not "公式" in result.user.name and  not "公式" in result.user.description and not result.user.verified and not "official" in result.user._json['screen_name'] and result.user.followers_count - result.user.friends_count <= 10000:
        userdata.append([result.user._json['screen_name'],result.id,result.user.name,result.text,result.created_at,result.favorite_count,result.favorite_count+(result.retweet_count*3)])
        #print(str(userdata[counter])+"\n")
        #print(result.user.description)
        counter += 1
    #データをテキストに出力
    #text.write(str(userdata[counter]) + "\n")



counter = 0
text.write("今月のバズったツイートランキング！！\n")
#データのファボランキングをし、埋め込みHTMlをテキストに保存する処理
for result in userdata:
    userdata.sort(key=lambda x:x[6])
    userdata.reverse()
    text.write("ランキング " + str(counter + 1)+"位！！！\n")
    text.write("点数: " + str(userdata[counter][6]) + "点\n")
    text.write("https://twitter.com/" + userdata[counter][0] +"/status/"+ str(userdata[counter][1])  + "\n")
#    text.write(str(get_today_embed(result.id,result.user._json['screen_name'])) + "\n")
    counter += 1
    print(type(result[4]))


text.close()
