# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

from danmakuDetailsDealing import *

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


# 弹幕数与视频时间关系
def countOfTime(videoInfo, danmakuList):
    appearTimeList = getValueListByKey(danmakuList, 'appearTime')
    plt.hist(appearTimeList, bins=20, histtype='bar', rwidth=0.8)
    plt.xlabel('视频时间', fontproperties=font)
    plt.ylabel('弹幕数量', fontproperties=font)
    plt.title('%s\nav%s\n弹幕数与时间图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    plt.show()


# 弹幕颜色
def colorAnalyse(videoInfo, danmakuList):
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
        if item['count'] / len(danmakuList) <= 0.015:
            colorName.append('')
        else:
            colorName.append(item['color'])

    colorCount = getValueListByKey(colorCountDictList, 'count')
    # ,autopct='%3.1f %%'
    plt.pie(colorCount, labels=colorName, colors=colorSet, shadow=True, startangle=90)
    plt.title('%s\nav%s\n弹幕颜色饼图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    plt.tight_layout()
    plt.show()


# 用户发送弹幕数饼图
# 这是一个人数图，不是弹幕数图
# 容易弄混
def countPerFeizhai(videoInfo, danmakuList):
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
    # feizhaiCountList = getValueListByKey(feizhaiCountDictList, 'feizhaiCount')
    # danmakuCountList = getValueListByKey(feizhaiCountDictList, 'danmakuCount')
    feizhaiCountList = []
    danmakuCountList = []
    for item in feizhaiCountDictList:
        feizhaiCountList.append(item['feizhaiCount'])
        if item['feizhaiCount'] / len(danmakuList) <= 0.002:
            danmakuCountList.append('')
        else:
            danmakuCountList.append(item['sendDanmakuCount'])

    plt.pie(feizhaiCountList, labels=danmakuCountList, shadow=True, startangle=90)
    plt.title('%s\nav%s\n用户发送弹幕数饼图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    plt.tight_layout()
    plt.show()
