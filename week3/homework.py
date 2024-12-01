
def my_myputnum(b,new_b):
    while 1:
        a=input("请输入数字，输入end结束输入")
        if(a=="end"):
            break
        a=int(a)
        b.append(a)

#去除字符中的元音
def question1():
    a=input("请输入英文字符：")
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_a = ''

    for i in a:
        if i.lower() in vowels:
            #改为空格
            new_a += ' '
        else:
            new_a += i  

    print(new_a)

def odd(num):
    if num%2!=0:
        return True
    return False


def question2_3():
    b=[]
    new_b=[]
    my_myputnum(b,new_b)
    for i in b:
        if(odd(i)):
            new_b.append(i)
    
    return new_b

def question4():
    b=[]
    new_b=[]
    my_myputnum(b,new_b)

    for i in b:
        new_b.append(i*10)
    
    return new_b

def question5():
    b=[]
    new_b =[]
    my_myputnum(b,new_b)
    for i in b:
        if i*i>50:
            new_b.append(i)
    return new_b

def question6():
    #将重复字符串删除，如aaabbbccc变为abc
    a=input("请输入字符串")
    b=[]
    new_b = []
    for i in a:
        b.append(i)
    
    for i in b:
        if i not in new_b:
            new_b.append(i)
    return new_b

menu = (
    ["牛奶", "虎皮蛋糕"],
    ["南瓜瘦肉粥", "牛奶杯子蛋糕"],
    ["牛奶", "牛角包"],
    ["菜心瘦肉汤", "三丝炒米粉"],
    ["腐皮玉米瘦肉粥", "三酱肠粉"]
)
if __name__=='__main__':
    print(question6)

