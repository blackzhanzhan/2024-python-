'''
1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['kitty', 'Tom', 'richard']，输出：['Kitty', 'Tom', 'Richard']：
  测试功能：
  L1 = ['kitty', 'TOm', 'richard']
  L2 = list(map(normalize, L1))
  print(L2)
'''

def normalize(s):
    return s.capitalize()


L1 = ['kitty', 'Tom', 'richard']
L2 = list(map(normalize, L1))
print(L2)
