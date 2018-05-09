# -*- coding: utf-8 -*-
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates
import numpy as np

from danmakuDetailsDealing import *

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


# 弹幕数与视频时间关系
def countOfTime(videoInfo, danmakuList, photoFolderPath):
    appearTimeList = getValueListByKey(danmakuList, 'appearTime')
    plt.figure(figsize=(12, 9))
    plt.hist(appearTimeList, bins=20, histtype='bar', rwidth=0.8)
    plt.xlabel('视频时间', fontproperties=font)
    plt.ylabel('弹幕数量', fontproperties=font)
    plt.title('%s\nav%s\n弹幕数与时间图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)

    # TODO：检查path以及title
    filePath = photoFolderPath + '%s_弹幕数与时间图.png' % videoInfo['title']
    plt.savefig(filePath)
    print('弹幕数与时间图 已生成并存储')
    plt.show()


# 弹幕颜色
def colorAnalyse(videoInfo, danmakuList, photoFolderPath):
    colorList = []
    for danmaku in danmakuList:
        colorList.append(danmaku['color'])
    colorSet = set(colorList)
    colorCountDictList = []
    for item in colorSet:
        colorCountDict = {'color': item,
                          'count': colorList.count(item)}
        colorCountDictList.append(colorCountDict)
    colorCountDictList = sortDictByKey(colorCountDictList, 'count', True)
    colorSet.clear()
    colorName = []
    colorSet = []
    for item in colorCountDictList:
        colorSet.append(item['color'])
        if item['count'] / len(danmakuList) <= 0.005:
            colorName.append('')
        else:
            colorName.append(item['color'])

    colorCount = getValueListByKey(colorCountDictList, 'count')
    # ,autopct='%3.1f %%'
    plt.figure(figsize=(19.2, 16.8))
    plt.pie(colorCount, labels=colorName, colors=colorSet, shadow=True, startangle=90)
    plt.title('%s\nav%s\n弹幕颜色饼图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font, fontsize='xx-large')
    plt.tight_layout()
    plt.legend()

    # TODO：检查path以及title
    filePath = photoFolderPath + '%s_弹幕颜色饼图.png' % videoInfo['title']
    plt.savefig(filePath)
    print('弹幕颜色饼状图 已生成并存储')
    plt.show()


# 用户发送弹幕数饼图
# 这是一个人数图，不是弹幕数图
# 容易弄混
def countPerFeizhai(videoInfo, danmakuList, photoFolderPath):
    feizhaiList = getValueListByKey(danmakuList, 'feizhaiId')
    feizhaiSet = set(feizhaiList)
    countList = []
    for item in feizhaiSet:
        countList.append(feizhaiList.count(item))
    feizhaiCountDictList = []

    danmakuCountSet = set(countList)
    for item in danmakuCountSet:
        feizhaiCountDictList.append({'sendDanmakuCount': item, 'feizhaiCount': countList.count(item)})
    feizhaiCountDictList = sortDictByKey(feizhaiCountDictList, 'sendDanmakuCount')

    feizhaiCountList = []
    danmakuCountList = []
    for item in feizhaiCountDictList:
        feizhaiCountList.append(item['feizhaiCount'])
        if item['feizhaiCount'] / len(danmakuList) <= 0.002:
            danmakuCountList.append('')
        else:
            danmakuCountList.append(item['sendDanmakuCount'])

    plt.figure(figsize=(12, 9))
    plt.pie(feizhaiCountList, labels=danmakuCountList, shadow=True, startangle=90)
    plt.title('%s\nav%s\n用户发送弹幕数饼图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    plt.tight_layout()

    # TODO：检查path以及title
    filePath = photoFolderPath + '%s_用户发送弹幕数饼图.png' % videoInfo['title']
    plt.savefig(filePath)
    print('用户发送弹幕数饼图 已生成并存储')
    plt.show()


def danmakuHeatMap(videoInfo, danmakuList, photoFolderPath):
    originalTimestampList = getValueListByKey(danmakuList, 'sentTimestamp')
    timestampList = []
    for item in originalTimestampList:
        timestampList.append(convertDateTimeToTimestamp(convertTimestampToDateTime(item, "%m/%d/%Y"), "%m/%d/%Y"))
    timestampSet = sorted(set(timestampList))
    dateSet = []
    for item in timestampSet:
        dateSet.append(convertTimestampToDateTime(item, '%m/%d/%Y'))
    danmakuCount = []
    isFirst = True
    for item in timestampSet:
        if isFirst:
            danmakuCount.append(timestampList.count(item))
            isFirst = False
        else:
            danmakuCount.append(danmakuCount[-1] + timestampList.count(item))

    # 横坐标信息
    xs = [datetime.strptime(d, '%m/%d/%Y').date() for d in dateSet]
    # 配置横轴坐标
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    # 显示图例
    plt.gcf().autofmt_xdate()  # 自动旋转日期标记
    plt.figure(figsize=(12, 9))
    plt.plot(xs, danmakuCount)
    plt.title('%s\nav%s\n视频弹幕数累计折线图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    plt.tight_layout()

    # TODO：检查path以及title
    filePath = photoFolderPath + '%s_视频弹幕数累计折线图.png' % videoInfo['title']
    plt.savefig(filePath)
    print('视频弹幕数累计折线图 已生成并存储')
    plt.show()
