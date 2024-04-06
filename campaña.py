
from datetime import date
from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoError

class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios=None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio  # se asume tipo date
        self.fecha_termino = fecha_termino  # se asume tipo date
        self._anuncios = anuncios if anuncios is not None else []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres permitidos.")
        self._nombre = valor


    @property
    def anuncios(self):
        return self._anuncios


    def agregar_anuncio(self, anuncio):
        if isinstance(anuncio, Anuncio):
            self._anuncios.append(anuncio)
        else:
            raise TypeError("Solo se pueden agregar instancias de Anuncio o de sus subclases.")

    def __str__(self):
        conteo_video = sum(isinstance(anuncio, Video) for anuncio in self._anuncios)
        conteo_display = sum(isinstance(anuncio, Display) for anuncio in self._anuncios)
        conteo_social = sum(isinstance(anuncio, Social) for anuncio in self._anuncios)

        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Anuncios: {conteo_video} Video, {conteo_display} Display, {conteo_social} Social")

