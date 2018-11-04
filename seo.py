import MeCab
import requests
from bs4 import BeautifulSoup

def scraip():
    result = []

    url = requests.get("https://blog.goo.ne.jp/isehakusandou")
    soup = BeautifulSoup(url.text,"html.parser")

    sample1 = soup.find_all("title")
    if len(sample1) > 0:
        for counter in range(len(sample1)):
            result.append(sample1[counter])

    sample2 = soup.find_all("span")
    if len(sample2) > 0:
        for counter in range(len(sample2)):
            result.append(sample2[counter])


    sample3 = soup.find_all("h2")
    if len(sample3) > 0:
        for counter in range(len(sample3)):
            result.append(sample3[counter])


    sample4 = soup.find_all("h3")
    if len(sample4) > 0:
        for counter in range(len(sample4)):
            result.append(sample4[counter])


    sample5 = soup.find_all("h4")
    if len(sample5) > 0:
        for counter in range(len(sample5)):
            result.append(sample5[counter])


    sample6 = soup.find_all("h5")
    if len(sample6) > 0:
        for counter in range(len(sample6)):
            result.append(sample6[counter])


    sample7 = soup.find_all("h6")
    if len(sample7) > 0:
        for counter in range(len(sample7)):
            result.append(sample7[counter])


    sample8 = soup.find_all("p")
    print(sample8[0])
    if len(sample8) > 0:
        for counter in range(len(sample8)):
            result.append(sample8[counter])



    file = open("copas.text","w")
    for i in range(len(result)):
        file.write(result[i].text+"\n")

    file.close()

def seo_search(wakati):
    sub_dict = {}
    for i in range(len(wakati)):
        if sub_dict.get(str(wakati[i])) == None:
            sub_dict[str(wakati[i])] = 0

    for j in wakati:
        if j in sub_dict:
            sub_dict[j] += 1

    return sub_dict

def joinList2(mecab):
    joins = []
    for i in range(len(mecab)):
        try:
            joins.append(mecab[i]+mecab[i+1])
        except:
            pass
    return joins

def delete_joshi(mecab):
    returnItem = []
    for i in mecab:
        if i == "は" or i == "に" or i == "と" or i == "を" or i == "の" or i == "。"or  i == "、" or i == "です" or i == "この" or i == "その" or i == "あの" or i == "ます" or i == "って" or i == "？" or i == "「" or i == "」" or i == "で" or i == "へ" or i == "»" or i == "な" or i == "う" or i == "ましょ" or i == "これ" or i == "それ" or i == "あれ" or i == "どれ" or i == "ここ" or i == "そこ" or i == "あそこ" or i == "どこ" or i == "こちら" or i == "こっち" or i == "そちら" or i == "そっち" or i == "あちら" or i == "あっち" or i == "どちら" or i == "どっち" or i == "この" or i == "その" or i == "あの" or i == "どの" or i == "こう" or i == "そう" or i == "ああ" or i == "どう" or i == "こんなだ" or i == "そんなだ" or i == "あんなだ" or i == "どんなだ" or i == "・" or i == "し" or i == "ました" or i == "【" or i == "】" or i == "." or i == "*" or i == '"' or i == "'" or i == "が" or i == "て" or i == "こと" or i == "ません" or i == "[" or i == "]" or i == "！" or i == "ません" or i == "した" or i == "という":
            continue
        else:
            returnItem.append(i)
    return returnItem

scraip()

file_sub = open("copas.text","r")
file_res = open("result_seo.text","w")
m = MeCab.Tagger("-Owakati")
#print(list(m.parse(file_sub.read()).split(" ")))
for k in sorted(seo_search(joinList2(delete_joshi(list(m.parse(file_sub.read()).split(" "))))).items(), key=lambda x: x[1], reverse=True):
    file_res.write(str(k) + "\n")

file_sub.close()
file_res.close()
