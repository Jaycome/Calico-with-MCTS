# Test Plan

This project should include tests for both game logic and MCTS behaviour.

## Game Logic Tests

| Test Area | Example Test | Expected Result |
|---|---|---|
| Game state initialization | Create a new game state | Board and player state are valid |
| Legal move generation | Request legal moves | Only valid actions are returned |
| Move application | Apply a legal move | Board state updates correctly |
| Scoring | Score known board state | Score matches expected value |
| Turn transition | End current turn | Next player / next state is correct |

## MCTS Tests

| Test Area | Example Test | Expected Result |
|---|---|---|
| Node expansion | Expand an unexplored node | Child nodes are created |
| Simulation | Run rollout | Valid terminal or evaluation result is produced |
| Backpropagation | Update parent nodes | Visit counts and values are updated |
| Action selection | Select best action | Returned action is legal |

## Manual Validation

- Run a short game with a random or MCTS agent.
- Confirm the program completes without runtime errors.
- Compare agent decisions under different exploration constants.
- Confirm repeated simulations produce meaningful output.
