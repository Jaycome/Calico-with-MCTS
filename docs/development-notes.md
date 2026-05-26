# Development Notes

## Recommended Refactoring

- Separate game rules from agent logic.
- Add a common `Agent` interface for MCTS, random, and heuristic agents.
- Move experiment scripts into an `experiments/` directory.
- Add structured result logging using CSV or JSON.
- Add type hints to key modules.

## Suggested Future Structure

```text
src/
├── game/
│   ├── state.py
│   ├── rules.py
│   └── scoring.py
├── agents/
│   ├── mcts.py
│   ├── random_agent.py
│   └── heuristic_agent.py
├── experiments/
│   └── run_experiment.py
└── utils/
    └── logging.py
```

## Quality Improvements

- Add unit tests for scoring and move legality.
- Add command-line arguments for time budget and exploration constant.
- Add experiment output files for reproducible analysis.
- Add visualizations for score distribution and win rate comparison.
