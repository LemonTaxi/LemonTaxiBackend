from ui.responses.hello_response import HelloResponse, PlayItem


class HelloAppService:
    @classmethod
    def hello(cls) -> HelloResponse:
        players: list[PlayItem] = [
            PlayItem(name="MEL", role="PO"),
            PlayItem(name="AVORY", role="PD"),
            PlayItem(name="FINN", role="ENG"),
            PlayItem(name="HAN", role="ENG"),
            PlayItem(name="IAN", role="ENG"),
        ]
        return HelloResponse(team_name="LemonTaxi", players=players)
