import random
import pickle

courses = ['语文', '数学', '英语']
scores = {}  # 学号为键，成绩清单为值

# task1 用字典存储语数外的成绩
for stuno in range(201801, 201850):
    score = {}
    for course in courses:
        score[course] = random.randint(60, 100)
    scores["学号：" + str(stuno)] = score

# task2 实现每个学生的总分数统计
for score in scores.values():
    score['总分'] = sum(score.values())

# task3 按总分由高到低排序学号
sorted_scores = sorted(scores.items(), key=lambda x: x[1]['总分'], reverse=True)

# task4 成绩放入文件
score_list = []

for student in sorted_scores:
    line = student[0] + " "
    for subject, score in student[1].items():
        score_str = subject + " " + str(score) + " "
        line += score_str
    line += "\n"
    score_list.append(line)

with open("../data/score.txt", "wt") as fout:
    fout.writelines(score_list)

# task5 将数据以对象形式写入对象文件
with open("../data/score.pkl", "wb") as fout:
    pickle.dump(sorted_scores, fout)

# 读取对象文件并打印
with open("../data/score.pkl", 'rb') as fin:
    data_load = pickle.load(fin)
    print(data_load)