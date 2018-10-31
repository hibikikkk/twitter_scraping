from twitter import Twitter, OAuth
import TwitterAPI
import tweepy
import os

def rep_save():
    for result in search_results:
        if  Lists == []:
            Lists.append(result.user._json['screen_name'])

        elif result in Lists:
            continue

        else:
            Lists.append(result.user._json['screen_name'])


def rep_rank():
    for result1 in Lists:
        if res_dic.get(str(result1)) == None:
            res_dic[str(result1)] = 0



    for result2 in search_results:
        if str(result2.user._json['screen_name']) in res_dic:
            res_dic[str(result2.user._json['screen_name'])] += 1


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
q = "to:kiyohiro_0728"
count = 1000

#検索
search_results = api.search(q=q, count=count)
Lists = []
res_dic = {}


file = open("rep.txt","w")
rep_save()
rep_rank()
file.write("検索数:"+str(count)+"\n")
for i in sorted(res_dic.items(), key=lambda x: x[1], reverse=True):
    file.write(str(i) + "\n")
file.close
