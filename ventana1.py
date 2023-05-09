import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QDialog, \
    QDialogButtonBox, QVBoxLayout, QApplication, QDesktopWidget
from PyQt5 import QtGui


class Ventana1(QMainWindow):


    # Hacer el metodo de contruccion de la ventana:
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Poner el titulo
        self.setWindowTitle("Formulario de Registro")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/pix.jpg'))

        # Establecemos las propiedades de ancho y alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/pac.jpg')

        # Definimos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en layaut horizontal:
        self.horizontal = QHBoxLayout()
        # Le ponemos las márgenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)



        # ------    PONER AL FINAL  ------

        # Indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())
