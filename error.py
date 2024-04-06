
class SubTipoInvalidoError(Exception):
    """Excepción lanzada cuando el subtipo de anuncio es inválido."""
    pass

class LargoExcedidoError(Exception):
    """Excepción lanzada cuando el nombre de la campaña excede el largo máximo permitido."""
    pass
