import glob
import math
import pprint


import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

stopWD = set(stopwords.words("arabic"))

ArrFiles = []
uniqSet = {}
BofWords = []
TFCalculated=[]
IDFCalculated=[]
IDF =[]
TF__IDF=[]
MyDirectory =r'd:\SANAD\Culture\Trainingset\*.txt'
# read files from directory either training set or testing set
for path in sorted(glob.iglob(MyDirectory)):
    text_file = open(path, encoding='utf-8').read().replace('\n', ' ')
    ArrFiles.append(text_file.replace('  ', ' ').split(" "))
# remove stop words
length = len(ArrFiles)
i = 0
while i < length:
    for w in ArrFiles[i]:
        if w in stopWD or w == '':
            ArrFiles[i].remove(w)
    i += 1
# Create unique set to calculate IDF
for arr in ArrFiles:
    for word in arr:
        uniqSet = set(arr).union(set(uniqSet))

# generate Bag of words dictionary to compare with unique set
i = 0
while i < length:
    linf = dict.fromkeys(uniqSet, 0)
    for word122 in ArrFiles[i]:
        linf[word122] += 1
    BofWords.append(linf)
    i += 1


#these fuction to calculate the tf-idf for all words
def calcTFIDF(tf,idf):
  tf_idf={}
  for w,v in tf.items():
     tf_idf[w]=v *idf[w]
  return tf_idf

def calculateTF(wordsDict,BagOfWords):
  tfdict={}
  bagofwordcount=len(BagOfWords)
  for word ,count in wordsDict.items():
    tfdict[word]=count/ float(bagofwordcount)
  return tfdict

def calculateIDF(documentss):
  N=len(documentss)
  idf=dict.fromkeys(documentss[0].keys(),0)
  for d in documentss:
    for w,v in d.items():
      if v>0:
        idf[w] +=1
  for w,v in idf.items():
      idf[w]=math.log(N/float(v))
  return idf

# [print(d) for d in BofWords]

l=len(BofWords)
i=0
while i< l:
    TFCalculated.append(calculateTF(BofWords[i],ArrFiles[i]))
    i+=1

i=0
print('tf calculated')
[print(d) for d in TFCalculated]
#

IDF.append(calculateIDF(BofWords))
pprint.pprint(IDF)

i=0
while i < len(IDF):
    TF__IDF.append(calcTFIDF(TFCalculated[i],IDF[0]))
    i=+1
pprint.pprint(TF__IDF)






