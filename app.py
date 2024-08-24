"""FastAPI entrypoint."""

import uvicorn
from fastapi import APIRouter, FastAPI, status
from fastapi.responses import Response
from mov_granada_api.exceptions.handler import add_handler
from mov_granada_api.routers.bus import router as bus_api
from mov_granada_api.routers.metro import router as metro_api

app = FastAPI(
    title="MovGranada API",
    description=("API para información de transportes urbanos de Granada"),
    version="0.1.0",
    contact={
        "name": "Miguel Ángel Fernández Gutiérrez",
        "url": "https://mianfg.me",
        "email": "hello@mianfg.me",
    },
)

add_handler(app)


@app.get("/")
async def health_check() -> Response:
    """Check API health."""
    return Response(status_code=status.HTTP_200_OK)


router = APIRouter()

router.include_router(bus_api, prefix="/bus", tags=["bus"])
router.include_router(metro_api, prefix="/metro", tags=["metro"])

app.include_router(router)


def run() -> None:
    """Run FastAPI via uvicorn."""
    uvicorn.run("app:app", host="localhost", port=8080, reload=True, workers=3)


# for development purposes
if __name__ == "__main__":
    run()
