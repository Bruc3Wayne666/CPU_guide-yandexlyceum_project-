import sys
from config import AMD, INTEL
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QGridLayout, QMainWindow, \
    QLabel, QDialog, QRadioButton
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
        self.button_amd.setIcon(QtGui.QIcon('images/amd_logo.png'))
        self.button_amd.setStyleSheet('background: #90EE90')

        self.button_intel = QPushButton(self)
        self.button_intel.setText('Intel')
        self.button_intel.resize(360, 40)
        self.button_intel.setIcon(QtGui.QIcon('images/intel_logo.png'))
        self.button_intel.setStyleSheet('background: #90EE90')

        self.top = QPushButton(self)
        self.top.resize(360, 40)
        self.top.setText('TOP')
        self.top.setIcon(QtGui.QIcon('images/trophy_gold.png'))

        self.developer = QPushButton(self)
        self.developer.resize(360, 40)
        self.developer.setText('For developers')
        self.developer.setIcon((QtGui.QIcon('images/laptop.png')))

        grid = QGridLayout()
        grid.addWidget(self.button_amd, 2, 1)
        grid.addWidget(self.button_intel, 2, 2)
        grid.addWidget(self.top, 1, 1)
        grid.addWidget(self.developer, 1, 2)

        self.labelWidgetChoice = QLabel()
        self.labelWidgetChoice.setText('Choice the CPU')
        self.labelWidgetChoice.resize(800, 100)
        self.labelWidgetChoice.setStyleSheet('font-size: 32px; color: yellow')
        vbox.addWidget(self.labelWidgetChoice)

        self.listWidget = QListWidget()
        self.listWidget.setFixedSize(780, 260)

        self.listWidget.setStyleSheet('background: #786c6c; color: white')
        vbox.addItem(grid)
        vbox.addWidget(self.listWidget)

        vbox.addStretch(1)

        self.modelListWidget = QListWidget()
        self.modelListWidget.setFixedSize(780, 260)

        self.modelListWidget.setStyleSheet('background: #786c6c; color: white')
        self.modelListWidget.hide()
        vbox.addWidget(self.modelListWidget)

        self.descriptionList = QListWidget()
        self.descriptionList.setFixedSize(780, 260)

        self.descriptionList.setStyleSheet('background: #786c6c; color: white')
        self.descriptionList.hide()
        vbox.addWidget(self.descriptionList)


class MyWidget(QMainWindow, Ui_myWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.button_amd.clicked.connect(self.showModelList)
        self.button_intel.clicked.connect(self.showModelList)
        self.listWidget.itemClicked.connect(self.connect_db)

        self.developer.clicked.connect(self.updateDb)
        self.top.clicked.connect(self.topPage)

        self.flag = False

    def topPage(self):
        import webbrowser


        webbrowser.open('https://www.techradar.com/news/best-processors')

    def showModelList(self):
        self.descriptionList.clear()
        self.descriptionList.hide()
        self.listWidget.show()
        self.modelListWidget.hide()

        if self.sender().text() == 'Intel':
            self.flag = 'Intel'
            self.listWidget.clear()
            self.listWidget.addItems(INTEL)
        elif self.sender().text() == 'AMD':
            self.flag = 'AMD'
            self.listWidget.clear()
            self.listWidget.addItems(AMD)

    def connect_db(self, item):
        import sqlite3 as sq

        con = sq.connect('main.db')
        cur = con.cursor()

        self.result = cur.execute(f"""SELECT * FROM {self.flag.lower()} WHERE name LIKE '%{item.text()}%'""").fetchall()

        self.modelListWidget.clear()
        self.listWidget.hide()
        self.modelListWidget.show()

        for elem in self.result:
            self.modelListWidget.addItem(elem[1])

        self.modelListWidget.itemClicked.connect(self.showList)

        con.commit()
        con.close()

    def showList(self, item):
        flagTwo = False
        information = self.result
        item_cpu = ''

        for elem in information:
            if elem[1] == item.text():
                item_cpu = elem
                flagTwo = True
                break

        if flagTwo:
            item_cpu = list(item_cpu[1:])
            self.modelListWidget.hide()
            self.descriptionList.clear()
            self.descriptionList.show()
            for elem in item_cpu:
                self.descriptionList.addItem(str(elem))

    def updateDb(self):
        from PyQt5.QtWidgets import QLineEdit

        print('kjhuy')
        upDialog = QDialog(self)
        upDialog.setFixedSize(400, 260)
        upDialog.setWindowTitle('Add new CPU')
        upDialog.setStyleSheet("background: #2F4F4F")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cpu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.idLine = QLineEdit(upDialog)
        self.idLine.resize(115, 20)
        self.idLine.setStyleSheet('background: #90EE90')
        self.idLine.move(90, 20)

        self.modelLine = QLineEdit(upDialog)
        self.modelLine.resize(115, 20)
        self.modelLine.setStyleSheet('background: #90EE90')
        self.modelLine.move(90, 60)

        self.yearLine = QLineEdit(upDialog)
        self.yearLine.resize(115, 20)
        self.yearLine.setStyleSheet('background: #90EE90')
        self.yearLine.move(90, 100)

        self.priceLine = QLineEdit(upDialog)
        self.priceLine.resize(115, 20)
        self.priceLine.setStyleSheet('background: #90EE90')
        self.priceLine.move(90, 140)

        self.archLine = QLineEdit(upDialog)
        self.archLine.resize(115, 20)
        self.archLine.setStyleSheet('background: #90EE90')
        self.archLine.move(90, 180)

        self.coresLine = QLineEdit(upDialog)
        self.coresLine.resize(115, 20)
        self.coresLine.setStyleSheet('background: #90EE90')
        self.coresLine.move(280, 20)

        self.threadsLine = QLineEdit(upDialog)
        self.threadsLine.resize(115, 20)
        self.threadsLine.setStyleSheet('background: #90EE90')
        self.threadsLine.move(280, 60)

        self.fabLine = QLineEdit(upDialog)
        self.fabLine.resize(115, 20)
        self.fabLine.setStyleSheet('background: #90EE90')
        self.fabLine.move(280, 100)

        self.tdpLine = QLineEdit(upDialog)
        self.tdpLine.resize(115, 20)
        self.tdpLine.setStyleSheet('background: #90EE90')
        self.tdpLine.move(280, 140)

        self.imgLine = QLineEdit(upDialog)
        self.imgLine.resize(115, 20)
        self.imgLine.setStyleSheet('background: #90EE90')
        self.imgLine.move(280, 180)

        idLabel = QLabel(upDialog)
        idLabel.resize(20, 20)
        idLabel.setStyleSheet('color: White')
        idLabel.move(67, 20)
        idLabel.setText('id:')

        modelLabel = QLabel(upDialog)
        modelLabel.resize(61, 20)
        modelLabel.setStyleSheet('color: White')
        modelLabel.move(20, 60)
        modelLabel.setText('Model name:')

        yearLabel = QLabel(upDialog)
        yearLabel.resize(31, 20)
        yearLabel.setStyleSheet('color: White')
        yearLabel.move(56, 100)
        yearLabel.setText('Year:')

        priceLabel = QLabel(upDialog)
        priceLabel.resize(31, 20)
        priceLabel.setStyleSheet('color: White')
        priceLabel.move(56, 140)
        priceLabel.setText('Price:')

        archLabel = QLabel(upDialog)
        archLabel.resize(61, 20)
        archLabel.setStyleSheet('color: White')
        archLabel.move(20, 180)
        archLabel.setText('Architecture:')

        coresLabel = QLabel(upDialog)
        coresLabel.resize(41, 20)
        coresLabel.setStyleSheet('color: White')
        coresLabel.move(236, 20)
        coresLabel.setText('Cores:')

        threadsLabel = QLabel(upDialog)
        threadsLabel.resize(51, 20)
        threadsLabel.setStyleSheet('color: White')
        threadsLabel.move(226, 60)
        threadsLabel.setText('Threads:')

        fabLabel = QLabel(upDialog)
        fabLabel.resize(31, 20)
        fabLabel.setStyleSheet('color: White')
        fabLabel.move(246, 100)
        fabLabel.setText('Fab:')

        tdpLabel = QLabel(upDialog)
        tdpLabel.resize(31, 20)
        tdpLabel.setStyleSheet('color: White')
        tdpLabel.move(246, 140)
        tdpLabel.setText('TDP:')

        imgLabel = QLabel(upDialog)
        imgLabel.resize(51, 20)
        imgLabel.setStyleSheet('color: White')
        imgLabel.move(220, 180)
        imgLabel.setText('Type smt:')

        commitBtn = QPushButton(upDialog)
        commitBtn.setStyleSheet('background: #90EE90')
        commitBtn.setText('OK')
        commitBtn.resize(90, 30)
        commitBtn.move(115, 220)

        cancelBtn = QPushButton(upDialog)
        cancelBtn.setStyleSheet('background: #90EE90')
        cancelBtn.setText('Cancel')
        cancelBtn.resize(90, 30)
        cancelBtn.move(205, 220)

        radioAMD = QRadioButton(upDialog)
        radioAMD.resize(41, 17)
        radioAMD.move(10, 10)
        radioAMD.setText('AMD')

        radioIntel = QRadioButton(upDialog)
        radioIntel.resize(41, 17)
        radioIntel.move(10, 30)
        radioIntel.setText('Intel')

        radioAMD.clicked.connect(self.selectManufacturer)
        radioIntel.clicked.connect(self.selectManufacturer)

        upDialog.setWindowIcon(icon)

        upDialog.show()

        commitBtn.clicked.connect(self.addNew)

    def selectManufacturer(self):
        self.manufacturer = self.sender().text()

    def addNew(self):
        import sqlite3 as sq

        addInfo = []
        addInfo.append((self.idLine.text(), self.manufacturer, self.modelLine.text(), self.yearLine.text(),
                        self.priceLine.text(), self.archLine.text(), self.coresLine.text(),
                        self.threadsLine.text(), self.fabLine.text(), self.tdpLine.text(),
                        self.imgLine.text()))
        addInfo = addInfo[0]

        try:
            with sq.connect('main.db') as con:
                cur = con.cursor()

                cur.execute(f"""INSERT INTO {self.manufacturer.lower()} VALUES ({int(addInfo[0])},
'{addInfo[2]}', {int(addInfo[3])}, {int(addInfo[4])}, '{addInfo[5]}', {int(addInfo[6])}, {int(addInfo[7])},
{int(addInfo[8])}, {int(addInfo[9])}, '{addInfo[10]}')""")

                con.commit()
        except Exception:

            string = f"INSERT INTO {self.manufacturer.lower()} VALUES ({int(addInfo[0])}, '{addInfo[2]}', {int(addInfo[3])}, {int(addInfo[4])}, '{addInfo[5]}', {int(addInfo[6])}, {int(addInfo[7])}, {int(addInfo[8])}, {int(addInfo[9])}, '{addInfo[10]}')"

            print('Не работает заполнение по запросу:')
            print(string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
