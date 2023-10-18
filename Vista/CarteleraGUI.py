import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlLabel

class CarteleraGUI(BaseWidget):

    def __init__(self):
        BaseWidget.__init__(self,'Inscribir usuario')

        #Definition of the forms fields
        self._lavelUno   = ControlLabel("Hola")
        self._firstname  = ControlText('First name')
        self._middlename = ControlText('Middle name')
        self._lastname   = ControlText('Lastname name')
        self._fullname   = ControlText('Full name')
        self._button     = ControlButton('Press this button')

        #Define the button action
        self._button.value = self.__buttonAction

    def __buttonAction(self):
        """Button action event"""
        self._fullname.value = self._firstname.value +" "+ self._middlename.value + \
        " "+ self._lastname.value

#Execute the application
if __name__ == "__main__":
    pyforms.start_app( Cartelera , geometry=(300, 200, 400, 500))
