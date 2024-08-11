from domain.const.route_type import RouteType
from domain.dto.road_hazard_dto import RoadHazardDTO
from domain.road_hazard_service import RoadHazardService
from ui.requests.get_road_hazards_request_body import GetRoadHazardRequestBody
from ui.responses.get_road_hazards_response import (
    GetRoadHazardResponse,
    RoadHazardResponseItem,
    RoadHazardRouteItem,
)
from utils.mathematics import Coordinate, MathematicsUtil


class RoadHazardAppService:
    @classmethod
    def get_road_hazards(cls, request: GetRoadHazardRequestBody):
        hazards = RoadHazardService.get_road_hazards(request.routes)

        route_items: list[RoadHazardRouteItem] = []
        for route in request.routes:
            coordinates = route.geometry.coordinates
            hazard_items: list[RoadHazardResponseItem] = cls.__find_hazards_on_route(
                coordinates=coordinates, hazards=hazards
            )

            route_type = RouteType.UNSAFE if hazard_items else RouteType.SAFE
            route_items.append(
                RoadHazardRouteItem(
                    id=route.id, route_type=route_type, hazards=hazard_items
                )
            )

        return GetRoadHazardResponse(routes=route_items)

    @classmethod
    def __find_hazards_on_route(
        cls, coordinates: list[list[float]], hazards: list[RoadHazardDTO]
    ) -> list[RoadHazardResponseItem]:
        hazard_items: list[RoadHazardResponseItem] = []
        for index in range(len(coordinates) - 1):
            first_point = Coordinate(
                longitude=coordinates[index][0], latitude=coordinates[index][1]
            )
            second_point = Coordinate(
                longitude=coordinates[index + 1][0],
                latitude=coordinates[index + 1][1],
            )
            for hazard in hazards:
                hazard_point = Coordinate(
                    longitude=hazard.coordinate[0],
                    latitude=hazard.coordinate[1],
                )

                if MathematicsUtil.is_point_near_great_circle(
                    first_point, second_point, hazard_point
                ):
                    hazard_coordinates = cls.__get_coordinates(index, coordinates)
                    hazard_items.append(
                        RoadHazardResponseItem(
                            type=hazard.type,
                            coordinate=[
                                hazard_point.longitude,
                                hazard_point.latitude,
                            ],
                            coordinates=hazard_coordinates,
                        )
                    )

        return hazard_items

    @classmethod
    def __get_coordinates(
        cls, index: int, coordinates: list[list[float]]
    ) -> list[list[float]]:
        if index < 2 or index > len(coordinates) - 2:
            return [coordinates[index], coordinates[index + 1]]

        # NOTE: 화면에서 시각적으로 표현해주기 위해 주변 coordinate를 포함
        return [
            coordinates[index - 2],
            coordinates[index - 1],
            coordinates[index],
            coordinates[index + 1],
            coordinates[index + 2],
        ]
