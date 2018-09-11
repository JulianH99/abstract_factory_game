from .base_builders import SpriteBuilder


class PlayerGroup:
    def __init__(self, builder: SpriteBuilder):
        self._builder = builder

    def build_player(self, gender, clan):
        self._builder.build_body(gender)
        self._builder.build_accessories(clan)

        (body, accessories) = self._builder.get_object()

        print(body, accessories)
        return body, accessories

