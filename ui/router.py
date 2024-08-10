from .hello import router as hello_router


def init_router(app):
    app.include_router(hello_router)
