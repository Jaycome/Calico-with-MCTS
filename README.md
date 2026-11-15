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
- Configurable simulation parameters, such as time budget and exploration constant.
- Experiment-oriented structure for analysing decision quality and game outcomes.

## Repository Structure

```text
Calico-with-MCTS/
├── calico.py              # Core Calico game logic
├── ConnectState.py        # Game state representation
├── mcts.py                # MCTS implementation
├── mcts2.py               # Alternative MCTS variant
├── meta.py                # Supporting metadata / configuration
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

Run the main game or experiment script:

```bash
python calico.py
```

## Experiment Variables

The original project focuses on two major experimental variables:

1. **MCTS thinking time** — how long an agent is allowed to search before choosing an action.
2. **Exploration constant** — the parameter controlling the exploration-exploitation balance in UCT-style MCTS.

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

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
