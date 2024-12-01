import numpy as np

from week10.code.scores2jsoncsv import score, scores

# 加载CSV文件
data = np.genfromtxt('../data/cs.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')

# 提取各列
ids = data['Id']
nos = data['No']
majors = data['Major']
courses = data['Course']
scores = data['Score']

def get_grade(score):
    if score >= 90:
        return 'Excellent'
    elif score >= 80:
        return 'Good'
    elif score >= 70:
        return 'Medium'
    elif score >= 60:
        return 'Pass'
    else:
        return 'Fail'

unique_nos = np.unique(nos)

student_results = []

for no in unique_nos:
    student_scores = scores[nos == no]
    avg_score = np.mean(student_scores)
    total_courses = len(student_scores)

    grades = [get_grade(score) for score in student_scores]
    grade_counts = {
        'Excellent': grades.count('Excellent'),
        'Good': grades.count('Good'),
        'Medium': grades.count('Medium'),
        'Pass': grades.count('Pass'),
        'Fail': grades.count('Fail')
    }

    student_results.append({
        'No': no,
        'Avg': avg_score,
        'Total': total_courses,
        'Excellent': grade_counts['Excellent'] / total_courses,
        'Good': grade_counts['Good'] / total_courses,
        'Medium': grade_counts['Medium'] / total_courses,
        'Pass': grade_counts['Pass'] / total_courses,
        'Fail': grade_counts['Fail'] / total_courses
    })

    # 按平均分排序
student_results = sorted(student_results, key=lambda x: x['Avg'], reverse=True)

    # 打印结果
with open()



