from domain.const.road_hazard_type import RoadHazardType
from domain.dto.road_hazard_dto import RoadHazardDTO


class RoadHazardService:
    @classmethod
    def get_road_hazards(cls) -> list[RoadHazardDTO]:
        lane_invisible_hazard_coordinates = [129.377144, 36.024051]
        crack_hazard_coordinates = [129.370209, 36.040094]

        return [
            RoadHazardDTO(
                type=RoadHazardType.LANE_INVISIBLE,
                coordinates=lane_invisible_hazard_coordinates,
            ),
            RoadHazardDTO(
                type=RoadHazardType.CRACK, coordinates=crack_hazard_coordinates
            ),
        ]
