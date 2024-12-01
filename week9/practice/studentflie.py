import random
# 常见的中文姓氏
surnames = [
    '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈',
    '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',

]
# 常见的名字用字
names = [
    '天', '明', '伟', '华', '文', '博', '斌', '磊', '洋', '涛',
    '松', '林', '强', '军', '勇', '刚', '猛', '建', '超', '杰',
]


def generate_name():
    # 随机选择一个姓氏
    surname = random.choice(surnames)
    # 名字可能是单字或双字
    if random.choice([True, False]):
        name = random.choice(names)
    else:
        name = ''.join(random.sample(names, 2))
    return surname + name

def rand_sex():
    a=random.randint(1,2)
    if a==1:
        return '男'
    else:
        return '女'


studentfile_1=[]
studentfile_2=[]

for stuno in range(20232131,2023251):
    stu={}
    stu['学号']=stuno
    stu['姓名']=generate_name()
    stu["性别"]=rand_sex()
    studentfile_1.append(stu)

for stuno in range(2023251,2023351):
    stu={}
    stu['学号']=stuno
    stu['姓名']=generate_name()
    stu["性别"] = rand_sex()
    studentfile_2.append(stu)

print(studentfile_1)

