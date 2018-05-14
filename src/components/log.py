import os
import time

from pymongo import *

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
        logDB = {'目标': None, '事件': information, '时间': now}
    else:
        logInfo = 'av%s\n事件：%s\n时间：%s\n\n' % (videoInfo['aid'] + videoInfo['title'], information, now)
        logDB = {'目标': 'av%s %s' % (videoInfo['aid'], videoInfo['title']), '事件': information, '时间': now}
    with open(logFile, 'a')as log:
        log.write(logInfo)

    conn = MongoClient('localhost', 27017)
    db = conn.logDB
    dbSet = db['log']
    dbSet.insert_one(logDB)
    return logInfo


def writeErrorLog(information, videoInfo=None):
    now = str(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())))
    if videoInfo is None:
        errorLogInfo = '事件：%s\n时间：%s\n\n' % (information, now)
        errorLogDB = {'目标': None, '事件': information, '时间': now}
    else:
        errorLogInfo = 'av%s\n事件：%s\n时间：%s\n\n' % (videoInfo['aid'] + videoInfo['title'], information, now)
        errorLogDB = {'目标': 'av%s %s' % (videoInfo['aid'], videoInfo['title']), '事件': information, '时间': now}
    with open(errorLogFile, 'a')as errorLog:
        errorLog.write(errorLogInfo)
    conn = MongoClient('localhost', 27017)
    db = conn.logDB
    dbSet = db['errorLog']
    dbSet.insert_one(errorLogDB)
    return errorLogInfo
