# -*- coding: utf-8 -*-
from os import path

from src.components.danmakuAnalyser import *
from src.components.getBilibiliDanmaku import *
from src.components.log import *

avListPath = r'res/avList.txt'


def startOne(avNumber, savePath):
    try:
        savePath = folderPathAvailable(savePath)
    except FileExistsError:
        return writeLog("存储路径无效")

    if not path.exists(savePath):
        os.makedirs(savePath)
    setLogFile(savePath)
    body(avNumber, savePath)
    return "爬取完成"


def startList(avNumberListPath, savePath):
    try:
        savePath = folderPathAvailable(savePath)
    except FileExistsError:
        return writeLog("存储路径无效")
    if not path.exists(savePath):
        os.makedirs(savePath)

    setLogFile(savePath)
    avNumList = open(avNumberListPath).read().split(',')

    for avNumber in avNumList:
        try:
            body(avNumber, savePath)
        except AttributeError:
            writeErrorLog("av号格式不正确：av%s" % avNumber)
            continue
        except TimeoutError:
            writeErrorLog("获取源代码超时：av%s" % avNumber)
            continue
        except RuntimeError:
            writeErrorLog("获取源码时连接异常：av%s" % avNumber)
            continue
        except IndexError:
            writeErrorLog("av%s 源码出错" % avNumber)
            continue

    return "爬取完成"


def body(avNumber, savePath):
    avNumber = avNumber.strip()
    try:
        html = getVideoHtmlByAid(avNumber)
    except AttributeError:
        raise AttributeError
    except TimeoutError:
        raise TimeoutError
    except RuntimeError:
        raise RuntimeError

    try:
        videoInfo = getCidAndAid(html)
    except IndexError:
        raise IndexError

    try:
        danmakuSource = getDanmakuHtml(videoInfo)
    except TimeoutError:
        raise TimeoutError
    except RuntimeError:
        raise RuntimeError

    try:
        danmakuList = getDanmaku(danmakuSource)
    except IndexError:
        raise IndexError

    title = titleAvailable(videoInfo)
    videoPath = path.join(savePath, '%s/' % title)
    excelFolderPath = videoPath
    photoFolderPath = path.join(videoPath, 'photo/')
    if not os.path.exists(photoFolderPath):
        os.makedirs(photoFolderPath)
    print(writeLog('文件夹创建成功 %s' % photoFolderPath))

    writeToMongoDB(videoInfo, danmakuList)
    writeDanmakuToExcel(videoInfo, danmakuList, excelFolderPath)
    countOfTime(videoInfo, danmakuList, photoFolderPath)
    colorAnalyse(videoInfo, danmakuList, photoFolderPath)
    countPerFeizhai(videoInfo, danmakuList, photoFolderPath)
    danmakuHeatMap(videoInfo, danmakuList, photoFolderPath)
    danmakuWordCloud(videoInfo, danmakuList, photoFolderPath)
