import threading

from PyQt5.QtWidgets import QFileDialog

import os
from src.gui.baseClass import *
from src.components.start import *
from PyQt5 import QtCore, QtGui, QtWidgets


class GUIClass(QtWidgets.QMainWindow, Ui_BilibiliDanmakuWindow):

    def __init__(self):
        super(GUIClass, self).__init__()
        self.setupUi(self)

        initSaveDir = path.join(path.abspath(path.join(os.getcwd(), '../..')), r'result')
        initAVList = path.join(path.abspath(path.join(os.getcwd(), '../..')), r'res/avList.txt')
        self.lineEdit_saveDir.setText(initSaveDir)
        self.lineEdit_avList.setText(initAVList)
        self.pushButton_selectSaveDir.clicked.connect(self.button_save_openfile)
        self.pushButton_selectAvListDir.clicked.connect(self.button_avListFile)
        self.pushButton_avNumberStart.clicked.connect(self.button_startOne)
        self.pushButton_avListStart.clicked.connect(self.button_startList)

    def button_save_openfile(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        self.lineEdit_saveDir.setText(dir_path)
        self.label_show_status.setText("存储路径选择完成")

    def button_avListFile(self):
        file_name = QFileDialog.getOpenFileName(self, "选择文件", '', '文本文件(*.txt)')
        self.lineEdit_avList.setText(file_name[0])
        self.label_show_status.setText("av号列表文件选择完成")

    def button_startOne(self):
        avNumber = self.lineEdit_avNumber.text()
        savePath = self.lineEdit_saveDir.text()
        self.label_show_status.setText("正在爬取，请稍等")
        t = threading.Thread(target=startOne, args=(avNumber, savePath))
        t.start()

    def button_startList(self):
        listPath = self.lineEdit_avList.text()
        savePath = self.lineEdit_saveDir.text()
        self.label_show_status.setText("正在爬取，请稍等")
        t = threading.Thread(target=startList, args=(listPath, savePath))
        t.start()
