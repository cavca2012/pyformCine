class Pelicula(object):

    def __init__(self, titulo, portadaURL, director, clasificacion, sinopsis):
        self._titulo        = titulo
        self._portadaURL    = portadaURL
        self._director      = director
        self._clasificacion = clasificacion
        self._sinopsis      = sinopsis

    def descripcion(self):
        return (self._portadaURL,self._titulo,self._sinopsis)
