# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog 
from bitstring import BitArray
from grain import Grain
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 771, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 400, 721, 23))
        self.progressBar.setObjectName("progressBar")
        self.pushButtonSrcFile = QtWidgets.QPushButton(self.tab)
        self.pushButtonSrcFile.setGeometry(QtCore.QRect(670, 30, 88, 29))
        self.pushButtonSrcFile.setObjectName("pushButtonSrcFile")
        self.pushButtonDstFile = QtWidgets.QPushButton(self.tab)
        self.pushButtonDstFile.setGeometry(QtCore.QRect(670, 90, 88, 29))
        self.pushButtonDstFile.setObjectName("pushButtonDstFile")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 140, 751, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.keyLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.keyLabel_2.setObjectName("keyLabel_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.keyLabel_2)
        self.lineEditKey = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEditKey.setObjectName("lineEditKey")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditKey)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.iVLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.iVLabel_2.setObjectName("iVLabel_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.iVLabel_2)
        self.lineEditIV = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEditIV.setObjectName("lineEditIV")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditIV)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 17))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 310, 231, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonEncrypt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonEncrypt.setObjectName("pushButtonEncrypt")
        self.horizontalLayout_2.addWidget(self.pushButtonEncrypt)
        self.pushButtonDecrypt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonDecrypt.setObjectName("pushButtonDecrypt")
        self.horizontalLayout_2.addWidget(self.pushButtonDecrypt)
        self.lineEditDstFile = QtWidgets.QLineEdit(self.tab)
        self.lineEditDstFile.setGeometry(QtCore.QRect(10, 90, 651, 29))
        self.lineEditDstFile.setObjectName("lineEditDstFile")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 56, 17))
        self.label.setObjectName("label")
        self.lineEditSrcFile = QtWidgets.QLineEdit(self.tab)
        self.lineEditSrcFile.setGeometry(QtCore.QRect(10, 30, 651, 29))
        self.lineEditSrcFile.setObjectName("lineEditSrcFile")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 751, 421))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelImgSrc = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelImgSrc.setObjectName("labelImgSrc")
        self.horizontalLayout_3.addWidget(self.labelImgSrc)
        self.labelImgDst = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelImgDst.setScaledContents(False)
        self.labelImgDst.setObjectName("labelImgDst")
        self.horizontalLayout_3.addWidget(self.labelImgDst)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(80, 430, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(550, 430, 101, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Edit Code
        self.pushButtonSrcFile.clicked.connect(self.selectSrcFile)
        self.pushButtonDstFile.clicked.connect(self.selectDstFile)
        self.pushButtonEncrypt.clicked.connect(self.encrypt)
        self.pushButtonDecrypt.clicked.connect(self.decrypt)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSrcFile.setText(_translate("MainWindow", "Browse"))
        self.pushButtonDstFile.setText(_translate("MainWindow", "Browse"))
        self.keyLabel_2.setText(_translate("MainWindow", "Key"))
        self.label_4.setText(_translate("MainWindow", "E.g. : 00000000000000000000"))
        self.iVLabel_2.setText(_translate("MainWindow", "IV"))
        self.label_6.setText(_translate("MainWindow", "E.g. : 0000000000000000"))
        self.label_2.setText(_translate("MainWindow", "Destination"))
        self.pushButtonEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.pushButtonDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label.setText(_translate("MainWindow", "Source"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Encrypt / Decrypt"))
        self.labelImgSrc.setText(_translate("MainWindow", "No File Selected"))
        self.labelImgDst.setText(_translate("MainWindow", "No File Selected"))
        self.label_9.setText(_translate("MainWindow", "Source File"))
        self.label_10.setText(_translate("MainWindow", "Destination File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Preview"))

    def selectSrcFile(self):
        file = QFileDialog.getOpenFileName(None, 'Select File', '', "Image files (*.jpg, *.png)")[0]
        self.lineEditSrcFile.setText(file)
        pixmap = QtGui.QPixmap(file)
        self.labelImgSrc.setPixmap(pixmap)
        #self.labelImgDst.setPixmap(pixmap)

        #a = QFileDialog.getOpenFileName()
        
    def selectDstFile(self):
        self.lineEditDstFile.setText(QFileDialog.getSaveFileName(None, 'Save File', '', "Image files (*.jpg, *.png)")[0])

    def encrypt(self):
        key = self.lineEditKey.text()
        iv = self.lineEditIV.text()
        file = self.lineEditSrcFile.text()
        outfile = self.lineEditDstFile.text()
        self.progressBar.setValue(0)

        grain = Grain(key, iv)

        # Images proccesing
        images = cv2.imread(file, cv2.IMREAD_COLOR)
        row = images.shape[0]
        col = images.shape[1]

        self.progressBar.setMaximum((row-1)*(col-1))
        for i in range(row):
            for j in range(col):
                #print "Proccessing pixel [{}][{}]".format(i, j)
                self.progressBar.setValue(self.progressBar.value() + 1)
                images[i][j] = grain.encrypt(images[i][j])

        cv2.imwrite(outfile, images)        
        
        pixmap = QtGui.QPixmap(outfile)
        self.labelImgDst.setPixmap(pixmap)

    def decrypt(self):
        key = self.lineEditKey.text()
        iv = self.lineEditIV.text()
        file = self.lineEditSrcFile.text()
        outfile = self.lineEditDstFile.text()
        self.progressBar.setValue(0)

        grain = Grain(key, iv)

        # Images proccesing
        images = cv2.imread(file, cv2.IMREAD_COLOR)
        row = images.shape[0]
        col = images.shape[1]

        self.progressBar.setMaximum((row-1)*(col-1))
        for i in range(row):
            for j in range(col):
                #print "Proccessing pixel [{}][{}]".format(i, j)
                self.progressBar.setValue(self.progressBar.value() + 1)
                images[i][j] = grain.decrypt(images[i][j])

        cv2.imwrite(outfile, images)        
        
        pixmap = QtGui.QPixmap(outfile)
        self.labelImgDst.setPixmap(pixmap)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myfirstgui = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(myfirstgui)
    myfirstgui.show()
    sys.exit(app.exec_())