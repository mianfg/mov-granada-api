"""Utilidades para VCARD. Usado en Apple Shortcuts."""

import csv
import os

from mov_granada_api.models.bus import ParadaBusModel
from mov_granada_api.models.metro import ParadaMetroModel


def __get_vcard_dict(name: str, key: str, cols: list[str]) -> dict:
    vcard_dict = {}

    with open(
        os.path.join(os.path.dirname(__file__), f"../data/{name}.csv"),
    ) as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            vcard_dict[row[key]] = {col: row[col] for col in cols}

    return vcard_dict


vcard_bus_dict = __get_vcard_dict("bus", "linea", ["nombre", "id", "base64"])
vcard_metro_dict = __get_vcard_dict("metro", "parada", ["base64"])


def __minutos_to_str(minutos: int) -> str:
    if minutos == 0:
        return "Inminente"
    if minutos == 1:
        return "1 minuto"
    return f"{minutos} minutos"


def make_vcard_bus(parada: ParadaBusModel) -> str:
    """Crear VCARD a partir de ParadaBusModel."""
    vcard_str = ""
    for proximo in parada.proximos:
        info = vcard_bus_dict[proximo.linea]
        vcard_str += (
            "BEGIN:VCARD\n"
            "VERSION:3.0\n"
            f"N;CHARSET=utf-8:{__minutos_to_str(proximo.minutos)}\n"
            f"NOTE:{info['id']}\n"
            f"PHOTO;BASE64:{info['base64']}\n"
            f"ORG:Destino: {proximo.destino}\n"
            "END:VCARD\n"
        )

    return vcard_str


def make_vcard_metro(parada: ParadaMetroModel) -> str:
    """Crear VCARD a partir de ParadaBusModel."""
    vcard_str = ""
    for proximo in parada.proximos:
        info = vcard_metro_dict[proximo.direccion]
        vcard_str += (
            "BEGIN:VCARD\n"
            "VERSION:3.0\n"
            f"N;CHARSET=utf-8:{__minutos_to_str(proximo.minutos)}\n"
            f"PHOTO;BASE64:{info['base64']}\n"
            f"ORG:Dirección: {proximo.direccion}\n"
            "END:VCARD\n"
        )

    return vcard_str
