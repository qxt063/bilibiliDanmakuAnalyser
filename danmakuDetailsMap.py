import time


def getDanmakuSentTimestamp(timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestamp)))


def getDanmakuType(typeNumber):
    typeDict = {1: '滚动弹幕', 2: '滚动弹幕', 3: '滚动弹幕', 4: '底端弹幕',
                5: '顶端弹幕', 6: '逆向弹幕', 7: '精准弹幕', 8: '高级弹幕'}
    return typeDict.get(int(typeNumber))


def getDanmakuFontSize(fontSizeNumber):
    fontSizeDict = {12: '非常小', 16: '很小', 18: '小',
                    25: '中', 36: '大', 45: '很大', 64: '特别大'}
    return fontSizeDict.get(int(fontSizeNumber))


def getDanmakuPool(poolNumber):
    poolDict = {0: '普通池', 1: '字幕池', 2: '特殊池'}
    return poolDict.get(int(poolNumber))
