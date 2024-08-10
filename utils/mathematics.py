import math

import pydantic

EARTH_RADIUS = 6371.0  # 지구 반지름(km)


class Coordinate(pydantic.BaseModel):
    longitude: float
    latitude: float


class MathematicsUtil:
    @classmethod
    def is_point_near_great_circle(
        cls,
        point_1: Coordinate,
        point_2: Coordinate,
        point_3: Coordinate,
        epsilon: float = 0.00000005,
    ):
        distance = cls.__get_point_to_great_circle_distance(point_1, point_2, point_3)
        return distance <= epsilon

    @classmethod
    def __get_point_to_great_circle_distance(
        cls,
        point_1: Coordinate,
        point_2: Coordinate,
        point_3: Coordinate,
    ):
        # 각 점 사이의 대원 거리
        d12 = cls.__haversine(point_1, point_2)
        d13 = cls.__haversine(point_1, point_3)
        d23 = cls.__haversine(point_2, point_3)

        # 각 빗변으로 헤론 공식을 사용해 삼각형 넓이 계산
        area = cls.__heron(d12, d13, d23)

        distance_to_line = (2 * area) / d12

        return distance_to_line

    @classmethod
    def __haversine(cls, point_1: Coordinate, point_2: Coordinate) -> float:
        delta_latitude = math.radians(point_2.latitude - point_1.latitude)
        delta_longitude = math.radians(point_2.longitude - point_1.longitude)
        latitude_1 = math.radians(point_1.latitude)
        latitude_2 = math.radians(point_2.latitude)

        value = (
            math.sin(delta_latitude / 2) ** 2
            + math.cos(latitude_1)
            * math.cos(latitude_2)
            * math.sin(delta_longitude / 2) ** 2
        )
        value = 2 * math.atan2(math.sqrt(value), math.sqrt(1 - value))
        spherical_distance = EARTH_RADIUS * value

        return spherical_distance

    @classmethod
    def __heron(cls, d12: float, d13: float, d23: float) -> float:
        s = (d12 + d13 + d23) / 2
        area = math.sqrt(s * (s - d12) * (s - d13) * (s - d23))

        return area
