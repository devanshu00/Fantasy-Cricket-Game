from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn = sqlite3.connect('final.db')
import math


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 519)
        #starting line label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        #H LAYOUT FOR COMBO BOX
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 601, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #COMBO BOX FOR SELECTING TEAM
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        sql1='select name from teams'
        cursor=conn.execute(sql1)
        teams=[]
        for row in cursor:
            print(row)
            self.comboBox_2.addItem(row[0])
        conn.close
        #COMBO BOX FOR SELECTING MATCH
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Match1")
        self.comboBox.addItem("Match2")
        self.comboBox.addItem("Match3")
        self.comboBox.addItem("Match4")
        self.comboBox.addItem("Match5")
        self.horizontalLayout.addWidget(self.comboBox)
        #LINE FOR DIVIDING
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 100, 630, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        #H LAYOUT FOR PLAYERS AND POINTS
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 110, 601, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #LABEL FOR PLAYERS
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        #LABEL FOR POINTS
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        #LABEL FOR POINT DISPLAY
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        #H LAYOUT FOR LISTS
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 150, 601, 301))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #LIST FOR PLAYERS
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        #LIST FOR POINTS
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        #BUTTON FOR SCORE CALCULATION
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 470, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
       
    def calculate(self):
        team=self.comboBox_2.currentText()
        self.listWidget.clear()
        self.listWidget_2.clear()
        data="select players,value from teams where name='"+team+"'"
        cur=conn.execute(data)
        row=cur.fetchone()
        print(row)  #last element after "," is null
        selected=row[0].split(',')        
        self.listWidget_2.addItems(selected)
        teamtotal=0        
        match=self.comboBox.currentText()
        print(selected)  #there is an empty string in the end
        #Reduced one iteration here
        for i in range(self.listWidget_2.count() - 1):
            totalscore=0
            batscore=0
            bowlscore=0
            fieldscore=0
            nm=self.listWidget_2.item(i).text()
            print("nm  ",nm)
            curs=conn.execute("select * from "+match+" where player='"+nm+"'")
            row=curs.fetchone()
            print(row)
            batscore=row[1]/2
            if batscore>=50:
                batscore=batscore+5
            if batscore>=100:
                batscore=batscore+10
            if row[1]>0:
                sr=row[1]/row[2]
                if sr>=80 and sr<100:
                    batscore=batscore+2
                if sr>=100:
                    batscore=batscore+4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
            
            bowlscore=row[8]*10
            if row[8]>=3:
                bowlscore=bowlscore+5
            if row[8]>=5:
                bowlscore=bowlscore=bowlscore+10
            if row[7]>0:
                er=6*row[7]/row[5]                
                if er<=2:
                    bowlscore=bowlscore+10
                if er>2 and er<=3.5:
                    bowlscore=bowlscore+7
                if er>3.5 and er<=4.5:
                    bowlscore=bowlscore+4

            fieldscore=(row[9]+row[10]+row[11])*10            

            totalscore=batscore+bowlscore+fieldscore           

            self.listWidget.addItem(str(totalscore))
            teamtotal=teamtotal+totalscore
        self.label_4.setText(str(teamtotal))
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.label_3.setText(_translate("Dialog", "Players"))
        self.label_2.setText(_translate("Dialog", "                           Points"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




