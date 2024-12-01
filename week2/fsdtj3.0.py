"""
    功能：学生成绩（百分制）等级人数统计
          统计不同分数段学生人数要求：
            “不及格”：小于60；
            “及格”：大于等于60小于75；
            “良好”：大于等于75小于85
            “优秀”：大于等于85
    作者：张三
    日期：20211014
    版本：3.0
    V3.0版本新增功能：输入的成绩先放在分数列表中，统计的各类人数也存放在列表中
"""

scores = []       #初始化学生成绩列表
#任务1：输入30个学生成绩(需要判断成绩有效性，无效成绩重新输入)，加入到成绩列表
for i in range(30):
  a=i
  while True:
    try:
      user_input = int(input("请输入第{}个学生的成绩(0到100之间的整数): ").format(a+1) )
      if  0<= user_input <= 100:
        break
    except ValueError:
      print("输入无效，请重新输入。")


score_level = [0,0,0,0]   #初始化成绩等级人数列表：[不及格，及格，良好，优秀]
#任务2：遍历成绩列表，统计各分数段存入成绩等级人数列表
for score in scores:
  if(score<60):
    score_level[0]+=1
  elif(60<=score<=75):
    score_level[1]+=1
  elif(75<=score<=85):
    score_level[2]+=1
  else:
    score_level[3]+=1

print('各分数段人数为：不及格{}人，及格{}人，良好{}人，优秀{}人'.format(score_level[0],score_level[1],score_level[2],score_level[3]))
#任务3：输出全班最高分、最低分、平均分
scores.sort()
highest_score =scores[-1]
low_score = scores[0]
avg_score = sum(scores)/len(scores)
print("全班最高分为",highest_score)
print("全班平均分为",avg_score)
print("全班最低分为",low_score)
#任务4：列出全班前十名的成绩
print("全班前十名成绩为：",scores[-1:-11:-1])
pass