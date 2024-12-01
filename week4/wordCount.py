text='''
Yang Zhongmin, president of SCNU, also attended the main ceremony and extended a warm welcome to the new students from home and 39 other countries around the world. In his speech titled "Shouldering the Mission on the Road of Pursuing Dreams", he pointed out, every student made efforts to gather here and open a new chapter of life at SCNU. "SCNUer" will become their new identity and the identity will accompany them for the rest of their lives.
'''

wordList=text.split()
stopWord=['the','of','for','to','and','also','a']
wordFrenquency={}


for word in wordList:
    if word in stopWord:
        continue
    wordFrenquency[word] =wordFrenquency.get(word,0)+1

sortedWord=sorted(wordFrenquency.items(),key=lambda x:x[1],reverse=True)
print(sortedWord)
