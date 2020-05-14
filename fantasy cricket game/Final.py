from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit
import sqlite3
conn=sqlite3.connect('final.db')

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 771, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        #H LAYOUT FOR BAT/BALL/AR/WK
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #LABEL FOR BAT
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        #LABEL FOR BAT COUNTING
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        #LABEL FOR BALL
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        #LABEL FOR BALL COUNTING
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        #LABEL FOR AR
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        #LABEL FOR AR COUNTING
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        #LABEL FOR WK
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        #LABEL FOR WK COUNTING
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        #LABEL FOR YOUR SELECTIONS
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #H LAYOUT FOR POINTS AVL/USED
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 771, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #LABEL FOR POINTS AVL
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setIndent(60)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        #LABEL FOR AVL COUNTING
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        #LABEL FOR POINTS USED
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setIndent(70)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        #LABEL FOR USED COUNTING
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        #LIST 1
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setGeometry(QtCore.QRect(10, 200, 331, 401))
        self.list1.setObjectName("list1")
        #LIST2
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setGeometry(QtCore.QRect(450, 200, 331, 401))
        self.list2.setObjectName("list2")
        ##LABEL FOR SYMBOL >
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(390, 380, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        #H LAYOUT FOR RBTNS
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 150, 331, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #RBTN FOR BAT
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        #RBTN FOR BALL
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        #RBTN FOR AR
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        #RBTN FOR WK
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        #H LAYOUT FOR TEAM NAME
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(450, 150, 331, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #LABEL FOR TEAM NAME
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setIndent(50)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        #FOR DISPLAYING TEAM NAME
        self.line = QtWidgets.QLineEdit(self.centralwidget)
        self.line.setObjectName("line")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.horizontalLayout_4.addWidget(self.line)
        
        #MENU
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #ACTIONS IN MENU5
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionNEW_Team.triggered.connect(self.new)
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionOPEN_Team.triggered.connect(self.open)
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionSAVE_Team.triggered.connect(self.save)
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionEVALUATE_Team.triggered.connect(self.evaluate)
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #LOC FOR CLICKING FOR ADDING AND REMOVING ITEMS FROM LISTS
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)
        #LOC FOR RBTNS
        self.radioButton.toggled.connect(self.ctg)
        self.radioButton_2.toggled.connect(self.ctg)
        self.radioButton_3.toggled.connect(self.ctg)
        self.radioButton_4.toggled.connect(self.ctg)
        #VAR FOR COUNTING
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0
######################################################################         
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Your selections"))
        self.label_11.setText(_translate("MainWindow", "Points Available"))
        self.label_10.setText(_translate("MainWindow", "1000"))
        self.label_12.setText(_translate("MainWindow", "Points Used"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", ">"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BOW"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team Name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
######################################################################
#menu
    def new(self):
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0
        self.list1.clear()
        self.list2.clear()
        text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter team name:",QLineEdit.Normal,"")
        if ok and text != '':
            self.line.setText(str(text))
        self.show()

        
    def open(self):
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0
        self.list1.clear()
        self.list2.clear()
        sql1 = "select name from teams;"
        cur = conn.execute(sql1)
        teams = []
        for row in cur:
            teams.append(row[0])
        team, ok = QtWidgets.QInputDialog.getItem(MainWindow,"select","Choose Team",teams,0,False)
        if ok:
            self.line.setText(team)
        
        sql2 = "SELECT players,value from teams where name='"+team+"';"
        cur = conn.execute(sql2)
        row = cur.fetchone()
        selected = row[0].split(',')
        self.list2.addItems(selected)
        self.used = row[1]
        self.avl = 1000-row[1]
        count = self.list2.count()
        for i in range(count-1):
            ply = self.list2.item(i).text()
            sql3 = "select ctg from stats where player='"+ply+"';"
            cur=conn.execute(sql3)
            row=cur.fetchone()
            ctgr=row[0]
            if ctgr=="BAT":
                self.bat+=1
            if ctgr=="BWL":
                self.bwl+=1
            if ctgr=="AR":
                self.ar+=1
            if ctgr=="WK":
                self.wk+=1  
        self.show()

        
    def save(self):
        coun=self.list2.count()
        selected=""
        for i in range(coun):
            selected=selected+self.list2.item(i).text()
            if i<coun:
                selected+=","
        self.saveteam(self.line.text(),selected,self.used)
    def saveteam(self,nm,ply,val):
        if self.bat+self.bwl+self.ar+self.wk != 11:
            self.showdlg("You must have 11 players in team")
            return
        sql4="INSERT INTO teams (name,players,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
        try:
            cur=conn.execute(sql4)
            self.showdlg("Team Saved")
            conn.commit()
        except:
            self.showdlg("Error")
            conn.rollback()
    
    def evaluate(self):
        from evls import Ui_Dialog 
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec()
 #function for displaying 
    def show(self):
        self.label_3.setText(str(self.bat))
        self.label_5.setText(str(self.bwl))
        self.label_9.setText(str(self.wk))
        self.label_7.setText(str(self.ar))
        self.label_10.setText(str(self.avl))
        self.label_13.setText(str(self.used))

#function for error msg display
    def error(self,ctgr,item):
        msg=''
        if ctgr=="BAT" and self.bat>=5:
            msg="You cant select more than 5 batsman"
        if ctgr=="BWL" and self.bwl>=5:
            msg="You cant select more than 5 bowlers"
        if ctgr=="AR" and self.ar>=3:
            msg="You cant select more than 3 all rounders"
        if ctgr=="WK" and self.wk>=1:
            msg="You cant select more than 1 wicket-keeper"
        if msg!='':
            self.showdlg(msg)
            return False
        if self.avl<=0:
            msg="You have exceeded the points limit"
            self.showdlg(msg)
            return False
        if ctgr=="BAT":
            self.bat+=1
        if ctgr=="BWL":
            self.bwl+=1
        if ctgr=="AR":
            self.ar+=1
        if ctgr=="WK":
            self.wk+=1
            
        sql="SELECT value from stats where player='"+item.text()+"'"
        cur=conn.execute(sql)
        row=cur.fetchone()
        self.avl-=int(row[0])
        self.used+=int(row[0])
        return True

#function for selecting players from list1
    def removelist1(self,item):
        ctgr=''
        if self.radioButton.isChecked()==True:
            ctgr='BAT'
        if self.radioButton_2.isChecked()==True:
            ctgr='BWL'
        if self.radioButton_3.isChecked()==True:
            ctgr='AR'
        if self.radioButton_4.isChecked()==True:
            ctgr='WK'
        ret=self.error(ctgr,item)
        
        if ret==True:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
            self.show()

#function for categorizing players
    def ctg(self):
        ctgr=''
        if self.radioButton.isChecked()==True:
            ctgr='BAT'
        if self.radioButton_2.isChecked()==True:
            ctgr='BWL'
        if self.radioButton_3.isChecked()==True:
            ctgr='AR'
        if self.radioButton_4.isChecked()==True:
            ctgr='WK'
       	
        self.filllist(ctgr)

#function for removing players from list2
    def removelist2(self,item):
        self.list2.takeItem(self.list2.row(item))
        
        cursor = conn.execute("SELECT player,value, ctg from stats where player='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.radioButton.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="BWL":
            self.bwl-=1
            if self.radioButton_2.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.radioButton_3.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.radioButton_4.isChecked()==True:
                self.list1.addItem(item.text())
        self.show()

#function for displaying team name
    def filllist(self,ctgr):
        if self.line.text()=='':
            self.showdlg("Enter team name")
            return
        
        self.list1.clear()
        sql="SELECT player from players where ctg='"+ctgr+"';"
        cur=conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.list2.count()):
                selected.append(self.list2.item(i).text())
            if row[0] not in selected:self.list1.addItem(row[0])


#function for displaying dlg box for evaluating score
    def showdlg(self,msg):
        Dlg=QtWidgets.QMessageBox()
        Dlg.setText(msg)
        Dlg.setWindowTitle("?")
        ret=Dlg.exec()
###################################################################### 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
