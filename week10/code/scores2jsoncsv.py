"""
    作者：张三
    功能：将列表中的成绩数据写入scores.json文件，转换并写入规范的csv文件（scores.csv）
    版本：1.0
    日期：10/22/2024
"""
import json
import csv
# 列表scores中存储了10个学生的成绩
scores = [('学号:201801', {'语文': 148, '数学': 141, '英语': 68, '总分': 357}), ('学号:201803', {'语文': 140, '数学': 79, '英语': 85, '总分': 304}), ('学号:201807', {'语文': 146, '数学': 101, '英语': 57, '总分': 304}), ('学号:201809', {'语文': 119, '数学': 106, '英语': 69, '总分': 294}), ('学号:201804', {'语文': 101, '数学': 106, '英语': 78, '总分': 285}), ('学号:201808', {'语文': 100, '数学': 102, '英语': 74, '总分': 276}), ('学号:201805', {'语文': 127, '数学': 76, '英语': 70, '总分': 273}), ('学号:201802', {'语文': 113, '数学': 62, '英语': 80, '总分': 255}), ('学号:201806', {'语文': 76, '数学': 94, '英语': 70, '总分': 240})]

# 任务1：将列表中的成绩数据写入scores.json文件
datajson=json.dumps(scores,sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False)
with open('../data/scores.json', 'w', encoding='utf-8') as fin:
    fin.write(datajson)


# 任务2: 将列表中的成绩数据转换并写入规范的csv文件（scores.csv）
# 格式为：学号,语文,数学,英语,总分
#         201805,147,101,76,324
#         201809,93,145,53,291
fieldnames = ['学号', '语文', '数学', '英语', '总分']
with open('../data/scores.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for score in scores:
        student_id = score[0].split(':')[1]  # 提取学号
        score_dict = {subject: score[1][subject] for subject in score[1]}  # 创建成绩字典
        score_dict['学号'] = student_id  # 添加学号到字典中
        writer.writerow(score_dict)