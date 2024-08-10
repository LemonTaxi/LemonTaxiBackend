import pydantic


class RouteGeometry(pydantic.BaseModel):
    coordinates: list[float]


class RouteRequest(pydantic.BaseModel):
    id: str
    geometry: RouteGeometry


class GetRoadHazardRequestBody(pydantic.BaseModel):
    routes: list[RouteRequest]
