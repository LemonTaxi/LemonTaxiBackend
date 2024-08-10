import random

from domain.const.road_hazard_type import RoadHazardType
from domain.dto.road_hazard_dto import RoadHazardDTO, PathDTO
from ui.requests.get_road_hazards_request_body import RouteRequest


class RoadHazardService:
    @classmethod
    def get_road_hazards(cls, routes: list[RouteRequest]) -> list[RoadHazardDTO]:
        # NOTE: 경로 상 겹치지 않는 Coordinates에 Hazard 임의 생성
        return cls.__generate_fake_hazards(safe_route=routes[0], unsafe_route=routes[1])

    @classmethod
    def __generate_fake_hazards(
        cls, safe_route: RouteRequest, unsafe_route: RouteRequest
    ) -> list[RoadHazardDTO]:
        safe_paths = cls.__transform_coordinates_to_path(
            safe_route.geometry.coordinates
        )
        unsafe_paths = cls.__transform_coordinates_to_path(
            unsafe_route.geometry.coordinates
        )

        not_duplicated_unsafe_path: list[PathDTO] = []
        for unsafe_path in unsafe_paths:
            is_duplicated = False
            for safe_path in safe_paths:
                if unsafe_path == safe_path:
                    is_duplicated = True
                    continue
            if not is_duplicated:
                not_duplicated_unsafe_path.append(unsafe_path)

        path_having_hazard_indexes = random.sample(
            range(len(not_duplicated_unsafe_path) - 1),
            len(not_duplicated_unsafe_path) // 60,
        )
        print(path_having_hazard_indexes)

        road_hazard: list[RoadHazardDTO] = []
        for index in path_having_hazard_indexes:
            path = not_duplicated_unsafe_path[index]

            type = RoadHazardType(random.randint(0, 1))
            coordinate = [
                (path.coordinate_1[0] + path.coordinate_2[0]) / 2,
                (path.coordinate_1[1] + path.coordinate_2[1]) / 2,
            ]

            road_hazard.append(RoadHazardDTO(type=type, coordinate=coordinate))

        return road_hazard

    @classmethod
    def __transform_coordinates_to_path(
        cls, coordinates: list[list[float]]
    ) -> list[PathDTO]:
        path: list[PathDTO] = []
        for index in range(len(coordinates) - 1):
            path.append(
                PathDTO(
                    coordinate_1=coordinates[index], coordinate_2=coordinates[index + 1]
                )
            )

        return path
