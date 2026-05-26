# Architecture

## Overview

This project implements a digital version of Calico and focuses on AI decision-making through Monte Carlo Tree Search (MCTS). The system can be understood as four layers:

1. **Game State Layer** — represents the board, tiles, player turns, legal moves, and current score context.
2. **Game Logic Layer** — applies moves, updates the board, and calculates scoring outcomes.
3. **Agent Layer** — chooses actions using MCTS or alternative decision strategies.
4. **Experiment Layer** — runs repeated simulations to compare agent behaviour under different settings.

## Main Components

```text
calico.py
  Core game execution and main game loop.

ConnectState.py
  Game-state representation used by the search agent.

mcts.py
  MCTS implementation using selection, expansion, simulation, and backpropagation.

mcts2.py
  Alternative MCTS implementation or scoring heuristic.

meta.py
  Supporting configuration or metadata used by the game logic.
```

## Data Flow

```mermaid
flowchart LR
    GameState[Game State] --> LegalMoves[Legal Move Generation]
    LegalMoves --> MCTS[MCTS Agent]
    MCTS --> Simulation[Rollout / Simulation]
    Simulation --> Evaluation[Score Evaluation]
    Evaluation --> Backprop[Backpropagation]
    Backprop --> Action[Selected Action]
    Action --> GameState
```

## Design Considerations

- Keep game state transitions deterministic and testable.
- Separate agent decision logic from game rule logic.
- Make experiment parameters configurable.
- Record simulation results for reproducible comparisons.
