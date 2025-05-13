import reflex as rx

class Incidencia(rx.Model, Table=True):
    """ Class Incidencias """
    nombre: str
    telefono: str
    direccion: str
    motivo: str
    usuario: str
    fecha: str
    status: str
    bitrix: str


