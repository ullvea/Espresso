# https://github.com/ullvea/Espresso.git
# pip install pipreqs
import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Кофе")
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        self.save_results()

    def save_results(self):
        rows = self.cur.execute("SELECT * FROM coffee").fetchall()
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'сорт',
                                              'степень обжарки', 'молотый/в зернах',
                                              'описание вкуса', 'цена', 'объем упаковки'])
        for i, j in enumerate(rows):
            for index, item in enumerate(j):
                self.table.setItem(i, index, QTableWidgetItem(str(item)))
        self.con.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())