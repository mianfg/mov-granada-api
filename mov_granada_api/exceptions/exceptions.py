"""Excepciones."""


class BusGranadaAPIError(Exception):
    """Excepción general."""


class ParadaNotFoundError(BusGranadaAPIError):
    """Excepción para parada no encontrada."""


class ParadaRequestError(BusGranadaAPIError):
    """Excepción para errores con requests."""
