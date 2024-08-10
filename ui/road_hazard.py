from fastapi import APIRouter

from ui.requests.get_road_hazards_request_body import GetRoadHazardRequestBody
from application.road_hazard_app_service import RoadHazardAppService

router = APIRouter()


@router.post("/road-hazards")
def get_road_hazards(request: GetRoadHazardRequestBody):
    return RoadHazardAppService.get_road_hazards(request).dict()
