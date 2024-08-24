"""CategoryModel."""

from pydantic import Field

from mov_granada_api.models.base import BusGranadaAPIBaseModel


class ProximoMetroModel(BusGranadaAPIBaseModel):
    """Modelo para próximo autobús."""

    direccion: str = Field(description="Dirección de tren")
    minutos: int = Field(
        description="Número de minutos hasta que llegue el tren",
        ge=0,
    )


class ParadaMetroModel(BusGranadaAPIBaseModel):
    """Modelo para parada."""

    nombre: str = Field(description="Nombre de la parada")
    proximos: list[ProximoMetroModel] = Field(
        description="Lista de próximos autobuses",
    )
