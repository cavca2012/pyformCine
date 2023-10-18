from Modelo.Persona import Persona


class Usuario(Persona):

    def __init__(self, firstName, middleName, lastName, username, password):
        super().__init__(firstName, middleName, lastName)
        self._username    = username
        self._password      = password

    @property
    def __str__(self):
        return self._username + self._password
