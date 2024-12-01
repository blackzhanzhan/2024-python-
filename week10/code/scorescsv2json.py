"""
    作者：张三
    功能：将存储成绩数据的csv文件（scores.csv）转换并写入scores.json文件
          csv格式为：学号,语文,数学,英语,总分
                     201805,147,101,76,324
                     201809,93,145,53,291
    版本：1.0
    日期：10/22/2024
"""
import json
import csv

from week9.practice.student_score import score_list

# 任务1：利用csv库读取csv文件到列表scores_list
scores_list=[]
with open('../data/scores.csv','r',encoding='utf-8') as fout:
    reader = csv.reader(fout)
    for row in reader:
        score_list.append(row)
print('task1 test')
print(scores_list)

# 任务2：转换并准备成列表嵌套字典scores_dict
scores_dict =[]
for row in scores_list:
    student_id = f"学号:{row['学号']}"
    scores = {
        '语文': int(row['语文']),
        '数学': int(row['数学']),
        '英语': int(row['英语']),
        '总分': int(row['总分'])
    }
    scores_dict.append((student_id, scores))
    print('task2 test')
    print(scores_dict)

# 任务3：将字典数据写入文件scores.json
with open('../data/scores.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(scores_dict, jsonfile, ensure_ascii=False, indent=4)
