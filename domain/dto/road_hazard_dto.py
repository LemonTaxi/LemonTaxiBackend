import pydantic

from domain.const.road_hazard_type import RoadHazardType


class RoadHazardDTO(pydantic.BaseModel):
    type: RoadHazardType
    coordinates: list[float]
