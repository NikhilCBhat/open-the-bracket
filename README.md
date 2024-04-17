# Open the Bracket! 

A multiplayer turn-based numbers game.   

## Game Rules
Each turn players can either provide an operation (+, -, mod, factorial, etc) or a number. The goal is to form an equation, which results in being as close as possible to a predetermined target number.

The operations/numbers are evaluated into an equation as a running stream. Ex: 3, +, 5, ^, 2  would be 64 (3+5=8, 8^2=64)

Players can only use each operation and digit once. 

## Execution Instructions
```sh
python3 numbers_game.py
```