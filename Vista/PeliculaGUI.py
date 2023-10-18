import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlText
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlCombo
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlTextArea
from Modelo.Pelicula import Pelicula
from Vista.PersonaGUI import PersonaGUI


class PeliculaGUI(BaseWidget):

    def __init__(self):
        super().__init__(self,'Nueva Pelicula')

        #Definition of the forms fields
        self._campoTitulo        = ControlText('Titulo')
        self._campoPortadaURL    = ControlFile('Portada')
        self._campoDirector      = ControlText('Director')
        self._campoClasificacion = ControlCombo('Clasificaciones')
        self._campoSinopsis      = ControlTextArea('Sinopsis')
        self._campoBotRegistrar  = ControlButton('Registrar Película')
        self._campoClasificacion.add_item('Infantiles (AA)', 'AA')
        self._campoClasificacion.add_item('Todo publico (A)', 'A')
        self._campoClasificacion.add_item('Adolecentes (B)', 'B')
        self._campoClasificacion.add_item('Adultos +18 (C)', 'C')
        self._campoClasificacion.add_item('Adultos por Contenido explicito (D)', 'D')

        #Define the button action
        self._campoBotRegistrar.value = self.__buttonAction

    def __buttonAction(self):
        pel = Pelicula(self._campoTitulo.value, self._campoPortadaURL.value, self._campoDirector.value, self._campoClasificacion.value, self._campoSinopsis.value)
        print(pel.descripcion())
        self.hide()
        per = PersonaGUI()
        per.show()


#Execute the application
if __name__ == "__main__":
    pelgui = PeliculaGUI()
    pelgui.show()
    pyforms.start_app()
    #pyforms.start_app( PeliculaGUI, geometry=(500,300,300,400) )
