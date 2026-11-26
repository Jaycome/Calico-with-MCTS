import random
from copy import deepcopy

import pytest

from game_state import GameState
from mcts import UctMctsAgent
from mcts2 import UctMctsAgent2
from meta import GameMeta

ONE, TWO, DRAW = GameMeta.PLAYERS["one"], GameMeta.PLAYERS["two"], GameMeta.PLAYERS["draw"]
CAT_7_POINTS = 4  # token value of the 7-point cat


def new_game(seed=0):
    random.seed(seed)
    state = GameState()
    state.initial_setting()
    state.cat_setting()
    state.set_goal_tile(state.tile_base)
    state.set_goal_tile(state.tile_base2)
    state.place_goal_tile(state.tile_base, (0, 1, 2), (6, 13, 16))
    state.place_goal_tile(state.tile_base2, (0, 1, 2), (6, 13, 16))
    return state


def play_randomly(state):
    while state.round <= 22:
        state.move(random.choice(state.possible_moves()))
        state.move(random.choice(state.possible_moves2()))
    return state


def test_new_game_has_legal_moves_and_player_one_starts():
    state = new_game()
    assert state.to_play == ONE
    assert state.possible_moves()


def test_move_passes_the_turn():
    state = new_game()
    state.move(state.possible_moves()[0])
    assert state.to_play == TWO
    state.move(state.possible_moves2()[0])
    assert state.to_play == ONE


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_random_game_finishes_with_a_result(seed):
    state = play_randomly(new_game(seed))
    assert state.winner in (ONE, TWO, DRAW)


def finished_game_with_identical_boards():
    state = play_randomly(new_game(3))
    state.tile_base2 = deepcopy(state.tile_base)
    return state


def test_identical_boards_draw():
    assert finished_game_with_identical_boards().winner == DRAW


@pytest.mark.parametrize("board, expected", [("tile_base", ONE), ("tile_base2", TWO)])
def test_seven_point_cat_counts_only_for_its_owner(board, expected):
    # Regression test: player 2's 7-point cats used to be read from player 1's board.
    state = finished_game_with_identical_boards()
    tiles = getattr(state, board)
    empty = next(i for i, t in enumerate(tiles) if t["token"] == 0)
    tiles[empty]["token"] = CAT_7_POINTS
    assert state.winner == expected


def test_agents_choose_legal_moves():
    state = new_game(4)
    first, second = UctMctsAgent(state), UctMctsAgent2(state)

    first.search(0.05)
    move = first.best_move()
    assert move in state.possible_moves()
    state.move(move)
    first.move(move)
    second.move(move)

    second.search(0.05)
    move2 = second.best_move()
    assert move2 in state.possible_moves2()
