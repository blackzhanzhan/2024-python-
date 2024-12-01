'''
题目：编写代码选择播放音乐
描述：两类音乐分别存储在文件夹happy和sad中
           用户输入心情（0代表开心，1代表伤心，8代表不想听了），系统根据随机选取音乐播放100秒

解析：
	1. 分别获取文件名存储在列表中（筛选音乐文件可用列表推导式）        os.listdir(‘.\路径')
    2. 随机选取歌曲		random.choice(happy_list)
    3. 播放歌曲（当前歌曲听完后重新选取）
                                         pygame.mixer.init()
                                         pygame.mixer.music.load(‘音乐文件名')
                                         pygame.mixer.music.play()
                                         time.sleep(100)		
'''

import pygame
import os
import random
import time
happy_list = os.listdir('./music/happy')
sad_list = os.listdir('./music/sad')

if __name__ == '__main__':
    mood = input("请输入心情,0代表开心，1代表伤心，8代表不想听了: ") 
    if mood == '0':
        music = random.choice(happy_list)
        full_path_happy = os.path.join('./music/happy', music)
        pygame.mixer.init()
        pygame.mixer.music.load(full_path_happy)
        pygame.mixer.music.play()
        time.sleep(100)
    elif mood == '1':
        music = random.choice(sad_list)
        full_path_sad = os.path.join('./music/sad', music)
        pygame.mixer.init()
        pygame.mixer.music.load(full_path_sad)
        pygame.mixer.music.play()
        time.sleep(100)
    elif mood == '8':
        exit()