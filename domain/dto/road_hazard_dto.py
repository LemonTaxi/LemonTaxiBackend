import pydantic

from domain.const.road_hazard_type import RoadHazardType


class RoadHazardDTO(pydantic.BaseModel):
    type: RoadHazardType
    coordinate: list[float]


class PathDTO(pydantic.BaseModel):
    coordinate_1: list[float]
    coordinate_2: list[float]

    def __eq__(self, other):
        return (
            self.coordinate_1 == other.coordinate_1
            and self.coordinate_2 == other.coordinate_2
        ) or (
            self.coordinate_1 == other.coordinate_2
            and self.coordinate_2 == other.coordinate_1
        )
