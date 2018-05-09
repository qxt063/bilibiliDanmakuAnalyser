# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

from danmakuDetailsDealing import *

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


def countOfTime(videoInfo, danmakuList):
    maxTime = int(danmakuList[len(danmakuList) - 1]['appearTime']) + 1
    step = int(maxTime / 10)
    appearTimeList = getValuesByKey(danmakuList, 'appearTime')
    bins = range(0, maxTime, step)

    plt.hist(appearTimeList, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('视频时间', fontproperties=font)
    plt.ylabel('弹幕数量', fontproperties=font)
    plt.title('%s\nav%s\n弹幕数与时间图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    plt.show()


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
    colorSet = []
    colorName = []
    for item in colorCountDictList:
        colorSet.append(item['color'])
        if item['count'] / len(danmakuList) <= 0.015:
            colorName.append('')
        else:
            colorName.append(item['color'])

    colorCount = getValuesByKey(colorCountDictList, 'count')
    # ,autopct='%3.1f %%'
    plt.pie(colorCount, labels=colorName, colors=colorSet, shadow=True, startangle=90)
    plt.title('%s\nav%s\n弹幕颜色饼图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    plt.tight_layout()
    plt.show()
