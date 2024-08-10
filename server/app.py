import dotenv
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

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


# handle CORS preflight requests
@app.options("/{rest_of_path:path}")
async def preflight_handler(request: Request, rest_of_path: str) -> Response:
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
    return response


# set CORS headers
@app.middleware("http")
async def add_CORS_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
    return response
