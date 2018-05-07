# -*- coding: utf-8 -*-

from getBilibiliDanmaku import *

if __name__ == '__main__':
    videoInfo = getCidAndAid(getVideoHtmlByAid(input("输入av号：")))
    danmakuSource = getDanmakuHtml(videoInfo)
    danmakuList = getDanmaku(danmakuSource)
    Path = 'K:/test/danmaku/弹幕信息_%s.xls' % videoInfo['title']
    writeDanmakuToExcel(videoInfo, danmakuList, Path)
    # for danmaku in danmakuList:
    #     printDanmaku(danmaku)
    #     print()
