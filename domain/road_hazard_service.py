from domain.const.road_hazard_type import RoadHazardType
from domain.dto.road_hazard_dto import RoadHazardDTO


class RoadHazardService:
    @classmethod
    def get_road_hazards(cls) -> list[RoadHazardDTO]:
        lane_invisible_hazard_coordinate = [129.377144, 36.024051]
        crack_hazard_coordinate = [129.372393, 36.039827]

        return [
            RoadHazardDTO(
                type=RoadHazardType.LANE_INVISIBLE,
                coordinate=lane_invisible_hazard_coordinate,
            ),
            RoadHazardDTO(
                type=RoadHazardType.CRACK, coordinate=crack_hazard_coordinate
            ),
        ]
