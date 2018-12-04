import csv
import string
import math
import operator
import matplotlib.pyplot as plt
import numpy as np
from docutils.nodes import classifier
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def eliminateTags(str,tags):
    ind = str.find(tags)
    while (ind!=-1):
        indEnd = str.find(' ',ind+len(tags))
        str = str[0:ind] + str[indEnd:]
        ind = str.find(tags)
    return str

def removePunctuation(str):
    newStr = ''
    for i in str:
        if i not in string.punctuation:
            newStr+=i
    return newStr

def countLettersAndWords(str):
    listStr = str.split(' ')
    tmp=[]
    chars = 0
    for i in listStr:
        if i != '':
            tmp.append(i)
            chars+=len(i)
    return (tmp,len(tmp),chars)

def bagOfWords(tweets):
    bagOfWords = []
    for ls in tweets:
        for w in ls[0]:
            bagOfWords.append(w)
    return bagOfWords


def removeStopWords(bow):
    stop = stopwords.words('english')
    newBow = []
    for w in bow:
        if w not in stop:
            newBow.append(w)
    return newBow

def numberOfWords(bow):
    wcDict = dict([])
    for i in bow:
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

def showDistributionOfWords(allWords,w):
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

def showSentimentDist(bow):
    sid = SentimentIntensityAnalyzer()
    concat = ''
    for w in bow:
        concat += w + ' '
    ss = sid.polarity_scores(concat)
    values=[]
    labels=[]
    for k in ss:
        print('{}: {}'.format(k,ss[k],end=' '))
        labels.append(k)
        values.append(ss[k])
    plt.pie(values[:-1],labels=labels[:-1],colors=['red','grey','green'],shadow = True, startangle = 90)
    plt.title('Distribution of different sentimel words.')
    plt.show()

#MAIN:
inCsv = csv.reader(open('TrumpTweets.csv','r',encoding="utf8"),delimiter=';')
tweets = []
for i in inCsv:
    lowcase = i[4].lower()
    clearStr = eliminateTags(lowcase,'http')
    clearStr = eliminateTags(clearStr,'pic.')
    clearStr = eliminateTags(clearStr,'# ')
    clearStr = eliminateTags(clearStr,'@ ')
    clearStr = removePunctuation(clearStr)
    tweets.append(countLettersAndWords(clearStr))
    # print(tweets[len(tweets)-1])


bow = bagOfWords(tweets)

print(len(set(bow))/len(bow))

bow = removeStopWords(bow)
print(len(bow))

wcDict = numberOfWords(bow)
for k,v in wcDict:
    print(k,':',v)


showTopNWords(wcDict,10)

showDistributionOfWords(bow,['great', 'thank', 'people', 'hillary', 'us', 'america', 'big', 'money'])

showSentimentDist(bow)

