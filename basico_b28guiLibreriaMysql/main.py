'''
Created on Mar 30, 2020

@author: aressancho
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal , ventana_registrar_libro,\
    ventana_listado_libros, ventana_list_widget, ventana_table_widget,\
    ventana_editar_libro, ventana_ver_detalles_libro
import sys
from modelo.clases import Libro
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton, QFileDialog,\
    QPixmap, QLabel
from _functools import partial
import shutil #facilidades para copiar un archivo digital
from pathlib import Path#facilidades para manejo de rutas
from validadores import  validadores_libro
#variable con el resultado de base de datos:
lista_resultado = None

#inicio definicion funciones

def registrar_libro():
    libro = Libro()
    
    libro.titulo = ui_registrar_libro.entrada_titulo_libro.text()
    libro.titulo = libro.titulo.strip()#elimina espacios en blanco al principio y al final
    #asi valido el titulo
    resultado_validar_titulo = validadores_libro.validar_titulo(libro.titulo)
    if resultado_validar_titulo == None :
        ui_registrar_libro.label_error_titulo.setText("<font color='red'>titulo incorrecto</font>")
        return
    else:
        ui_registrar_libro.label_error_titulo.clear()
    
    libro.paginas = ui_registrar_libro.entrada_paginas_libro.text()
    libro.precio = ui_registrar_libro.entrada_precio_libro.text()
    #checkbox
    if ui_registrar_libro.checkbox_digital.isChecked():
        libro.digital = True
    #combo
    indice_seleccionado = ui_registrar_libro.combo_tapa.currentIndex()
    libro.tapa = ui_registrar_libro.combo_tapa.itemText(indice_seleccionado)
    #radio button
    if ui_registrar_libro.radio_standar.isChecked() :
        libro.envio = "standar"
    
    if ui_registrar_libro.radio_urgente.isChecked() :
        libro.envio = "urgente"    
    
    if ui_registrar_libro.radio_prioritario.isChecked():
        libro.envio = "prioritario"    
    
    id_generado = operaciones_bd.registro_libro(libro)
    #despues de registrar enbase de datos, quiero guardar la imagen temporal
    #renombrandola al id del registro realizado. Para saber que dicha imagen
    #es la asociaciada a dicho registro
    
    #solo muevo la imagen si existe
    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/" + str(id_generado) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)
    
    QMessageBox.about(MainWindow,"Info","Registro de libro OK")

def seleccionar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    ancho_label_imagen = ui_registrar_libro.label_imagen.width()
    alto_label_imagen = ui_registrar_libro.label_imagen.height()
    #redimension por ancho
    #pixmap_redim = pixmap.scaledToWidth(ancho_label_imagen)
    #ui_registrar_libro.label_imagen.setPixmap(pixmap_redim)
    #redimension por alto
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_registrar_libro.label_imagen.setPixmap(pixmap_redim)
    #redimension por alto y ancho
    #pixmap_redim = pixmap.scaled(ancho_label_imagen,alto_label_imagen)
    #ui_registrar_libro.label_imagen.setPixmap(pixmap_redim)

def mostar_registro_libro():
    ui_registrar_libro.setupUi(MainWindow)
    ui_registrar_libro.boton_registrar_libro.clicked.connect(registrar_libro)
    ui_registrar_libro.boton_seleccionar_archivo.clicked.connect(seleccionar_imagen)
    ui_registrar_libro.label_error_titulo.clear()
    ui_registrar_libro.label_error_paginas.clear()
    
def mostrar_listado_libros():
    ui_listar_libros.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_libros()
    texto = ""
    for l in lista_resultado:
        texto +=  "id: " + str(l[0]) + " titulo: " + l[1] + " paginas: " + str(l[2])+ "\n"
    ui_listar_libros.listado_libros.setText(texto)

def mostrar_list_widget():
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_libros()
    #voy a rellenar el list widget
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget_libros.addItem(l[1] + " paginas: " + str(l[2]))
    ui_ventana_list_widget.list_widget_libros.itemClicked.connect(mostrar_registro)    

#funcion que hace algo, en este caso mostrar toda la formacion,
#cuando se haga click en un elemento del list widget
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_libros.currentRow()
    texto = ""
    texto += "titulo: " + lista_resultado[indice_seleccionado][1]+"\n"
    texto += "paginas: " + str(lista_resultado[indice_seleccionado][2]) + "\n"
    texto += "precio: " + str(lista_resultado[indice_seleccionado][3])    
    QMessageBox.about(MainWindow,"Info", texto)

#funciones para la tabla 
def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)
    #vamos a rellenar la tabla:
    libros = operaciones_bd.obtener_libros()
    fila = 0
    for l in libros:
        ui_ventana_table_widget.tabla_libros.insertRow(fila)
        #y ahora meto las celdas correspondientes en la fila 
        columna_indice = 0
        for valor in l:
            
            if columna_indice == 4:
                if valor == 0:
                    valor = "NO"
                else:
                    valor = "SI"
            
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.tabla_libros.setItem(fila,columna_indice,celda)
            columna_indice += 1
        #despues de rellenar los datos en la fila 
        #boton ver detalles:
        boton_ver_detalles = QPushButton("ver detalles")
        boton_ver_detalles.clicked.connect(partial(cargar_ver_detalles,l[0]))
        ui_ventana_table_widget.tabla_libros.setCellWidget(fila,3,boton_ver_detalles)
        
        #voy a meterle un boton de borrar
        boton_borrar = QPushButton("borrar")
        boton_borrar.clicked.connect(partial(borrar_libro,l[0]))
        ui_ventana_table_widget.tabla_libros.setCellWidget(fila,4,boton_borrar)
        
        boton_editar = QPushButton("editar")
        boton_editar.clicked.connect(partial(editar_libro,l[0],l[1]))
        ui_ventana_table_widget.tabla_libros.setCellWidget(fila,5,boton_editar)
        
        #muestro una miniatura:
        label_miniatura = QLabel()
        ruta_imagen = "imagenes/" + str(l[0]) + ".jpg"
        objeto_path = Path(ruta_imagen)
        existe = objeto_path.is_file()
        if existe == True: #Path("imagenes/" + l[0] + ".jpg").is_file() :
            pixmap = QPixmap(ruta_imagen)
            pixmap_redim = pixmap.scaledToHeight(40)
            label_miniatura.setPixmap(pixmap_redim)
            ui_ventana_table_widget.tabla_libros.setCellWidget(fila,6,label_miniatura)
            
        fila += 1

def cargar_ver_detalles(id):
    QMessageBox.about(MainWindow,"Info","ver detalles del registro de id: " + str(id))
    ui_ventana_ver_detalles_libro.setupUi(MainWindow)
    libro = operaciones_bd.obtener_libro_por_id(id)
    
    ui_ventana_ver_detalles_libro.entrada_titulo_libro.setText(libro.titulo)
    ui_ventana_ver_detalles_libro.entrada_paginas_libro.setText(str(libro.paginas))
    ui_ventana_ver_detalles_libro.entrada_precio_libro.setText(str(libro.precio))

    if libro.digital :
        ui_ventana_ver_detalles_libro.checkbox_digital.setChecked(True)
    
    ui_ventana_ver_detalles_libro.combo_tapa.setCurrentText(libro.tapa)
    
    if libro.envio == "standar":
        ui_ventana_ver_detalles_libro.radio_standar.setChecked(True)
    
    if libro.envio == "urgente":
        ui_ventana_ver_detalles_libro.radio_urgente.setChecked(True)
        
    if libro.envio == "prioritario":
        ui_ventana_ver_detalles_libro.radio_prioritario.setChecked(True)
    
    #para cuando se quiera editar libro, cargo su imagen en 
    #el label imagen 
    pixmap = QPixmap("imagenes/"+str(libro.id)+".jpg")
    alto_label_imagen = ui_ventana_ver_detalles_libro.label_imagen.height()
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_ver_detalles_libro.label_imagen.setPixmap(pixmap_redim)
    
    
def editar_libro(id,titulo):
    QMessageBox.about(MainWindow,"Info","vas a editar el registro de id: " + str(id) + " titulo: " + titulo)
    ui_ventana_editar_libro.setupUi(MainWindow)
    #lo suyo ahora es sacar de base de datos toda la informacion a editar
    libro_a_editar = operaciones_bd.obtener_libro_por_id(id)
    ui_ventana_editar_libro.entrada_titulo_libro.setText(libro_a_editar.titulo)
    ui_ventana_editar_libro.label_error_titulo.clear()
    ui_ventana_editar_libro.entrada_paginas_libro.setText(str(libro_a_editar.paginas))
    ui_ventana_editar_libro.label_error_paginas.clear()
    ui_ventana_editar_libro.entrada_precio_libro.setText(str(libro_a_editar.precio))
    
    if libro_a_editar.digital :
        ui_ventana_editar_libro.checkbox_digital.setChecked(True)
    
    ui_ventana_editar_libro.combo_tapa.setCurrentText(libro_a_editar.tapa)
    
    if libro_a_editar.envio == "standar":
        ui_ventana_editar_libro.radio_standar.setChecked(True)
    
    if libro_a_editar.envio == "urgente":
        ui_ventana_editar_libro.radio_urgente.setChecked(True)
        
    if libro_a_editar.envio == "prioritario":
        ui_ventana_editar_libro.radio_prioritario.setChecked(True)
    
    #para cuando se quiera editar libro, cargo su imagen en 
    #el label imagen 
    pixmap = QPixmap("imagenes/"+str(libro_a_editar.id)+".jpg")
    alto_label_imagen = ui_ventana_editar_libro.label_imagen.height()
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_editar_libro.label_imagen.setPixmap(pixmap_redim)
    
    
    
    ui_ventana_editar_libro.boton_guardar_cambios_libro.clicked.connect(partial(guardar_cambios_libro,libro_a_editar.id))
    ui_ventana_editar_libro.boton_seleccionar_archivo.clicked.connect(seleccionar_imagen_editar)

def seleccionar_imagen_editar():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    ancho_label_imagen = ui_ventana_editar_libro.label_imagen.width()
    alto_label_imagen = ui_ventana_editar_libro.label_imagen.height()
    #redimension por ancho
    #pixmap_redim = pixmap.scaledToWidth(ancho_label_imagen)
    #ui_registrar_libro.label_imagen.setPixmap(pixmap_redim)
    #redimension por alto
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_editar_libro.label_imagen.setPixmap(pixmap_redim)
    #redimension por alto y ancho
    #pixmap_redim = pixmap.scaled(ancho_label_imagen,alto_label_imagen)
    #ui_registrar_libro.label_imagen.setPixmap(pixmap_redim)

    
def guardar_cambios_libro(id):
    libro_guardar_cambios = Libro()
    libro_guardar_cambios.titulo = ui_ventana_editar_libro.entrada_titulo_libro.text()
    
    #asi valido el titulo
    resultado_validar_titulo = validadores_libro.validar_titulo(libro_guardar_cambios.titulo)
    if resultado_validar_titulo == None :
        ui_ventana_editar_libro.label_error_titulo.setText("<font color='red'>titulo incorrecto</font>")
        return
    else:
        ui_ventana_editar_libro.label_error_titulo.clear()
    
    
    libro_guardar_cambios.paginas = ui_ventana_editar_libro.entrada_paginas_libro.text()
    libro_guardar_cambios.precio = ui_ventana_editar_libro.entrada_precio_libro.text()
    
    if ui_ventana_editar_libro.checkbox_digital.isChecked():
        libro_guardar_cambios.digital = True
    
    libro_guardar_cambios.tapa = ui_ventana_editar_libro.combo_tapa.currentText()
    
    if ui_ventana_editar_libro.radio_standar.isChecked():
        libro_guardar_cambios.envio = "standar"
        
    if ui_ventana_editar_libro.radio_urgente.isChecked():
        libro_guardar_cambios.envio = "urgente"
        
    if ui_ventana_editar_libro.radio_prioritario.isChecked():
        libro_guardar_cambios.envio = "prioritario"    
    
    libro_guardar_cambios.id = id
    
    QMessageBox.about(MainWindow,"Info","guardar cambios sobre el registro de id: " + str(id))
    operaciones_bd.guardar_cambios_libro(libro_guardar_cambios)
    
    #solo muevo la imagen si existe
    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/" + str(id) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)
    
    
    mostrar_table_widget()#vuelvo a mostrar todos los libros
    
def borrar_libro(id):
    res = QMessageBox.question(MainWindow,"Info","Vas a borrar un registro de id: " + str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_libro(id)
        mostrar_table_widget()
    

def mostrar_inicio():
    ui.setupUi(MainWindow)
    
#fin definicion funciones

#inicio aplicacion principal:

app = QtWidgets.QApplication(sys.argv)#linea obligatoria para usar pyqt5
MainWindow = QtWidgets.QMainWindow()#crear una ventana principal con pyqt5

ui = ventana_principal.Ui_MainWindow()#creo el interfaz definido por ventana_principal.py
                                      #que es el archivo generado desde la consola a partir 
                                      #del archivo de diseño ventana_principal.ui
ui_registrar_libro = ventana_registrar_libro.Ui_MainWindow()#lo mismo pero para registrar libro
ui_listar_libros = ventana_listado_libros.Ui_MainWindow()#lo mismo pero para listar libros
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()
ui_ventana_editar_libro = ventana_editar_libro.Ui_MainWindow()
ui_ventana_ver_detalles_libro = ventana_ver_detalles_libro.Ui_MainWindow()

ui.setupUi(MainWindow)#todo lo que tiene el interfaz de la ventana principal lo pongo en el 
                      #MainWindow
#asignar las funciones a los submenús
ui.submenu_insertar_libro.triggered.connect(mostar_registro_libro)
ui.submenu_listar_libros.triggered.connect(mostrar_listado_libros)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_list_widget_libros.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_libros.triggered.connect(mostrar_table_widget)
                      
MainWindow.show()#mostrar la ventana principal de pyqt5
sys.exit(app.exec_())#cerrar la aplicacion cuando se cierra la ventana MainWindow