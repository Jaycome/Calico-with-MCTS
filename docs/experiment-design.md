# Experiment Design

## Purpose

The purpose of the experiments is to compare how MCTS agents perform under different search settings and evaluation heuristics.

## Independent Variables

- MCTS time budget per move
- Exploration constant
- Evaluation heuristic
- Number of simulations
- Agent type

## Dependent Variables

- Win rate
- Average final score
- Score variance
- Average decision time
- Number of simulations completed per move

## Suggested Experiment Matrix

| Experiment | Agent Variant | Time Budget | Exploration Constant | Repeated Games |
|---|---|---:|---:|---:|
| E1 | Outcome-focused MCTS | 1s | 1.0 | 100 |
| E2 | Outcome-focused MCTS | 3s | 1.0 | 100 |
| E3 | Point-aware MCTS | 1s | 1.0 | 100 |
| E4 | Point-aware MCTS | 3s | 1.0 | 100 |
| E5 | Point-aware MCTS | 3s | 1.4 | 100 |

## Result Reporting Template

| Agent | Avg Score | Win Rate | Avg Decision Time | Notes |
|---|---:|---:|---:|---|
| Outcome-focused MCTS | TBD | TBD | TBD | Baseline MCTS variant |
| Point-aware MCTS | TBD | TBD | TBD | Includes immediate score heuristic |

## Reproducibility Notes

- Use a fixed random seed where possible.
- Record Python version and dependency versions.
- Store raw experiment outputs under `results/`, which should be gitignored if generated frequently.
