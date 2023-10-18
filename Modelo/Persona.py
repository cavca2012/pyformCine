class Persona():

    def __init__(self, firstName, middleName, lastName):
        self._firstName     = firstName
        self._middleName    = middleName
        self._lastName      = lastName

    @property
    def __str__(self):
        return "{0} {1} {2}".format(self._firstName, self._middleName, self._lastName)
