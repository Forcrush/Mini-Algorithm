# 3=/76=/239/424/438/480/567/992/1176

# UoM COMP90054 Contest Project
## Youtube presentation

## Team Members
- Hongyu Chen - hongchen1@student.unimelb.edu.au - 1062897
- Jin Tian - t.jin8@student.unimelb.edu.au - 919208
- You Guo - youg1@student.unimelb.edu.au - 804177

## Approximate Q-Learning
### Problems
- Dead end scenario
- Pacman has no interest in eating capsule

### Solutions
- Add feature to solve the dead end situation
- Add training iterations or add feature about capsule-eating

## MCTS
### Problems
- Computation cost
- Termination condition in simulation
- Weighted parameters of features

### Solutions
- Set a low depth to iterate
- Discard the termination flag that all steps are run out, we just use a fixed depth to simulation
- The weight parameters of features such as the ‘distance to food’ / ‘distance to enemy’ are obtained through lots of experiments

## Final result

The MCTS has better performance than Approximate Q-learning on different layouts. Generally, maybe the approximate Q-learning lacks of training and some parameters are hard to adjust. Hence, the MCTS is the final algorithm implemented in our code. The core of MCTS is simulation part, which can update the value using back-propagation on each path. The simulation code is demonstrated as follows:
```
def simulation()
```