import datetime
import copy
import TwitterAPI
import tweepy

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
tweet_info = []

def tweet_bus_rank():

    now = datetime.datetime.now()
    counter = 0

    for tweets in tweet_info:
        tweetTime = tweets[4]

        day_dif = now.day - tweetTime.day
        hour_dif = now.hour - tweetTime.hour
        minute_dif = now.minute - tweetTime.minute
        second_dif = now.second - tweetTime.second

        total_second = day_dif*86400 + hour_dif*3600 + minute_dif*60 + second_dif

        if total_second > 1800:
            tweet_info[counter].append((tweets[5]+tweets[6]) / total_second * 10)

        counter += 1





def tweet_search():
    global tweet_info
    tweet_medias = []

    #検索キーワード入力
    q = "min_retweets:10000 min_faves:2000 lang:ja" #since: + str(datetime.date.today())
    search_results = api.search(q=q, count=10000)

    #検索
    for result in search_results:
        #画像データか動画データがあるなら取得
        if 'media' in result.entities:
            for i in range(len(result.extended_entities)):
                if result.extended_entities['media'][0].get('video_info') != None:
                    tweet_medias.append(result.extended_entities['media'][0]['video_info']['variants'][0]["url"])
                else:
                    tweet_medias.append(result.extended_entities['media'][i]['media_url'])



#        if not "公式" in result.user.name and  not "公式" in result.user.description and not result.user.verified and not "official" in result.user._json['screen_name'] and result.user.followers_count - result.user.friends_count <= 10000:
        tweet_info.append([result.user._json['screen_name'], result.id, result.user.name, result.text, result.created_at, result.favorite_count, result.retweet_count, copy.deepcopy(tweet_medias)])


def reply():
    counter = 0
    now = datetime.datetime.now()

    for i in tweet_info:
        #time.sleep(60)
        if i[8] != None and counter < 100:
            replyText = "@"+ i[0] + "\n" + "バズっています！！\n" + "ポイント:" + str(round(i[8]*100)) + "pt\n" + "現在" + str(counter+1) + "位"
            #api.update_status(status=replyText.encode("UTF-8"), in_reply_to_status_id=i[1])
            #print(replyText + "\n")
            print(i[2])
            counter += 1



if __name__ == "__main__":
    tweet_search()
    tweet_bus_rank()
    tweet_info.sort(key=lambda x:x[8])
    tweet_info.reverse()
    reply()
