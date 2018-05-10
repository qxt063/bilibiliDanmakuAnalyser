# -*- coding: utf-8 -*-
import testData
from danmakuAnalyser import *
from getBilibiliDanmaku import *

if __name__ == '__main__':
    videoInfo = getCidAndAid(getVideoHtmlByAid(input("输入av号：")))
    print(videoInfo)
    danmakuSource = getDanmakuHtml(videoInfo)

    # videoInfo = testData.videoInfo  # test
    # danmakuSource = testData.danmakuSource  # test

    excelFolderPath = 'K:/test/danmaku/'
    photoFolderPath = excelFolderPath + 'photo/'
    danmakuList = getDanmaku(danmakuSource)
    countOfTime(videoInfo, danmakuList, photoFolderPath)
    colorAnalyse(videoInfo, danmakuList, photoFolderPath)
    countPerFeizhai(videoInfo, danmakuList, photoFolderPath)
    danmakuHeatMap(videoInfo, danmakuList, photoFolderPath)
    danmakuWordCloud(videoInfo, danmakuList, photoFolderPath)
    # print(convertTimestamp(danmakuList[0]['sentTimestamp'], "%m/%d/%Y"))  # test

    # writeDanmakuToExcel(videoInfo, danmakuList, excelFolderPath)

    # for danmaku in danmakuList:
    #     printDanmaku(danmaku)
    #     print()
