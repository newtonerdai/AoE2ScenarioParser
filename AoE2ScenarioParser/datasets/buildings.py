from enum import Enum


class BuildingInfo(Enum):
    @property
    def ID(self):
        return self.value[0]

    @classmethod
    def from_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid id value")
        for x in cls._member_map_.values():
            if x.value[0] == value:
                return x
        raise ValueError(f"{value} is not a valid id value")

    @property
    def ICON_ID(self):
        return self.value[1]

    @classmethod
    def from_icon_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_icon_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid icon_id value")
        for x in cls._member_map_.values():
            if x.value[1] == value:
                return x
        raise ValueError(f"{value} is not a valid icon_id value")

    @property
    def DEAD_ID(self):
        return self.value[2]

    @classmethod
    def from_dead_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_dead_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid dead_id value")
        for x in cls._member_map_.values():
            if x.value[2] == value:
                return x
        raise ValueError(f"{value} is not a valid dead_id value")

    @property
    def IS_GAIA_ONLY(self):
        return self.value[3]

    @staticmethod
    def gaia_only():
        result = []
        for x in BuildingInfo:
            if x.IS_GAIA:
                result.append(x)
        return result

    @staticmethod
    def non_gaia():
        result = []
        for x in BuildingInfo:
            if not x.IS_GAIA:
                result.append(x)
        return result

    RUINS = 345, -1, -1, True
    AACHEN_CATHEDRAL = 1622, 37, 1517, False
    AMPHITHEATRE = 251, 58, 1514, False
    AQUEDUCT = 231, 52, 1522, False
    ARCH_OF_CONSTANTINE = 899, 37, 1485, False
    ARCHERY_RANGE = 87, 0, 1415, False
    ARMY_TENT_A = 1196, 76, 1467, False
    ARMY_TENT_B = 1197, 76, 1468, False
    ARMY_TENT_C = 1198, 77, 1469, False
    ARMY_TENT_D = 1199, 77, 1470, False
    ARMY_TENT_E = 1200, 77, 1471, False
    BARRACKS = 12, 2, 1402, False
    BLACKSMITH = 103, 4, 1419, False
    BOMBARD_TOWER = 236, 42, 1439, False
    BRIDGE_A_BOTTOM = 607, -1, 144, False
    BRIDGE_A_BROKEN_BOTTOM = 740, -1, 144, False
    BRIDGE_A_BROKEN_TOP = 739, -1, 144, False
    BRIDGE_A_CRACKED = 738, -1, 144, False
    BRIDGE_A_MIDDLE = 606, -1, 144, False
    BRIDGE_A_TOP = 605, -1, 144, False
    BRIDGE_B_BOTTOM = 610, -1, 144, False
    BRIDGE_B_BROKEN_BOTTOM = 743, -1, 144, False
    BRIDGE_B_BROKEN_TOP = 742, -1, 144, False
    BRIDGE_B_CRACKED = 741, -1, 144, False
    BRIDGE_B_MIDDLE = 609, -1, 144, False
    BRIDGE_B_TOP = 608, -1, 144, False
    BRIDGE_C_BOTTOM = 1206, -1, 144, False
    BRIDGE_C_BROKEN_BOTTOM = 1212, -1, 144, False
    BRIDGE_C_BROKEN_TOP = 1211, -1, 144, False
    BRIDGE_C_CRACKED = 1210, -1, 144, False
    BRIDGE_C_MIDDLE = 1205, -1, 144, False
    BRIDGE_C_TOP = 1204, -1, 144, False
    BRIDGE_D_BOTTOM = 1209, -1, 144, False
    BRIDGE_D_BROKEN_BOTTOM = 1215, -1, 144, False
    BRIDGE_D_BROKEN_TOP = 1214, -1, 144, False
    BRIDGE_D_CRACKED = 1213, -1, 144, False
    BRIDGE_D_MIDDLE = 1208, -1, 144, False
    BRIDGE_D_TOP = 1207, -1, 144, False
    BRIDGE_E_BOTTOM = 1552, -1, 144, False
    BRIDGE_E_BROKEN_BOTTOM = 1558, -1, 144, False
    BRIDGE_E_BROKEN_TOP = 1557, -1, 144, False
    BRIDGE_E_CRACKED = 1556, -1, 144, False
    BRIDGE_E_MIDDLE = 1551, -1, 144, False
    BRIDGE_E_TOP = 1550, -1, 144, False
    BRIDGE_F_BOTTOM = 1555, -1, 144, False
    BRIDGE_F_BROKEN_BOTTOM = 1561, -1, 144, False
    BRIDGE_F_BROKEN_TOP = 1560, -1, 144, False
    BRIDGE_F_CRACKED = 1559, -1, 144, False
    BRIDGE_F_MIDDLE = 1554, -1, 144, False
    BRIDGE_F_TOP = 1553, -1, 144, False
    CASTLE = 82, 7, 1430, False
    CATHEDRAL = 599, 11, 1480, False
    CHAIN_WEST_TO_EAST = 1398, 72, 144, False
    CHAIN_SOUTHWEST_TO_NORTHEAST = 1396, 72, 144, False
    CHAIN_NORTH_TO_SOUTH = 1399, 72, 144, False
    CHAIN_NORTHWEST_TO_SOUTHEAST = 1397, 72, 144, False
    CITY_GATE_WEST_TO_EAST = 1587, 36, 1512, False
    CITY_GATE_SOUTHWEST_TO_NORTHEAST = 1579, 36, 1510, False
    CITY_GATE_NORTH_TO_SOUTH = 1591, 36, 1513, False
    CITY_GATE_NORTHWEST_TO_SOUTHEAST = 1583, 36, 1511, False
    CITY_WALL = 370, 31, 143, False
    COLOSSEUM = 263, 58, 1520, False
    DOCK = 45, 13, -1, False
    DORMITION_CATHEDRAL = 1369, 37, 1493, False
    FARM = 50, 35, 357, False
    FEITORIA = 1021, 53, 1446, False
    FENCE = 1062, 30, 1065, False
    FIRE_TOWER = 190, 26, 1438, False
    FISH_TRAP = 199, 41, 278, False
    FORTIFIED_PALISADE_WALL = 119, 30, 143, False
    FORTIFIED_TOWER = 1102, 45, 1444, False
    FORTIFIED_WALL = 155, 31, 1509, False
    FORTRESS = 33, 8, 1486, False
    GATE_NORTHWEST_TO_SOUTHEAST = 88, 36, 1501, False
    GATE_WEST_TO_EAST = 659, 36, 1502, False
    GATE_SOUTHWEST_TO_NORTHEAST = 64, 36, 1500, False
    GATE_NORTH_TO_SOUTH = 667, 36, 1503, False
    GOL_GUMBAZ = 1217, 37, 1487, False
    GUARD_TOWER = 234, 25, 1437, False
    HARBOR = 1189, 56, -1, False
    HOUSE = 70, 34, 1403, False
    HUT_A = 1082, 75, 1455, False
    HUT_B = 1083, 75, 1456, False
    HUT_C = 1084, 74, 1457, False
    HUT_D = 1085, 75, 1458, False
    HUT_E = 1086, 75, 1459, False
    HUT_F = 1087, 75, 1460, False
    HUT_G = 1088, 75, 1461, False
    KEEP = 235, 26, 1438, False
    KREPOST = 1251, 55, 1479, False
    LUMBER_CAMP = 562, 40, 1409, False
    MARKET = 84, 16, 1422, False
    MILL = 68, 19, 1404, False
    MINING_CAMP = 584, 39, 1410, False
    MONASTERY = 104, 10, 1421, False
    MONUMENT = 826, 37, -1, False
    OUTPOST = 598, 38, 1405, False
    PALISADE_GATE_SOUTHWEST_TO_NORTHEAST = 793, 44, 1441, False
    PALISADE_GATE_WEST_TO_EAST = 797, 44, 1442, False
    PALISADE_GATE_NORTHWEST_TO_SOUTHEAST = 789, 44, 1440, False
    PALISADE_GATE_NORTH_TO_SOUTH = 801, 44, 1443, False
    PALISADE_WALL = 72, 30, 1407, False
    PYRAMID = 689, 57, 1515, False
    QUIMPER_CATHEDRAL = 872, 37, 1489, False
    RICE_FARM = 1187, 35, 1188, False
    ROCK_CHURCH = 1378, 341, -1, False
    SANCHI_STUPA = 1216, 37, 1490, False
    SANKORE_MADRASAH = 1367, 37, 1491, False
    SEA_GATE_SOUTHWEST_TO_NORTHEAST = 1379, 71, -1, False
    SEA_GATE_NORTH_TO_SOUTH = 1391, 71, -1, False
    SEA_GATE_WEST_TO_EAST = 1387, 71, -1, False
    SEA_GATE_NORTHWEST_TO_SOUTHEAST = 1383, 71, -1, False
    SEA_TOWER = 785, 25, -1, False
    SEA_WALL = 788, 30, -1, False
    SHRINE = 1264, 12, 1483, False
    SIEGE_WORKSHOP = 49, 22, 1425, False
    STABLE = 101, 23, 1417, False
    STONE_WALL = 117, 31, 1508, False
    STORAGE = 1081, 59, 1484, False
    TEMPLE_OF_HEAVEN = 637, 11, 1481, False
    TENT_A = 1097, 78, 1462, False
    TENT_B = 1098, 83, 1463, False
    TENT_C = 1099, 83, 1464, False
    TENT_D = 1100, 83, 1465, False
    TENT_E = 1101, 83, 1466, False
    TOWER_OF_LONDON = 1368, 37, 1492, False
    TOWN_CENTER = 109, 28, 1408, False
    TRADE_WORKSHOP = 110, 17, 1429, False
    UNIVERSITY = 209, 32, 1427, False
    WATCH_TOWER = 79, 25, 1436, False
    WONDER = 276, 37, 1445, False
    WOODEN_BRIDGE_A_BOTTOM = 1311, -1, 144, False
    WOODEN_BRIDGE_A_MIDDLE = 1310, -1, 144, False
    WOODEN_BRIDGE_A_TOP = 1309, -1, 144, False
    WOODEN_BRIDGE_B_BOTTOM = 1314, -1, 144, False
    WOODEN_BRIDGE_B_MIDDLE = 1313, -1, 144, False
    WOODEN_BRIDGE_B_TOP = 1312, -1, 144, False
    YURT_A = 712, 81, 1447, False
    YURT_B = 713, 82, 1448, False
    YURT_C = 714, 82, 1449, False
    YURT_D = 715, 82, 1450, False
    YURT_E = 716, 80, 1451, False
    YURT_F = 717, 80, 1452, False
    YURT_G = 718, 80, 1453, False
    YURT_H = 719, 79, 1454, False
    DONJON = 1665, 84, 1524, False
    TRADE_WORKSHOP_BR = 1647, 17, 1429, False
    TRADE_WORKSHOP_TG = 179, 17, 1429, False
