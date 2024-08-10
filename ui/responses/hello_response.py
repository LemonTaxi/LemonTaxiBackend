import pydantic


class PlayItem(pydantic.BaseModel):
    name: str
    role: str


class HelloResponse(pydantic.BaseModel):
    team_name: str
    players: list[PlayItem]
