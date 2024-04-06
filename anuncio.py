# anuncio.py
from error import SubTipoInvalidoError

class Anuncio:
    FORMATO = None
    SUB_TIPOS = ()

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self._ancho = self._validar_dimension(ancho)
        self._alto = self._validar_dimension(alto)
        self._url_archivo = url_archivo
        self._url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, valor):
        self._url_archivo = valor

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, valor):
        self._url_clic = valor

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        if self.FORMATO and valor in self.SUB_TIPOS:
            self._sub_tipo = valor
        else:
            raise SubTipoInvalidoError(f"Subtipo '{valor}' no válido para el formato {self.FORMATO}")

    @staticmethod
    def _validar_dimension(valor):
        return max(valor, 1)

    def comprimir_anuncio(self):
        raise NotImplementedError

    def redimensionar_anuncio(self):
        raise NotImplementedError


class Video(Anuncio):
    FORMATO = 'Video'
    SUB_TIPOS = ('instream', 'outstream')

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = max(valor, 5)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = 'Display'
    SUB_TIPOS = ('tradicional', 'native')

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = 'Social'
    SUB_TIPOS = ('facebook', 'linkedin')

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
