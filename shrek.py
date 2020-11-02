import sys
from config import AMD, INTEL
# from requires import connect_db
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QGridLayout, QMainWindow, \
    QLabel, QListWidgetItem
from PyQt5 import QtGui


class Ui_myWidget:
    def setupUi(self, MyWidget):
        # Делаем заголовок приложения
        MyWidget.setWindowTitle('CPU Guide')
        # Делаем иконку приложения
        MyWidget.setWindowIcon(QtGui.QIcon('cpu.png'))
        # Задаём размер окна
        MyWidget.setGeometry(400, 400, 800, 400)
        MyWidget.setMinimumSize(800, 400)
        MyWidget.setMaximumSize(800, 400)

        self.centralWidget = QWidget(MyWidget)
        self.centralWidget.setStyleSheet('background: #2F4F4F')

        self.centralWidget.resize(800, 400)
        vbox = QVBoxLayout(self.centralWidget)

        self.button_amd = QPushButton(self)
        self.button_amd.setText('AMD')
        self.button_amd.resize(360, 40)
        # self.button_amd.move(30, 70)
        self.button_amd.setIcon(QtGui.QIcon('images/amd_logo.png'))
        self.button_amd.setStyleSheet('background: #90EE90')

        self.button_intel = QPushButton(self)
        self.button_intel.setText('Intel')
        self.button_intel.resize(360, 40)
        # self.button_intel.move(410, 70)
        self.button_intel.setIcon(QtGui.QIcon('images/intel_logo.png'))
        self.button_intel.setStyleSheet('background: #90EE90')

        self.top = QPushButton(self)
        self.top.resize(360, 40)
        self.top.setText('TOP')
        # self.top.move(30, 15)
        self.top.setIcon(QtGui.QIcon('images/trophy_gold.png'))

        self.developer = QPushButton(self)
        self.developer.resize(360, 40)
        self.developer.setText('For developers')
        # self.developer.move(410, 15)
        self.developer.setIcon((QtGui.QIcon('images/laptop.png')))

        grid = QGridLayout()
        grid.addWidget(self.button_amd, 2, 1)
        grid.addWidget(self.button_intel, 2, 2)
        grid.addWidget(self.top, 1, 1)
        grid.addWidget(self.developer, 1, 2)

        # self.listWidget = QListWidget()
        # self.listWidget.setFixedSize(780, 260)

        self.vBoxBtnWidget = QVBoxLayout()

        # self.listWidget.setStyleSheet('background: #786c6c; color: white')
        vbox.addItem(grid)
        # vbox.addWidget(self.listWidget)
        for elem

        vbox.addStretch(1)


class MyWidget(QMainWindow, Ui_myWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.button_amd.clicked.connect(self.showModelList)
        self.button_intel.clicked.connect(self.showModelList)

        self.listWidget.clicked.connect(self.connect_db)

        self.flag = False

    def showModelList(self):
        if self.sender().text() == 'AMD':
            self.flag = 'AMD'
            self.listWidget.clear()
            for elem in AMD:
                self.vBoxBtnWidget.addItem(elem)
        elif self.sender().text() == 'Intel':
            self.flag = 'Intel'
            self.listWidget.clear()
            for elem in INTEL:
                self.vBoxBtnWidget.addItems(elem)


    def connect_db(self):
        import sqlite3 as sq

        if flag == 'Intel':
            print(self.listWidget.sel)

        con = sq.connect('main.db')
        cur = con.cursor()

        result = cur.execute(f"""SELECT * FROM {self.flag.lower()} WHERE name LIKE '%{self.sender().text()}%'""").fetchall()
        con.commit()
        #
        # print(self.flag.lower(), self.sender().text())

    # def seriesChosen(self):
    #     result = connect_db(self.sender().text(), self.flag)
    #     self.listWidget.clear()
    #     self.listWidget.addItems(result)

    # if self.sender.text() == 'ok':
    #     self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
