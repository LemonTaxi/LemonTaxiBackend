import pydantic

from domain.const.road_hazard_type import RoadHazardType


class RoadHazardResponseItem(pydantic.BaseModel):
    type: RoadHazardType
    coordinate: list[list[float]]


class GetRoadHazardResponse(pydantic.BaseModel):
    index: int
    hazards: list[RoadHazardResponseItem]
