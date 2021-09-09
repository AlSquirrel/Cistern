# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cisterne.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(40, 300, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setProperty("value", 3.0)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(40, 340, 62, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setProperty("value", 1.0)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(150, 300, 62, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setProperty("value", 0.9)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(150, 340, 62, 22))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_4.setProperty("value", 0.15)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 31, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 31, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 300, 31, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 340, 31, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 330, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 330, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 320, 81, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_clicked)
        #self.pushButton.setStyleSheet("background-color: lambswool")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 300, 131, 21))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 300, 171, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(120, 20, 461, 241))
        self.label_7.setObjectName("label_7")
        pixmap = QtGui.QPixmap('Цистерна сф. торец.png')
        self.label_7.setPixmap(pixmap)
        self.label_7.show()
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle('Объём жидкости в цистерне')
        MainWindow.setWindowIcon(QtGui.QIcon('icon_cist.png'))
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Объём жидкости в цистерне со сферическими торцами"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:800; color:#550000;\">L, м</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:800; color:#550000;\">D, м</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:800; color:#550000;\">R, м</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:800; color:#550000;\">h, м</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "РАССЧИТАТЬ"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#550000;\">Объём жидкости, м<sup>3</sup></span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#550000;\">Объём полной цистерны, м<sup>3</sup></span></p></body></html>"))

    def on_clicked(self):
        L = self.doubleSpinBox.value()
        D = self.doubleSpinBox_2.value()
        R = self.doubleSpinBox_3.value()
        h = self.doubleSpinBox_4.value()
        V, Vp = calc(L,D,R,h)
        s = "%.6g"%V
        self.lineEdit.setText(s)
        s = "%.6g"%Vp
        self.lineEdit_2.setText(s)


def calc(L,D,R,h):
    if h != 0.5*D:
        if h < 0.5:
            alfa = 2*math.acos(1-2*h/D)
            V0 = L*D**2*(alfa-math.sin(alfa))/8
            V1 = ((R**2-D**2/4)**(1/2)*(D*h-h**2)**(1/2)/2+math.asin((D*h-h**2)**(1/2)/(R**2-(D/2-h)**2)**(1/2))*((D/2-h)**2/2-R**2/2))*(D/2-h)
            V2 = -(R**2-D**2/4)**(1/2)/2*(D**2*math.asin(2*(D*h-h**2)**(1/2)/D)/8+abs(D/2-h)*(D*h-h**2)**(1/2)/2)
            V3 = abs(D/2-h)*((R**2-D**2/4)**(1/2)*(D*h-h**2)**(1/2)/2-math.asin((D*h-h**2)**(1/2)/(R**2-(D/2-h)**2)**(1/2))*((D/2-h)**2/2-R**2/2))/2

            s = (D*h-h**2)**(1/2);
            F0 = -R**2*(math.asin((R**2-D**2/4)**(1/2)/R)-math.asin((R**2-(D/2-h)**2)**(1/2)/R))/2
            Fs3 = (math.asin((R**2-(D/2-h)**2-s**2/9)**(1/2)/(R**2-s**2/9)**(1/2))-math.asin((R**2-D**2/4)**(1/2)/(R**2-s**2/9)**(1/2)))*(R**2/2-s**2/18)
            Fs23 = (math.asin((R**2-(D/2-h)**2-9*s**2/16)**(1/2)/(R**2-9*s**2/16)**(1/2))-math.asin((R**2-D**2/4)**(1/2)/(R**2-9*s**2/16)**(1/2)))*(R**2/2-9*s**2/32)
            p1 = (R*D/h)**(1/2)
            k1 = -(125*F0*s**4/864-21*Fs3*s**4/64+8*Fs23*s**4/27)/(65*s**p1*s**4/576+21*s**4*(s/3)**p1/64-8*s**4*(3*s/4)**p1/27)
            k2en = 37*F0*s**3*(s/3)**p1/64-26*F0*s**3*(3*s/4)**p1/27+Fs3*s**3*(3/4*s)**p1-Fs23*s**3*(s/3)**p1+665*F0*s**p1*s**3/1728-27*Fs3*s**p1*s**3/64+Fs23*s**p1*s**3/27
            k2den = 65*s**p1*s**4/576+21*s**4*(s/3)**p1/64-8*s**4*(3*s/4)**p1/27
            k2 = -k2en/k2den

            k3en = 5*F0*s*s**p1/12-3*Fs3*s*s**p1/4+Fs23*s*s**p1/3+F0*s*(s/3)**p1/4-2*F0*s*(3*s/4)**p1/3+Fs3*s*(3*s/4)**p1-Fs23*s*(s/3)**p1
            k3den = k2den
            k3 = k3en/k3den
            V4 = F0*s+0.5*k2*s**2+0.25*k3*s**4+k1*s**(p1+1)/(p1+1)
            V = V0 + 4*(V1+V2+V3+V4)

            hs = R-(R**2-D**2/4)**(1/2)
            Vp = math.pi *L*D**2/4+2*math.pi*hs**2*(R-hs/3)
        elif h < D:
            h = D-h
            alfa = 2*math.acos(1-2*h/D)
            V0 = L*D**2*(alfa-math.sin(alfa))/8
            V1 = ((R**2-D**2/4)**(1/2)*(D*h-h**2)**(1/2)/2+math.asin((D*h-h**2)**(1/2)/(R**2-(D/2-h)**2)**(1/2))*((D/2-h)**2/2-R**2/2))*(D/2-h)
            V2 = -(R**2-D**2/4)**(1/2)/2*(D**2*math.asin(2*(D*h-h**2)**(1/2)/D)/8+abs(D/2-h)*(D*h-h**2)**(1/2)/2)
            V3 = abs(D/2-h)*((R**2-D**2/4)**(1/2)*(D*h-h**2)**(1/2)/2-math.asin((D*h-h**2)**(1/2)/(R**2-(D/2-h)**2)**(1/2))*((D/2-h)**2/2-R**2/2))/2

            s = (D*h-h**2)**(1/2);
            F0 = -R**2*(math.asin((R**2-D**2/4)**(1/2)/R)-math.asin((R**2-(D/2-h)**2)**(1/2)/R))/2
            Fs3 = (math.asin((R**2-(D/2-h)**2-s**2/9)**(1/2)/(R**2-s**2/9)**(1/2))-math.asin((R**2-D**2/4)**(1/2)/(R**2-s**2/9)**(1/2)))*(R**2/2-s**2/18)
            Fs23 = (math.asin((R**2-(D/2-h)**2-9*s**2/16)**(1/2)/(R**2-9*s**2/16)**(1/2))-math.asin((R**2-D**2/4)**(1/2)/(R**2-9*s**2/16)**(1/2)))*(R**2/2-9*s**2/32)
            p1 = (R*D/h)**(1/2)
            k1 = -(125*F0*s**4/864-21*Fs3*s**4/64+8*Fs23*s**4/27)/(65*s**p1*s**4/576+21*s**4*(s/3)**p1/64-8*s**4*(3*s/4)**p1/27)
            k2en = 37*F0*s**3*(s/3)**p1/64-26*F0*s**3*(3*s/4)**p1/27+Fs3*s**3*(3/4*s)**p1-Fs23*s**3*(s/3)**p1+665*F0*s**p1*s**3/1728-27*Fs3*s**p1*s**3/64+Fs23*s**p1*s**3/27
            k2den = 65*s**p1*s**4/576+21*s**4*(s/3)**p1/64-8*s**4*(3*s/4)**p1/27
            k2 = -k2en/k2den

            k3en = 5*F0*s*s**p1/12-3*Fs3*s*s**p1/4+Fs23*s*s**p1/3+F0*s*(s/3)**p1/4-2*F0*s*(3*s/4)**p1/3+Fs3*s*(3*s/4)**p1-Fs23*s*(s/3)**p1
            k3den = k2den
            k3 = k3en/k3den
            V4 = F0*s+0.5*k2*s**2+0.25*k3*s**4+k1*s**(p1+1)/(p1+1)
            V = V0 + 4*(V1+V2+V3+V4)

            hs = R-(R**2-D**2/4)**(1/2)
            Vp = math.pi *L*D**2/4+2*math.pi*hs**2*(R-hs/3)
            V = Vp - V
        else:
            hs = R-(R**2-D**2/4)**(1/2)
            Vp = math.pi *L*D**2/4+2*math.pi*hs**2*(R-hs/3)
            V = Vp
    else :
        hs = R-(R**2-D**2/4)**(1/2)
        V = 0.5*(math.pi *L*D**2/4+2*math.pi*hs**2*(R-hs/3))
        Vp = math.pi *L*D**2/4+2*math.pi*hs**2*(R-hs/3)
    return V,Vp

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

