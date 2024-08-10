from domain.road_hazard_service import RoadHazardService
from ui.requests.get_road_hazards_request_body import GetRoadHazardRequestBody
from ui.responses.get_road_hazards_response import (
    GetRoadHazardResponse,
    RoadHazardResponseItem,
)


class RoadHazardAppService:
    @classmethod
    def get_road_hazards(cls, request: GetRoadHazardRequestBody):
        hazards = RoadHazardService.get_road_hazards()

        hazard_items: list[RoadHazardResponseItem] = []
        for hazard in hazards:
            hazard_items.append(
                RoadHazardResponseItem(type=hazard.type, coordinate=hazard.coordinate)
            )

        return GetRoadHazardResponse(index=1, hazards=hazard_items)
