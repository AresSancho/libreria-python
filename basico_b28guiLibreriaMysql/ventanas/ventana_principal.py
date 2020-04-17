# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 731, 181))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuLibros = QtWidgets.QMenu(self.menubar)
        self.menuLibros.setObjectName("menuLibros")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submenu_insertar_libro = QtWidgets.QAction(MainWindow)
        self.submenu_insertar_libro.setObjectName("submenu_insertar_libro")
        self.submenu_listar_libros = QtWidgets.QAction(MainWindow)
        self.submenu_listar_libros.setObjectName("submenu_listar_libros")
        self.actioninicio = QtWidgets.QAction(MainWindow)
        self.actioninicio.setObjectName("actioninicio")
        self.submenu_inicio = QtWidgets.QAction(MainWindow)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.submenu_list_widget_libros = QtWidgets.QAction(MainWindow)
        self.submenu_list_widget_libros.setObjectName("submenu_list_widget_libros")
        self.submenu_table_widget_libros = QtWidgets.QAction(MainWindow)
        self.submenu_table_widget_libros.setObjectName("submenu_table_widget_libros")
        self.menuLibros.addAction(self.submenu_insertar_libro)
        self.menuLibros.addAction(self.submenu_listar_libros)
        self.menuLibros.addAction(self.submenu_list_widget_libros)
        self.menuLibros.addAction(self.submenu_table_widget_libros)
        self.menuLibros.addAction(self.submenu_inicio)
        self.menubar.addAction(self.menuLibros.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bienvenido a mi aplicacion de gestión \n"
" de una librería"))
        self.menuLibros.setTitle(_translate("MainWindow", "Libros"))
        self.submenu_insertar_libro.setText(_translate("MainWindow", "Insertar Libro"))
        self.submenu_listar_libros.setText(_translate("MainWindow", "Listar Libros"))
        self.actioninicio.setText(_translate("MainWindow", "inicio"))
        self.submenu_inicio.setText(_translate("MainWindow", "inicio"))
        self.submenu_list_widget_libros.setText(_translate("MainWindow", "Listar Libros usando List Widget"))
        self.submenu_table_widget_libros.setText(_translate("MainWindow", "Listar Libros usando Table Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

