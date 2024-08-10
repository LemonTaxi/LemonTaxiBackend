from .hello import router as hello_router
from .road_hazard import router as road_hazard_router


def init_router(app):
    # Hello Junction Asia ! We Are LemonTaxi
    app.include_router(hello_router)

    # Road Hazard Router
    app.include_router(road_hazard_router)
