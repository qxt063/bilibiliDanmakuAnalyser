# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


def sortDanmakuByAppearTime(danmakuList):
    return sorted(danmakuList, key=lambda s: s['appearTime'])


def countOfTime(videoInfo, danmakuList):
    maxTime = int(danmakuList[len(danmakuList) - 1]['appearTime']) + 1
    step = int(maxTime / 10)
    appearTimeList = []
    for danmaku in danmakuList:
        appearTimeList.append(danmaku['appearTime'])
    bins = range(0, maxTime, step)

    global font
    plt.hist(appearTimeList, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('视频时间', fontproperties=font)
    plt.ylabel('弹幕数量', fontproperties=font)
    plt.title('%s\nav%s\n弹幕数与时间图' % (videoInfo['title'], videoInfo['aid']), fontproperties=font)
    # plt.legend()  # 显示标签
    plt.show()
