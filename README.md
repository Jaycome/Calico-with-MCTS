# Calico with Monte Carlo Tree Search

A Python implementation of the board game **Calico** focused on AI decision-making agents. The project implements Monte Carlo Tree Search (MCTS) agents and compares decision-making behaviour under different scoring heuristics, time budgets, and exploration-exploitation settings.

## Project Goals

- Implement a playable digital version of the Calico board game logic.
- Model game states, legal actions, scoring rules, and agent decisions.
- Implement Monte Carlo Tree Search for decision-making under uncertainty.
- Compare different MCTS variants and evaluation heuristics.
- Provide a reproducible structure for running experiments and analysing agent performance.

## Features

- Python-based Calico game logic.
- MCTS agent implementation.
- Alternative MCTS evaluation strategies.
- Command-line options for the number of games and the per-move search time.
- Per-game and summary results written to Excel workbooks for analysis.

## Repository Structure

```text
Calico-with-MCTS/
├── calico.py              # Experiment runner: plays the agents and records results
├── game_state.py          # Game state, legal moves and scoring
├── mcts.py                # MCTS agent, win/loss evaluation
├── mcts2.py               # MCTS agent, score-difference evaluation
├── meta.py                # Constants: players, tiles, patterns, exploration
├── docs/
│   ├── architecture.md
│   ├── algorithm-notes.md
│   ├── experiment-design.md
│   ├── test-plan.md
│   └── development-notes.md
├── requirements.txt
└── README.md
```

## Tech Stack

- Python 3.9+
- Monte Carlo Tree Search (MCTS)
- Game-state simulation
- Heuristic evaluation

## Installation

Clone the repository:

```bash
git clone https://github.com/Jaycome/Calico-with-MCTS.git
cd Calico-with-MCTS
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .venv\Scripts\activate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

`calico.py` plays the two MCTS agents against each other and prints win rates and average points per category:

```bash
python calico.py                                  # 50 games, 0.5 s search per move
python calico.py --games 10 --search-time 1.0     # custom run
```

A run writes two workbooks to the working directory:

- `MCTS4VsMCTS05.xlsx`: summary (wins, average button / cat / goal-tile points, total, min and max)
- `newMCTSVsMCTS.xlsx`: points per game and rollouts per turn

The random-agent experiments used in the original study are still in `calico.py` as commented-out blocks.

## Experiment Variables

The original project focuses on two major experimental variables:

1. **MCTS thinking time** — how long an agent is allowed to search before choosing an action.
2. **Exploration constant** — the parameter controlling the exploration-exploitation balance in UCT-style MCTS. It is set in each agent's `Node.value()`: the constant inside the square root is 4 in `mcts.py` and 0.5 in `mcts2.py`.

Two MCTS variants are considered:

- A variant that evaluates actions mainly by final game outcome.
- A variant that also considers immediate points gained by candidate actions.

## Suggested Evaluation Metrics

- Win rate
- Average final score
- Average decision time
- Number of simulations per move
- Score distribution across repeated games
- Stability of performance across different exploration constants

## Documentation

- [Architecture](docs/architecture.md)
- [Algorithm Notes](docs/algorithm-notes.md)
- [Experiment Design](docs/experiment-design.md)
- [Test Plan](docs/test-plan.md)
- [Development Notes](docs/development-notes.md)

## Future Improvements

- Add automated unit tests for game-state transitions and scoring rules.
- Add command-line arguments for experiment configuration.
- Add CSV output for repeated simulation results.
- Add charts for comparing MCTS variants.
- Refactor agent interfaces for easier comparison between search algorithms.
- Add baseline agents, such as random and greedy agents.

## Acknowledgements

The MCTS node and agent structure is adapted from [MCTS-agent-python](https://github.com/masouduut94/MCTS-agent-python) by Masoud Masoumi Moghadam et al. The Calico game logic, scoring and the two evaluation strategies were written for this project.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
