from fastapi import APIRouter

from application.hello_app_service import HelloAppService

router = APIRouter()


@router.get("/hello")
def hello():
    return HelloAppService.hello()
