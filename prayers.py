from PyQt5 import QtCore, QtGui, QtWidgets
import prayer_times as pt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.getPrayerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.getPrayerBtn.setGeometry(QtCore.QRect(10, 260, 391, 27))
        self.getPrayerBtn.setObjectName("getPrayerBtn")

        self.getPrayerBtn.clicked.connect(self.prayer_btn_clicked) 


        self.prayersListView = QtWidgets.QListView(self.centralwidget)
        self.prayersListView.setGeometry(QtCore.QRect(10, 10, 391, 241))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.prayersListView.setFont(font)
        self.prayersListView.setObjectName("prayersListView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def prayer_btn_clicked(self):
        
        times_dict = pt.get_prayers() 

        model = QtGui.QStandardItemModel()
        self.prayersListView.setModel(model)

        for i in times_dict.keys(): 
            # just format the string to look nice in gui 
            if i == "Maghreb": 
                model.appendRow(QtGui.QStandardItem(i + 2*"\t" + times_dict[i])); 
            # any prayer other than maghreb give it more 3*\t 
            else: model.appendRow(QtGui.QStandardItem(i + 3*"\t" + times_dict[i])); 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prayer Times"))
        self.getPrayerBtn.setText(_translate("MainWindow", "Get prayer times"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

