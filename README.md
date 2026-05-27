# Blood Money

A text-based western noir RPG built in Python, set in the American frontier in 1872.

## Story

You play as John Calloway, an infamous outlaw and hired gun. After winning a duel in the street, you are approached by a rancher with a job — track down a man who wronged him and deal with him quietly. What starts as a straightforward contract slowly unravels into something far more dangerous.

## Features

- Branching dialogue with meaningful choices
- D&D 5e mechanics including d20 ability checks, advantage and disadvantage, and combat
- A custom Gunslinger class with unique abilities
- Multiple endings depending on the choices you make
- A story that rewards paying attention

## How to Play

Run `main.py` to start the game. When prompted to make a choice, type the corresponding number and press enter. Some choices will trigger ability checks — the outcome depends on your character's stats and the roll of a dice.

## Files

- `main.py` — entry point
- `story.py` — all narrative and dialogue
- `combat.py` — combat system
- `characters.py` — player and enemy stats
- `utils.py` — dice rolling, ability checks, and shared utilities
- `copy_code.py` - saves all code to clipboard

## Requirements

- Python 3.8+
- pyfiglet (`pip install pyfiglet`)
