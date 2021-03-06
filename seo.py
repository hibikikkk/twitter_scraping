import MeCab
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def scraip(html):
    result = []

    url = requests.get(html)
    soup = BeautifulSoup(url.content,"html.parser")

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
    if len(sample8) > 0:
        for counter in range(len(sample8)):
            result.append(sample8[counter])



    file = open("copas.text","w")
    for i in range(len(result)):
        file.write(result[i].text+"\n")


    file.close()

def seo_search(wakati):
    print("ここはseo_searchの中の" + str(wakati))
    sub_dict = {}
    for i in range(len(wakati)):
        if sub_dict.get(str(wakati[i])) == None:
            sub_dict[str(wakati[i])] = 0

    for j in wakati:
        if j in sub_dict:
            sub_dict[j] += 1

    return sub_dict

def joinList2(mecab):
    print("ここはjoinList2の中の" + str(mecab))
    joins = []
    for i in range(len(mecab)):
        try:
            joins.append(mecab[i])
        except:
            pass

    return joins

def delete_joshi(mecab):
    print("ここはdelete_joshiの中の" + str(mecab))
    returnItem = []
    for i in mecab:
        if i[1] == "名詞" and i[2] != "":
            returnItem.append(i[0])
        elif i[1] == "名詞":
            returnItem.append(i[0])

    return returnItem

def mecab_list(text):
    m = MeCab.Tagger("-Ochasen")
    m.parse("")
    disas = m.parseToNode(text)
    outputList = []

    while disas:
        word = disas.surface
        part = disas.feature.split(',')
        if part[0] != u'BOS/EOS':
            if part[6] == None:
                outputList.append([word,part[0],""])
            elif part[6] != "*":
                outputList.append([word,part[0],part[6]])
            else:
                outputList.append([word,part[0],""])

        disas = disas.next
    return outputList

def list_connect(lists):
    counter = 1
    connected_list = []
    for i in lists:
        try:
            if i[1] == "名詞" and lists[counter][1] == "名詞" and lists[counter+1][1] == "名詞":
                connected_list.append([str(i[0]+lists[counter][0]+lists[counter+1][0]),"名詞",str(i[2]+lists[counter][2]+lists[counter+1][2])])

            elif i[1] == "名詞" and lists[counter][1] == "名詞":
                connected_list.append([str(i[0]+lists[counter][0]),"名詞",str(i[2]+lists[counter][2])])
            #else:
                #connected_list.append(i)

        except:
            connected_list.append(i)

        counter += 1
    return  connected_list

if __name__ == "__main__":
    sub = []
    graph_num = []
    graph_word = []
    inputLine = input("URLを入力してください\n")
    scraip(inputLine)

    file_sub = open("copas.text","r")
    print(type(file_sub))
    text = file_sub.read()
    print("抽出結果は\n"+text)
    #print(seo_search(joinList2(delete_joshi(mecab_list(file_sub.read())))))

    for k in sorted(seo_search(joinList2(delete_joshi(list_connect(mecab_list(text))))).items(), key=lambda x: x[1], reverse=True):
        sub.append(list(k))
        if k[1] > 3:
            graph_num.append(k[1])
            graph_word.append(k[0])

    df = pd.DataFrame(sub,columns=["word","number"])
    df.to_csv("result_seo.csv")
    file_sub.close()


    plt.pie(np.array(graph_num),labels=graph_word,counterclock=False, startangle=90,wedgeprops={'linewidth': 3, 'edgecolor':"white"},autopct="%1.1f%%")
    plt.show()
