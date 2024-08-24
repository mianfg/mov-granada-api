"""Exception handling."""

from fastapi import FastAPI, HTTPException, Request

from mov_granada_api.exceptions.exceptions import (
    ParadaNotFoundError,
    ParadaRequestError,
)


async def __exception_handler(request: Request, exc: Exception) -> None:  # noqa: ARG001
    if isinstance(exc, ParadaNotFoundError):
        raise HTTPException(
            status_code=404,
            detail="Parada no encontrada",
        )
    if isinstance(exc, ParadaRequestError):
        raise HTTPException(
            status_code=500,
            detail="Hubo un error con la petición",
        )

    raise exc


def add_handler(app: FastAPI) -> None:
    """Add exception handlers to FastAPI."""
    app.add_exception_handler(ParadaNotFoundError, __exception_handler)
    app.add_exception_handler(ParadaRequestError, __exception_handler)
