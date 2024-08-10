import math

import pydantic

EARTH_RADIUS = 6371.0  # 지구 반지름 (킬로미터)


class Coordinate(pydantic.BaseModel):
    longitude: float
    latitude: float


class MathematicsUtil:
    @classmethod
    def haversine(cls, point_1: Coordinate, point_2: Coordinate) -> float:
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
    def point_to_great_circle_distance(
        cls,
        point_1: Coordinate,
        point_2: Coordinate,
        point_3: Coordinate,
    ):
        # 두 점 (lat1, lon1), (lat2, lon2) 사이의 대원 거리
        d12 = cls.haversine(point_1, point_2)

        # 두 점 각각에서 점 (lat3, lon3)과의 거리
        d13 = cls.haversine(point_1, point_3)
        d23 = cls.haversine(point_2, point_3)

        # 헤론의 공식을 사용하여 삼각형의 면적을 구하고 높이를 계산
        s = (d12 + d13 + d23) / 2
        area = math.sqrt(s * (s - d12) * (s - d13) * (s - d23))

        # 높이(거리) = (2 * 면적) / d12
        distance_to_line = (2 * area) / d12

        return distance_to_line

    @classmethod
    def is_point_near_great_circle(
        cls,
        point_1: Coordinate,
        point_2: Coordinate,
        point_3: Coordinate,
        epsilon: float = 0.002,
    ):
        distance = cls.point_to_great_circle_distance(point_1, point_2, point_3)
        return distance <= epsilon
