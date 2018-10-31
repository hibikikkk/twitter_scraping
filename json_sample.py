import json
import urllib.request

def main():
  try:
     url = 'https://data-api.twitter.com/insights/engagement/28hr'
     res = urllib.request.urlopen(url)
     data = json.loads(res.read().decode('utf-8')) # 実行結果(json)をdata変数に格納
  except urllib.error.HTTPError as e:
     print('HTTPError: ', e)
  except json.JSONDecodeError as e:
     print('JSONDecodeError: ', e)

  for key in data['images']:
    print(key['title']) # titleのみ参照



if __name__ == '__main__':
    main()
