"""
@author: Masoud Masoumi Moghadam
Code Script:
Code for running Monte Carlo Tree Search method applying the evaluation with considering win or loss alone
Adapted code from "Monte-Carlo-Tree-Search-Agent-for-the-Game-of-HEX" by Masoud Masoumi Moghadam et al. at https://github.com/masouduut94/MCTS-agent-python """
import math
import time
import random
from copy import deepcopy
from meta import GameMeta,MCTSMeta
from ConnectState import GameState


class Node:

    def __init__(self, move, parent):
        self.move = move
        self.parent = parent
        self.N = 0  # times this position was visited
        self.Q = 0  # average reward (wins-losses) from this position
        self.N_RAVE = 0
        self.Q_RAVE = 0
        self.children = {}
        self.outcome = GameMeta.PLAYERS['none']

    def add_children(self, children: dict) -> None:
        for child in children:
            self.children[child.move] = child

    def value(self, explore: float = MCTSMeta.EXPLORATION):
        if self.N == 0:
            return 0 if explore == 0 else GameMeta.INF
        else:
            return self.Q / self.N + explore * math.sqrt(4*math.log(self.parent.N) / self.N)  # exploitation + exploration

        
class UctMctsAgent:

    def __init__(self, state=GameState()):
        self.root_state = deepcopy(state)
        self.root = Node(None,None)
        self.run_time = 0
        self.node_count = 0
        self.num_rollouts = 0

    def select_node(self) -> tuple:
        node = self.root
        state = deepcopy(self.root_state)
        while len(node.children) != 0:
            children = node.children.values()
            max_value = max(children, key=lambda n: n.value()).value()
            max_nodes = [n for n in children if n.value() == max_value]
            node = random.choice(max_nodes)
            state.move(node.move)
            if node.N == 0:
                return node, state
        if self.expand(node, state):
            node = random.choice(list(node.children.values()))
            state.move(node.move)
        return node, state

    def expand(self,parent: Node, state: GameState) -> bool:
        if state.round>=22:
            return False
        children = [Node(move, parent) for move in state.possible_moves()]
        parent.add_children(children)
        return True

    def roll_out(self,state: GameState) -> int:
        while (state.round<=22):
            moves = state.possible_moves()
            move = random.choice(moves)
            state.move(move)
            moves2=state.possible_moves2()
            move2=random.choice(moves2)
            state.move(move2)
        return state.winner
    
    def backup(self,node: Node, turn: int, outcome: int) -> None:
        reward = 0 if outcome == turn else 1
        while node is not None:
            node.N += 1
            node.Q += reward
            node = node.parent
            if outcome == GameMeta.OUTCOMES['draw']:
                reward = 0
            elif(reward==1):
                reward=-1
            elif(reward==-1):
                reward=1

    def search(self, time_budget: int):
        start_time = time.perf_counter()
        num_rollouts = 0
        while time.perf_counter() - start_time < time_budget:
            node, state = self.select_node()
            outcome = self.roll_out(state)
            self.backup(node,state.to_play,outcome)
            num_rollouts += 1
        run_time = time.perf_counter() - start_time
        self.run_time = run_time
        self.num_rollouts = num_rollouts

    def best_move(self):
        if self.root_state.round>=22:
            return -1
        max_value = max(self.root.children.values(), key=lambda n: n.N).N
        max_nodes = [n for n in self.root.children.values() if n.N == max_value]
        best_child = random.choice(max_nodes)
        return best_child.move

    def move(self, move):
        if move in self.root.children:
            self.root_state.move(move)
            self.root = self.root.children[move]
            return
        self.root_state.move(move)
        self.root = Node(None, None)

    def statistics(self) -> tuple:
        return self.num_rollouts, self.run_time

    