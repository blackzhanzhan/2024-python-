'''题目：最喜欢的电影
描述：录入你最喜欢的10部电影存入列表favoritefilms。
           想象各种应用场景，完成追加、插入、各种删除、输出等列表的基本操作
'''

favorite_films = []  # 创建一个空列表来存储电影

# 录入10部电影
for i in range(10):
    film = input(f"请输入你最喜欢的第{i+1}部电影: ")
    favorite_films.append(film)  # 将电影添加到列表中

# 输出电影列表
print("你最喜欢的电影有:")
for film in favorite_films:
    print(film)

# 示例操作：追加一部电影
new_film = input("请输入你想追加的电影: ")
favorite_films.append(new_film)

# 示例操作：插入一部电影
insert_film = input("请输入你想插入的电影: ")
position = int(input("请输入插入的位置(0-10): "))
favorite_films.insert(position, insert_film)

# 示例操作：删除一部电影
delete_film = input("请输入你想删除的电影: ")
if delete_film in favorite_films:
    favorite_films.remove(delete_film)
else:
    print("电影不在列表中。")

# 输出更新后的电影列表
print("更新后的电影列表:")
for film in favorite_films:
    print(film)