import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlLabel
from   pyforms.controls import ControlPassword

from Modelo.Usuario import Usuario
from Vista.CarteleraGUI import CarteleraGUI


class RegistrarGUI(BaseWidget):

    def __init__(self):
        BaseWidget.__init__(self,'Registrar usuario')
        #super().__init__(self,'Iniciar sesion')

        #Definition of the forms fields
        self._campoPNombre   = ControlText('Primer nombre')
        self._campoSNombre   = ControlText('Segundo nombre')
        self._campoApellidos = ControlText('Apellidos')
        self._username   = ControlText("Usuario")
        self._password  = ControlPassword('Contraseña')
        self._password2  = ControlPassword('Confirmen la contraseña')
        self._button  = ControlButton('Registrar usuario')

        #Define the button action
        self._button.value = self.__buttonRegistrar

    def __buttonRegistrar(self):
        user = Usuario(self._campoPNombre.value, self._campoSNombre.value, self._campoApellidos.value, self._username.value, self._password.value)
        print(user)

#Execute the application
if __name__ == "__main__":
    pyforms.start_app( RegistrarGUI , geometry=(300,300,400,200))
