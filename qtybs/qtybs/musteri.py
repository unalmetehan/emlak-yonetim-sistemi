from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
veritab = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="emlak"
)

class Ui_MainWindow(object):
    def adminacma(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_adminwindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def check_password(self):
        if self.lineEdit.text() == "admin":
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1245, 801)
        
        # Arka plan rengi
        MainWindow.setStyleSheet("background-color: #b0c4de;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Font stili ve boyutları
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        MainWindow.setFont(font)

        # Buton stilleri
        button_style = """
            QPushButton {
                background-color: #4CAF50; /* Yeşil */
                color: white;
                font-weight: bold;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049; /* Daha koyu yeşil */
            }
            QPushButton:disabled {
                background-color: rgba(76, 175, 80, 0.3);
                border: 2px solid rgba(76, 175, 80, 0.3);
            }
        """

        combobox_style = """
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 5px;
                color: #2d2d30;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
            }
        """
        
        lineedit_style = """
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 5px;
                color: #2d2d30;
            }
        """

        table_style = """
            QTableWidget {
                background-color: #ffffff;
                border: 2px solid #4CAF50;
                border-radius: 10px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
        """

        label_style = """
            QLabel {
                color: #ffffff;
                font-size: 12pt;
            }
        """

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 350, 151, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet(combobox_style)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 350, 151, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setStyleSheet(combobox_style)

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(380, 350, 151, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setStyleSheet(combobox_style)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 240, 181, 41))
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.StyleItalic))
        self.label.setStyleSheet(label_style)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 210, 121, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet(label_style)
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 260, 121, 41))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setStyleSheet(label_style)

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(560, 350, 151, 41))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setStyleSheet(combobox_style)

        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(730, 350, 151, 41))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setStyleSheet(combobox_style)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 410, 801, 361))
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet(table_style)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)




        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 50, 431, 71))
        self.label_2.setFont(QtGui.QFont("Arial Black" ,16, QtGui.QFont.StyleItalic))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(label_style)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(940, 110, 71, 30))
        self.label_3.setFont(QtGui.QFont("Arial ", 10, QtGui.QFont.StyleItalic))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(label_style)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(930, 50, 211, 51))
        self.label_4.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.StyleItalic))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(label_style)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1020, 110, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(lineedit_style)
        self.lineEdit.textChanged.connect(self.check_password)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.adminacma())
        self.pushButton.setGeometry(QtCore.QRect(990, 150, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet(button_style)

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.comboBox.currentIndexChanged.connect(self.filitre)
        self.comboBox_2.currentIndexChanged.connect(self.filitre)
        self.comboBox_3.currentIndexChanged.connect(self.filitre)
        self.comboBox_4.currentIndexChanged.connect(self.filitre)
        self.comboBox_5.currentIndexChanged.connect(self.filitre)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def filitre(self):
        print("listelendi")
        mycursor = veritab.cursor()
        selected_fiyat = self.comboBox.currentText()
        selected_adres = self.comboBox_2.currentText()
        selected_oda_sayisi = self.comboBox_3.currentText()
        selected_kat = self.comboBox_4.currentText()
        selected_balkon = self.comboBox_5.currentText()

        sorgu = "SELECT * FROM evler WHERE 1=1"
        deger = []

        if selected_fiyat != "FİYAT ARALIĞI":
         sorgu += " AND fiyat_araligi = %s"
         deger.append(selected_fiyat)

        if selected_adres != "ADRES":
         sorgu += " AND adres = %s"
         deger.append(selected_adres)

        if selected_oda_sayisi != "ODA SAYISI":
         sorgu += " AND oda_sayisi = %s"
         deger.append(selected_oda_sayisi)

        if selected_kat != "KAT":
         sorgu += " AND kat = %s"
         deger.append(selected_kat)

        if selected_balkon != "BALKON":
         sorgu += " AND balkon = %s"
         deger.append(selected_balkon)

    # Değerlerinizi tuple'a dönüştürün
         deger = tuple(deger)

        sorgu = "SELECT * FROM evler WHERE fiyat_araligi = %s or adres = %s and oda_sayisi = %s and kat = %s and balkon = %s"
        deger = (selected_fiyat, selected_adres, selected_oda_sayisi, selected_kat, selected_balkon)
        mycursor.execute(sorgu, deger)

        records = mycursor.fetchall()

        print("listeme {} sonuç gösterdi.".format(len(records)))

        self.tableWidget.setRowCount(len(records))
        for i, record in enumerate(records):
          print("Row {}: {}".format(i, record))
          for j, value in enumerate(record):
            item = QtWidgets.QTableWidgetItem(str(value))
            self.tableWidget.setItem(i, j, item)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "FİYAT ARALIĞI"))
        self.comboBox.setItemText(1, _translate("MainWindow", "500000-700000"))
        self.comboBox.setItemText(2, _translate("MainWindow", "700000-900000"))
        self.comboBox.setItemText(3, _translate("MainWindow", "1100000-1300000"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1300000-1500000"))
        self.comboBox.setItemText(5, _translate("MainWindow", "1500000-1700000"))
        self.comboBox.setItemText(6, _translate("MainWindow", "1700000-1900000"))
        self.comboBox.setItemText(7, _translate("MainWindow", "1900000-2100000"))
        self.comboBox.setItemText(8, _translate("MainWindow", "2100000+"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ADRES"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "ANKARA"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "İSTANBUL"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "KAHRAMANMARAŞ"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "İZMİR"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "ORDU"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "ODA SAYISI"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "4"))
        self.label.setText(_translate("MainWindow", "İLAN DURUMU"))
        self.checkBox.setText(_translate("MainWindow", "KİRALIK"))
        self.checkBox_2.setText(_translate("MainWindow", "SATILIK"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "KAT"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "1.KAT"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "2. KAT"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "3. KAT"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "4.KAT"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "5. KAT"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "6. KAT"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "7. KAT"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "BALKON "))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "EVET"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "HAYIR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "FİYAT"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ADRES"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ODA SAYISI"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "KAT"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "BALKON"))
        self.label_2.setText(_translate("MainWindow", "YBS GAYRİMENKULE HOŞGELDİNİZ"))
        self.label_3.setText(_translate("MainWindow", "ŞİFRE:"))
        self.label_4.setText(_translate("MainWindow", "YÖNETİCİ GİRİŞİ İÇİN"))
        self.pushButton.setText(_translate("MainWindow", "GİRİŞ YAP"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())