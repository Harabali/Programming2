# import nltk
# from nltk.book import text1
# nltk.download()

# text1.concordance("the")

import csv
import string
import math
import operator
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords

def removePunctuation(str):
    newStr = ''
    for i in str:
        if i not in string.punctuation:
            newStr+=i
    return newStr

def eliminateTags(str,tags):
    ind = str.find(tags)
    while (ind!=-1):
        tmp = str + " "
        indEnd = tmp.find(' ',ind+2)
        indEnd = min(len(str),indEnd)
        newStr = str[0:ind] + str[indEnd:len(str)]
        str = newStr
        ind = str.find(tags)
    return str

def countLettersAndWords(listStr):
    tmp=[]
    chars = 0
    for i in listStr:
        if i != '':
            tmp.append(i)
            chars+=len(i)
    return (tmp,len(tmp),chars)


def numberOfWords(list):
    wcDict = dict([])
    for i in list:
        if i not in wcDict:
            wcDict[i] = 1
        else:
            wcDict[i] += 1
    return sorted(wcDict.items(), key=operator.itemgetter(1), reverse=True)


def showTopNWords(dict,n):
    x = []
    y = []
    for k,v in wcDict[:n]:
        x.append(k)
        y.append(v)
    plt.barh(x,y)
    plt.yticks(x)
    plt.show()

def showDispersionOfWords(allWords,w):
    x = np.arange(1,len(allWords)+1)
    ys = np.zeros((len(w),len(allWords)))
    ind_i=0
    for i in w:
        ind_j=0
        for j in allWords:
            if i==j:
                ys[ind_i][ind_j] = ind_i+1
            ind_j+=1
        plt.scatter(x,ys[ind_i][:],marker='|')
        plt.ylabel(w)
        plt.ylim(0.1,len(w)+1)
        ind_i += 1
    plt.show()



inCsv = csv.reader(open('TrumpTweets.csv','r',encoding="utf8"),delimiter=';')
tweets = []
for i in inCsv:
    # lower casing
    lowcase = i[4].lower()
    # clearStr = removePunctuation(lowcase)
    clearStr=eliminateTags(lowcase,'http')
    clearStr = eliminateTags(clearStr,'pic.')
    clearStr = eliminateTags(clearStr,'# ')
    clearStr = eliminateTags(clearStr,'@ ')
    clearStr = removePunctuation(clearStr)
    tweets.append(countLettersAndWords(clearStr.split(' ')))
    # print(tweets[len(tweets)-1])

stop = stopwords.words('english')
bagOfWords = []
for ls in tweets:
    for w in ls[0]:
        if w not in stop:
            bagOfWords.append(w)

print(len(set(bagOfWords))/len(bagOfWords))

# wcDict = numberOfWords(bagOfWords)
#
# showTopNWords(wcDict,5)
#
# showDispersionOfWords(bagOfWords,['great', 'thank', 'people', 'hillary', 'us'])

outFile = open('stopWords.txt','w')
for i in stop:
    print(i,file=outFile)
outFile.close()

#Preprocessing:


