import cv2
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlImage
from PyQt5.QtCore import QTimer
from pyforms import start_app
from Vista.LoginGUI import LoginGUI


class Bienvenida(BaseWidget):
    def __init__(self):
        super().__init__('Bienvenido')
        #self.label = ControlText('Titulo1')
        self.image = ControlImage("Bienvenido")
        #self.abrir = ControlButton('Abrir ventana2')
        self.image.value = cv2.imread('img/bienvenido.jpg')

        #self.abrir.value = self.__buttonAction
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__abrirCartelera)
        self.timer.start(1000)

    def __abrirCartelera(self):
        self.timer.stop()

        login_gui = LoginGUI()
        login_gui.show()
        login_gui.setGeometry(300,300,400,200)

if __name__ == '__main__':
    start_app(Bienvenida,geometry=(300,300,400,300))
