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
markers = []
linestyle_str= []
colors = []


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
   pass

# 画子图1
def draw_fig01():
    plt.subplot(121)
    data = load_dataSet("researchResult.txt")
    #任务3：获取要显示的数据x,y1,y2
    pass
    #任务4：可视化第一组实验数据，并选择合适的标记、线型和标记。
    pass
    #任务5：装饰图形，设置x/y轴的标签、刻度和标题
    pass
    plt.legend(loc=7, prop=font2, bbox_to_anchor=(0.96, 0.90), ncol=1, borderaxespad=0.)


def draw_fig02():
    ax2 = plt.subplot(122)
    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}  # 字体格式
    x_data = [0.01,0.03, 0.05,0.07,0.09,0.11 ]  # 参数取值
    y_data = np.arange(0.40,0.61,0.05).tolist()
    algorithm1 =  [0.47,0.44, 0.47,0.43,0.44,0.42 ]  # NDCG@20
    algorithm2 =  [0.46,0.48, 0.49,0.47,0.46,0.45 ]  #
    algorithm3 =  [0.56,0.55, 0.565,0.54,0.53,0.52 ] #
    #任务6：实现带标记的子图
    pass

    #任务7：装饰图形坐标轴刻度 xtick，ytick与刻度标签xticklabels,yticklabels,设置坐标轴的范围
    pass

    # 任务8：装饰坐标轴标签
    pass

    #任务9：装饰坐标轴图例与网络线
    pass


def draw():
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(wspace=0.3, hspace=0.3)  # 调整子图间距
    draw_fig01()
    draw_fig02()
    plt.show()
    plt.savefig("./fig.svg", bbox_inches='tight')
    pass


#主驱动函数
if __name__ == '__main__':
    draw()


