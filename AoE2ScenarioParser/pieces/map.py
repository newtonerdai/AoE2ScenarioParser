from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.pieces.structs.terrain import TerrainStruct


class MapPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever('separator_1', DataType("2")),
            Retriever('unknown_string', DataType("str16")),
            Retriever('separator_2', DataType("2")),
            Retriever('map_color_mood', DataType("str16")),
            Retriever('collide_and_correct', DataType("u8")),
            # [VERSION CHANGE] ADDED in 1.36 > 1.37
            Retriever('villager_force_drop', DataType("u8"), set_repeat="1 if '{scenario_version}' == '1.37' else 0"),
            Retriever('player_1_camera_y', DataType("s32")),
            Retriever('player_1_camera_x', DataType("s32")),
            Retriever('ai_type', DataType("s8")),
            Retriever('map_width', DataType("s32"), save_as="map_width"),
            Retriever('map_height', DataType("s32"), save_as="map_height"),
            Retriever('terrain_data', DataType(TerrainStruct), set_repeat="{map_width}*{map_height}"),
        ]

        super().__init__("Map", retrievers, parser_obj, data=data)

    @staticmethod
    def defaults():
        defaults = {
            'separator_1': b'`\n',
            'unknown_string': '',
            'separator_2': b'`\n',
            'map_color_mood': '',
            'collide_and_correct': 0,
            'villager_force_drop': [0],
            'player_1_camera_y': -559026163,
            'player_1_camera_x': 2,
            'ai_type': 1,
            'map_width': 120,
            'map_height': 120,
            'terrain_data': [TerrainStruct(data=[0, 0, 0, b'\xff\xff', -1]) for _ in range(120*120)],
        }
        return defaults
