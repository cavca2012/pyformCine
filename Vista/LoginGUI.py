import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlLabel
from   pyforms.controls import ControlPassword

from Vista.CarteleraGUI import CarteleraGUI
from Vista.RegistrarGUI import RegistrarGUI


class LoginGUI(BaseWidget):

    def __init__(self):
        BaseWidget.__init__(self,'Iniciar sesion')
        #super().__init__(self,'Iniciar sesion')

        #Definition of the forms fields
        self._username   = ControlText("Usuario")
        self._password  = ControlPassword('Contraseña')
        self._button  = ControlButton('Iniciar Sesion')
        #self._label   = ControlLabel('_____________________________________')
        self._button2  = ControlButton('Registrar usuario')

        #Define the button action
        self._button.value = self.__buttonIniciar
        self._button2.value = self.__buttonRegistrar

    def __buttonIniciar(self):
        if self._username.value == 'admin' and self._password.value == 'admin':
            cartelera_gui = CarteleraGUI()
            cartelera_gui.show()
            cartelera_gui.setGeometry(300,300,400,200)
        else:
            print("Usuario o contraseña incorrectas")

    def __buttonRegistrar(self):
        registrar_gui = RegistrarGUI()
        registrar_gui.show()
        registrar_gui.setGeometry(300,300,400,200)

#Execute the application
if __name__ == "__main__":
    pyforms.start_app( LoginGUI , geometry=(300,300,400,200))
