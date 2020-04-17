# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_table_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla_libros = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_libros.setGeometry(QtCore.QRect(15, 81, 771, 471))
        self.tabla_libros.setObjectName("tabla_libros")
        self.tabla_libros.setColumnCount(7)
        self.tabla_libros.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_libros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_libros.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_libros.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_libros.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_libros.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_libros.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_libros.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tabla_libros.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tabla_libros.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "titulo"))
        item = self.tabla_libros.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "paginas"))
        item = self.tabla_libros.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ver detalles"))
        item = self.tabla_libros.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "borrar"))
        item = self.tabla_libros.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "editar"))
        item = self.tabla_libros.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "portada"))
        self.label.setText(_translate("MainWindow", "LISTADO USANDO UN TABLE WIDGET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

