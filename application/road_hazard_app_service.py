from domain.const.road_hazard_type import RoadHazardType
from ui.requests.get_road_hazards_request_body import GetRoadHazardRequestBody
from ui.responses.get_road_hazards_response import (
    GetRoadHazardResponse,
    RoadHazardResponseItem,
)


class RoadHazardAppService:
    @classmethod
    def get_road_hazards(cls, request: GetRoadHazardRequestBody):
        hazards: list[RoadHazardResponseItem] = []
        for hazard_type in list(RoadHazardType):
            hazards.append(RoadHazardResponseItem(type=hazard_type, coordinate=[1, 1]))

        return GetRoadHazardResponse(index=1, hazards=hazards)
