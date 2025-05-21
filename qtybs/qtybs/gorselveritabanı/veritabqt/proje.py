import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_MainWindow(object):
    def _init_(self):
        self.conn = None
        self.cursor = None
        self.setup_database_connection()

    def setup_database_connection(self):
        # Veritabanına bağlanma
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="denme"
        )
        self.cursor = self.conn.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1245, 801)
        
        # Arka plan rengi
        MainWindow.setStyleSheet("background-color: #2d2d30;")
        
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
        self.checkBox.setGeometry(QtCore.QRect(120, 210, 121, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet(label_style)
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 260, 121, 41))
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
        self.tableWidget.setGeometry(QtCore.QRect(20, 410, 681, 331))
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(5)
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

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 70, 431, 71))
        self.label_2.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.StyleItalic))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(label_style)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(940, 130, 131, 51))
        self.label_3.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.StyleItalic))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(label_style)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(940, 80, 231, 41))
        self.label_4.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.StyleItalic))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(label_style)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(940, 190, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(lineedit_style)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(940, 260, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet(button_style)

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(940, 320, 221, 41))
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.setText("Sil")
        self.deleteButton.setStyleSheet(button_style)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.adminacma)
        self.lineEdit.textChanged.connect(self.check_password)
        self.deleteButton.clicked.connect(self.delete_selected_row)

    def delete_selected_row(self):
        current_row = self.tableWidget.currentRow()
        if current_row != -1:
            # Tablo'dan veriyi silme
            fiyat_araligi = self.tableWidget.item(current_row, 0).text()
            adres = self.tableWidget.item(current_row, 1).text()
            oda_sayisi = self.tableWidget.item(current_row, 2).text()
            kat = self.tableWidget.item(current_row, 3).text()
            balkon_sayisi = self.tableWidget.item(current_row, 4).text()

            try:
                delete_query = "DELETE FROM your_table WHERE fiyat_araligi = %s AND adres = %s AND oda_sayisi = %s AND kat = %s AND balkon_sayisi = %s"
                self.cursor.execute(delete_query, (fiyat_araligi, adres, oda_sayisi, kat, balkon_sayisi))
                self.conn.commit()
                
                self.tableWidget.removeRow(current_row)
                QtWidgets.QMessageBox.information(None, "Başarılı", "Kayıt başarıyla silindi.")
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(None, "Hata", f"Veri silinirken bir hata oluştu: {err}")

if __name__ == "_main_":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())