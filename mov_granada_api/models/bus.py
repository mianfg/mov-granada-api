"""CategoryModel."""

from pydantic import Field

from mov_granada_api.models.base import BusGranadaAPIBaseModel


class ProximoBusModel(BusGranadaAPIBaseModel):
    """Modelo para próximo autobús."""

    linea: str = Field(description="Código de línea del autobús")
    destino: str = Field(description="Nombre del destino")
    minutos: int = Field(
        description="Número de minutos hasta que llegue el bus", ge=0,
    )


class ParadaBusModel(BusGranadaAPIBaseModel):
    """Modelo para parada."""

    nombre: str = Field(description="Nombre de la parada")
    proximos: list[ProximoBusModel] = Field(
        description="Lista de próximos autobuses",
    )
