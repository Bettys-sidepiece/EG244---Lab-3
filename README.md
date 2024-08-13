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

## Sample Game Screen
```
You are at the front desk, Receptionist is in the area.
There is a box next to the front desk.
Exits: west east

> interact with receptionist

Receptionist:
Hello, welcome to RidgeWorks, what can i help you with?

1) Hi, I am here to deliver a package addressed to Mr.Samsa.
2) Where are your restrooms.

> 1

Receptionist:
I have to let you know that due to security reasons all deliveries 
have to be inspected by our security officer. After inspection a
silver chip will be given to you. hand in the chip with the delivery
and you'll be on your way.

1) Okay
2) Where is the security room 

> 2

Receptionist:
The security room is through the west exit
into the atrium taking the north exit.

> go west

You are in the Atrium, Rudy is in the area.
Exits: west north south east

> 
```
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
