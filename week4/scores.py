scores={'zhanshan':45,'lisi':78,'wangwu':40,'zhouliu':96,'zhaoqi':65,'sunba':90,'zhengjiu':78,'wushi':96,'dongshiyi':60}
highest=max(scores.values())
print("最高分",highest)

highestPerson=[name for name,score in scores.items() if score==highest]
print("第一名",highestPerson)

sortedScores=[sorted(scores.items(),key = lambda x:x[1],reverse = True)]
#回去研究下面的code
third=sortedScores[:3]
for i in sortedScores:
    if i==sortedScores[3].value:
        third.append(i)

print("全班前三名",third)

