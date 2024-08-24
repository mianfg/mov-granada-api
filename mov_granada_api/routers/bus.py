"""Router para bus."""

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from mov_granada_api.models.bus import ParadaBusModel
from mov_granada_api.services.bus import get_parada_bus
from mov_granada_api.services.vcard import make_vcard_bus

router = APIRouter()


@router.get(
    "/{num_parada}",
    response_model=ParadaBusModel,
    response_description="Información de parada de bus",
)
async def bus(num_parada: int) -> ParadaBusModel:
    """Obtener información de parada de bus."""
    return get_parada_bus(num_parada)


@router.get(
    "/{num_parada}/vcard",
    response_class=PlainTextResponse,
    response_description="Información de parada de bus, en VCARD",
)
async def bus_vcard(num_parada: int) -> str:
    """Obtener información de parada de bus, en VCARD."""
    return make_vcard_bus(get_parada_bus(num_parada))
