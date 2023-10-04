import math
class GameMeta:
    PLAYERS = {'none': 0, 'one': 1, 'two': 2,'draw':3}
    OUTCOMES = {'none': 0, 'one': 1, 'two': 2, 'draw': 3}
    INF = float('inf')
    ROWS = 5
    COLS = 5
    TILE_ELEMENT={'none':0,
                  'light_blue':1,
                  'dark_blue':2,
                  'purple':3,
                  'pink':4,
                  'green':5,
                  'yellow':6,
                  'target_base':7}

    TILE_PATTERN={'none':0,
                  'vines':1,
                  'stripes':2,
                  'dots':3,
                  'ferns':4,
                  'flowers':5,
                  'quatrefoil':6,
                  'target_base':7}

    GOAL_TILE_TYPE={'none':0,
                    'single':1,
                    'double':2,
                    'triple':3

    }
class MCTSMeta:
    EXPLORATION = math.sqrt(2)