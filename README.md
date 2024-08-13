# The Delivery

## Description
"The Delivery" is a text-based adventure game implemented in Python. Players navigate through various rooms, interact with characters, collect and use items, and attempt to complete their delivery mission.

## Features
- Room-based navigation system
- Character interactions
- Inventory management
- Item usage and puzzle-solving
- Random events and teleportation mechanics

## How to Play
1. Run the `game.py` file to start the game.
2. Use text commands to interact with the game world:
   - `go [direction]`: Move in a specific direction (e.g., "go north")
   - `pick up [item]`: Pick up an item
   - `drop [item]`: Drop an item from your inventory
   - `open inventory`: View your current inventory
   - `interact with [character]`: Interact with a character in the room
   - `give [character] [item]`: Give an item to a character
   - `help`: Display available commands
   - `quit`: Exit the game

## Game Objective
Your mission is to deliver a package to Mr. G Samsa at Rigid-Works, navigating through the building, solving puzzles, and interacting with various characters along the way.

## Key Components
- `game.py`: Main game logic and loop
- `room.py`: Defines the Room and Transport_Room classes
- `item.py`: Defines various item types (Item, Consumable, Key, teleport)
- `character.py`: Defines the Character class for NPCs
- `player.py`: Defines the Player class and inventory management
- `command_parser.py`: Handles parsing of user input
- `command_words.py`: Defines valid commands

## Installation
1. Ensure you have Python installed on your system.
2. Clone this repository or download the source files.
3. Run `python game.py` in your terminal to start the game.

## Contributing
This project is part of a learning exercise. If you have suggestions or improvements, please open an issue or submit a pull request.

## Acknowledgements
This game was created as part of [My University Software Engineering Course]. Special thanks to [Professor Jason Jones].
