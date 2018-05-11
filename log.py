import os
import time

logFile = os.path.join(os.path.dirname(__file__), 'log.txt')
errorLogFile = os.path.join(os.path.dirname(__file__), 'errorLog.txt')


def setLogFile(rootPath):
    global logFile
    logFile = os.path.join(rootPath, 'log.txt')
    global errorLogFile
    errorLogFile = os.path.join(rootPath, 'errorLog.txt')


def writeLog(information, videoInfo=None):
    now = str(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())))
    if videoInfo is None:
        logInfo = '事件：%s\n时间：%s\n\n' % (information, now)
    else:
        logInfo = 'av%s\n事件：%s\n时间：%s\n\n' % (videoInfo['aid'] + videoInfo['title'], information, now)
    with open(logFile, 'a')as log:
        log.write(logInfo)
    return logInfo


def writeErrorLog(information, videoInfo=None):
    now = str(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())))
    if videoInfo is None:
        errorLogInfo = '事件：%s\n时间：%s\n\n' % (information, now)
    else:
        errorLogInfo = 'av%s\n事件：%s\n时间：%s\n\n' % (videoInfo['aid'] + videoInfo['title'], information, now)
    with open(errorLogFile, 'a')as errorLog:
        errorLog.write(errorLogInfo)
    return errorLogInfo
