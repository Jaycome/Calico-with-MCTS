# Algorithm Notes

## Monte Carlo Tree Search

Monte Carlo Tree Search is a simulation-based search algorithm often used in games with large decision spaces. It repeatedly explores possible future game states and updates estimated action values based on simulated outcomes.

A standard MCTS loop includes:

1. **Selection** — traverse the search tree by selecting promising child nodes.
2. **Expansion** — add one or more unexplored child states.
3. **Simulation** — run a rollout from the expanded state.
4. **Backpropagation** — update node statistics based on the simulation result.

## Exploration-Exploitation Trade-off

The exploration constant controls whether the agent prefers:

- **Exploitation:** choosing actions that already appear strong.
- **Exploration:** trying less-visited actions that may reveal better outcomes.

In experiments, this parameter should be varied to evaluate how sensitive the agent is to search behaviour.

## MCTS Variants in This Project

The project describes two MCTS variants:

1. **Outcome-focused MCTS** — evaluates actions mainly based on final game outcomes.
2. **Point-aware MCTS** — also considers immediate points gained by actions.

These variants can be compared by running repeated simulations and measuring score distributions, win rates, and consistency.

## Baseline Agents to Add Later

Recommended future baselines:

- Random agent
- Greedy score-based agent
- Rule-based heuristic agent

Adding baselines will make MCTS performance easier to interpret.
