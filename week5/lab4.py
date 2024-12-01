'''
题目：打怪物游戏
描述：假设有一个玩家，一个怪物，分别对应一连串数字，第一个数字为初始血量，从第二个开始到最后为其可能的攻击力，可选择的攻击力数量大于等于2， 每回合都有可能是玩家或者怪物攻击（随机选择），攻击力为玩家/怪物本身的攻击力中的随机一个，互相攻击直到其中一方血量小于等于0，输出胜利者及其剩余血量
解析：
	1. 假设一个玩家，一个怪物，分别对应一串数字，典型的Key：Value，用字典，Value为list
		role = {"player": [5, 2, 3, 4], "monster": [10, 1, 2]}
解析：
	2. 每回合都选择一个角色随机攻击，攻击力随机选择，用random
		n = random.randint(1, 2)  choice = random.randint(1, 3)
		atk = role["player"][choice]   role["monster"][0] -= atk
    解析：
	3. 直到一方血量小于等于0，外层套一个while循环     	
	              while role["player"][0] > 0 and role["monster"][0] > 0:
    解析：
	3. 判断胜利者	
	              if : xxx   else xxx                
'''
import random

# 定义玩家和怪物的属性
role = {"player": [5, 2, 3, 4], "monster": [10, 1, 2]}

# 游戏主循环
while role["player"][0] > 0 and role["monster"][0] > 0:
    # 随机选择攻击者
    attacker = random.choice(["player", "monster"])
    defender = "monster" if attacker == "player" else "player"
    
    # 随机选择攻击力
    attack_power = random.choice(role[attacker][1:])
    
    # 执行攻击
    role[defender][0] -= attack_power
    
    print(f"{attacker.capitalize()} 攻击了 {defender}，造成了 {attack_power} 点伤害")
    print(f"玩家剩余血量: {role['player'][0]}, 怪物剩余血量: {role['monster'][0]}")
    print("--------------------")

# 判断胜利者
if role["player"][0] > 0:
    winner = "玩家"
    remaining_health = role["player"][0]
else:
    winner = "怪物"
    remaining_health = role["monster"][0]

print(f"游戏结束！{winner}获胜，剩余血量为{remaining_health}")
             
