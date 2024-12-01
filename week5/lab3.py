'''
题目：水果出库
描述：有两个集合，一个表示商店当前包含的水果种类与个数，另一个表示仓库包含的水果种类，从仓库中随机取n次水果（每次取的个数为10以内随机数），n为仓库水果种类数的一半，如果仓库水果数为奇数则向下取整，仓库与商店中水果种类可能有重叠，但仓库与商店中的水果种类均不重复，输出最后商店中水果种类及其对应数量（按数量多少从小到大输出）。
解析：
	1. 两个集合，一个表示种类和个数，所以用字典，另一个列表和Set都可，但是仓库和商店中水果种类均不重复，这里采用Set      
store = {"apple": 1, "banana": 2, "watermelon": 3}	stock = set(["pear", "cherry", "apple", " orange"])
解析：
	2. 取水果数为仓库水果种类数的一半，用地板除获得次数，然后用choice进行随机选择	    	num = len(stock) // 2	choice = random.choice(list(stock))
解析：
	3. 取水果分为两种情况，原来有，那么数量追加，原来没有，则插入 

	4. 排序并输出
'''

import random
store = {"apple": 1, "banana": 2, "watermelon": 3}
stock = set(["pear", "cherry", "apple", " orange"])
num = len(stock) // 2
for i in range(num):
    choice = random.choice(list(stock))
    if choice in store:
        store[choice] += 1
    else:
        store[choice] = 1
    store = dict(sorted(store.items(), key=lambda x: x[1]))
print(store)



