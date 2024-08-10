import dotenv
from fastapi import FastAPI

from ui.router import init_router

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="Lemonbase Taxi",
        version="0.0.1",
    )

    init_router(app)

    return app


app = create_app()
