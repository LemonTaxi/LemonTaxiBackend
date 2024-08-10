import pydantic

from domain.const.road_hazard_type import RoadHazardType
from domain.const.route_type import RouteType


class RoadHazardResponseItem(pydantic.BaseModel):
    type: RoadHazardType
    coordinate: list[float]
    coordinates: list[list[float]]


class RoadHazardRouteItem(pydantic.BaseModel):
    id: str
    route_type: RouteType
    hazards: list[RoadHazardResponseItem]


class GetRoadHazardResponse(pydantic.BaseModel):
    routes: list[RoadHazardRouteItem]
