# -*- coding: utf-8 -*-
# @Author        : hailiu
# @Time          : 2022/7/13 12:52
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import math

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#任务1：将图标装饰的标记点markers 、线型linestyle_str和常用颜色colors 组织为列表
markers = ['<','>','o','s','d',]
linestyle_str= ['-.','--','-']
colors = ['r','g','b']


font1 = {
    'family': 'Times New Roman',
    'weight': 'normal',
    'size': 12,
}

font2 = {
    'family': 'SimHei',
    'weight': 'normal',
    'size': 9,
}

#任务2：实现函数load_dataSet装载指定文件finename的实验结果数据
def load_dataSet(filename,dir = "../data/"):
    data =np.loadtxt(dir + filename,delimiter=",")
    return data

# 画子图1
def draw_fig01():
    plt.subplot(121)
    data = load_dataSet("researchResult.txt")
    #任务3：获取要显示的数据x,y1,y2
    x = data[:, 0]  # 读自变量
    y1 = data[:, 1]  # 读sin的值
    y2 = data[:, 2]  # 读cos的值
    #任务4：可视化第一组实验数据，并选择合适的标记、线型和标记。
    plt.plot(x,y1, label='sin', linewidth=1,linestyle = linestyle_str[0],color = colors[0],marker= markers[0])
    plt.plot(x, y2, label='cos', linewidth=1, linestyle=linestyle_str[1], color=colors[1],marker = markers[1])

    #任务5：装饰图形，设置x/y轴的标签、刻度和标题
    plt.yticks(np.arange(-1, 1.2, 0.2))
    plt.ylim(-1, 1)
    plt.ylabel("sin/cos")
    plt.xlabel('x')
    plt.legend()
    plt.title("第一组实验数据可视化")

def draw_fig02():
    ax2 = plt.subplot(122)
    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}  # 字体格式
    x_data = [0.01,0.03, 0.05,0.07,0.09,0.11 ]  # 参数取值
    x_tick = range(len(x_data))
    y_data = np.arange(0.40,0.61,0.05).tolist()
    y_tick = range(len(y_data))
    algorithm1 =  [0.47,0.44, 0.47,0.43,0.44,0.42 ]  # NDCG@20
    algorithm2 =  [0.46,0.48, 0.49,0.47,0.46,0.45 ]  #
    algorithm3 =  [0.56,0.55, 0.565,0.54,0.53,0.52 ] #
    plt.plot(x_data, algorithm1, marker=markers[0], ms=8, label='BERT_base+SJTF', linewidth=2,
             linestyle=linestyle_str[0], color="b")
    plt.plot(x_data, algorithm2, marker=markers[2], ms=8, label='BERT_PACRR+SJTF', linewidth=2,
             linestyle=linestyle_str[0], color="g")
    plt.plot(x_data, algorithm3, marker=markers[3], ms=8, label='CEDR-KNRM+SJTF', linewidth=2,
             linestyle=linestyle_str[0], color="r")
    plt.xticks(x_data, x_tick)
    plt.yticks(y_data, y_tick)
    # plt.ylim([0.4, 0.6])
    plt.ylabel('NDCG@20', font2)
    plt.xlabel('a', font2)
    ax2.set_xticklabels(x_data)
    ax2.set_yticklabels(y_data)
    plt.legend(prop=font2, loc="upper right")
    plt.grid(color='gray', linestyle='--', linewidth=0.2, which='major', axis='both')
    plt.title("第2组实验数据可视化")

    #任务9：装饰坐标轴图例与网络线
    pass


def draw():
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(wspace=0.3, hspace=0.3)  # 调整子图间距
    draw_fig01()
    draw_fig02()
    plt.savefig("../result/fig.jpg", bbox_inches='tight')
    plt.show()

    pass


#主驱动函数
if __name__ == '__main__':
    data = load_dataSet("researchResult.txt")
    print(data)
    print(data.shape)
    draw()


