"""
程序功能：商品推广方案数据可视化
"""
import csv

import pandas as pd
from pyecharts.charts import Funnel, Grid
import pyecharts.options as opts
import os

onlineData = "../data/onlineAdvertizeData.csv"
offlineData = "../data/offlineAdvertizeData.csv"


def processData(datafile):
    #step1:读入推广数据文件
   with open(onlineData, "r", encoding="utf-8") as f:
       reader = csv.DictReader(f)
       for row in reader:
           

    #step2: 对数据按列求和
    pass
    return x_data, y_data


def drawFunnel_online(x_data, y_data):
    data = [[x_data[i], y_data[i]] for i in range(len(x_data))]
    c = (
        Funnel(init_opts=opts.InitOpts(width="1000px", height="500px"))
            .add(
            series_name="线上促销",
            data_pair=data,
            gap=2,
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a}</br>占比:{c}%"),
            label_opts=opts.LabelOpts(position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#ccc", border_width=1),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="线上促销", pos_left='10%'))
            .render("advitise_online.html")
    )

    os.system("advitise_online.html")


def drawFunnel_offline(u_data, v_data):
    pass



def drawFunnel_data(x, y):
    newX = []
    newY = []
    for i in range(len(x)):
        newX.append(x[i] + '：' + str(y[i]))
        newY.append(round((y[i] / y[0]) * 100, 2))
    return newX, newY


if __name__ == '__main__':
    onlineData = "../data/onlineAdvertizeData.csv"
    onlineX, onlineY = processData(onlineData)
    onlineY = [int(x) for x in onlineY]
    onlineX, onlineY = drawFunnel_data(onlineX, onlineY)

    offlineData = "../data/offlineAdvertizeData.csv"
    offlineX, offlineY = processData(offlineData)
    offlineY = [int(x) for x in offlineY]
    offlineX, offlineY = drawFunnel_data(offlineX, offlineY)

    drawFunnel_online(onlineX, onlineY)  # 线上促销函数
    drawFunnel_offline(offlineX,offlineY) #线下促销函数
