"""Servicio para obtener información de paradas de bus."""

import requests
from bs4 import BeautifulSoup

from mov_granada_api.exceptions.exceptions import (
    ParadaNotFoundError,
    ParadaRequestError,
)
from mov_granada_api.models.bus import ParadaBusModel, ProximoBusModel


def __get_url(num_parada: int) -> str:
    return (
        "https://www.transportesrober.com:9012/flotaenmovimiento/Transportes/"
        f"parada.aspx?idparada={num_parada}"
    )


def get_parada_bus(num_parada: int) -> ParadaBusModel:
    """Pedir información de parada de bus."""
    req = requests.get(__get_url(num_parada), timeout=5)

    if req.status_code != 200:  # noqa: PLR2004
        raise ParadaRequestError

    soup = BeautifulSoup(req.text, "lxml")
    entradas = soup.find("td", {"class": "tablacabecera"}).getText()

    if entradas == "Error":
        raise ParadaNotFoundError from None

    datos = soup.find_all("td", {"class": "tabla_campo_valor"})
    nombre = entradas.split(" - ")[0]
    proximos = []

    if len(datos) >= 3:  # noqa: PLR2004
        buses = [datos[i : i + 3] for i in range(0, len(datos), 3)]

        for bus in buses:
            bus = [col.getText().strip() for col in bus]  # noqa: PLW2901
            proximos.append(
                ProximoBusModel(
                    linea=bus[0],
                    destino=bus[1],
                    minutos=int(bus[2]) if bus[2] else 0,
                ),
            )

    return ParadaBusModel(nombre=nombre, proximos=proximos)
