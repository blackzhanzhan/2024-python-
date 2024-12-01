"""
程序功能，模拟评委打分，包括五个评委，一个大众评委
"""
import random

allplayer=[]
for i in range(6):
    print("请给第{}个选手打分".format(i+1))
    score=[]
    for i in range(5):
        jscore=eval((input("请第{}个评委打分：10分制  ".format(i+1))))
        score.append(jscore)
    score.sort()
    score.pop()
    score.pop(0)
    #产生一百个60-100的随机数作为大众分数
    ass=0
    for i in range(100):
        ass+=random.randint(60,100)
    print("第{}位选手观众评分：".format(i+1))
    ass=ass/100
    print(ass)
    score.append(ass)
    print("选手的最后得分：为",sum(score))#sum为python的内置函数，不属于对象行为
    allplayer.append(score)
print("所有选手的得分情况为：",allplayer)

#对所有选手的成绩进行排序
allplayer.sort(key=lambda x:sum(x),reverse=True)
print("选手得分排序后为：",allplayer)

#前三名为一等奖
firstRank=allplayer[0:3]
print("一等奖选手成绩为：")
print(firstRank)

#四到六名为二等奖
secondRank=allplayer[3:7]
print("二等奖选手成绩为：")
print(secondRank)