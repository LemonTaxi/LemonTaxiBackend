import dotenv
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from ui.router import init_router

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def create_app() -> FastAPI:
    origins = ["*"]
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]

    app = FastAPI(
        debug=True,
        middleware=middleware,
        title="Lemonbase Taxi",
        version="0.0.1",
    )

    init_router(app)

    return app


app = create_app()
