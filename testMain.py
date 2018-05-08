# -*- coding: utf-8 -*-
import testData
from danmakuAnalyser import *
from getBilibiliDanmaku import *

if __name__ == '__main__':
    videoInfo = getCidAndAid(getVideoHtmlByAid(input("输入av号：")))
    print(videoInfo)
    danmakuSource = getDanmakuHtml(videoInfo)

    # videoInfo = getCidAndAid(testData.htmlSource)
    # danmakuSource = testData.danmakuSource
    danmakuList = getDanmaku(danmakuSource)
    danmakuList = sortDanmakuByAppearTime(danmakuList)
    countOfTime(videoInfo, danmakuList)
    # for danmaku in danmakuList:
    #     printDanmaku(danmaku)
    #     print()

    folderPath = 'K:/test/danmaku/'
    writeDanmakuToExcel(videoInfo, danmakuList, folderPath)
