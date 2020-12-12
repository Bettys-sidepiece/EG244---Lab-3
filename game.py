from room import Room
from command_parser import Parser

"""
 *  This class is the main class of the "World of Zuul" application. 
 *  "World of Zuul" is a very simple, text based adventure game.  Users 
 *  can walk around some scenery. That's all. It should really be extended 
 *  to make it more interesting!
 * 
 *  To play this game, create an instance of this class and call the "play"
 *  method.
 * 
 *  This main class creates and initialises all the others: it creates all
 *  rooms, creates the parser and starts the game.  It also evaluates and
 *  executes the commands that the parser returns.
"""

class Game():
    """ To play this game, create an instance of this class and call the "play"  method.
    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game.  It also evaluates and
    executes the commands that the parser returns.
    """
    def __init__(self):
        """ Create the game and initialise its internal map. """
        self.create_rooms()
        self.parser = Parser()

    def create_rooms(self):
        """ Create all the rooms and link their exits together. """
        # create the rooms
        outside = Room("outside the main entrance of the university")
        theater = Room("in a lecture theater")
        pub = Room("in the campus pub")
        lab = Room("in a computing lab")
        office = Room("in the computing admin office")
        
        # initialise room exits
        outside.set_exit("east", theater)
        outside.set_exit("south", lab)
        outside.set_exit("west", pub)
        
        #initialise the items in the room
        outside.set_item("keycard","unlocks door in the computing lab ",0.2)
        #sets the position of the item
        outside.set_item_position("keycard", "on a grass patch")
        
        
        theater.set_exit("west", outside)

        pub.set_exit("east", outside)

        lab.set_exit("north", outside)
        lab.set_exit("east", office)

        office.set_exit("west", lab)

        self.current_room = outside;  # start game outside

    def play(self):
        """ Main play routine.  Loops until end of play """
        self.print_welcome()

        # Enter the main command loop.  Here we repeatedly read commands and
        # execute them until the game is over.
                
        finished = False
        while finished == False:
            command = self.parser.get_command()
            finished = self.process_command(command)
        print("Thank you for playing.  Good bye.")

    def print_welcome(self):
        """ Print out the opening message for the player """
        print()
        print("Welcome to the World of Zuul!")
        print("World of Zuul is a new, incredibly boring adventure game.")
        print("Type 'help' if you need help.")
        print()
        print(self.current_room.get_long_description())

    def process_command(self, command):
        """ Given a command, process (that is: execute) the command.

        Parameters
        ----------
        command: Command
            The command to be processed
        
        Returns true If the command ends the game, false otherwise.
        """
        want_to_quit = False

        if command.is_unknown():
            print("I don't know what you mean...")
            return False

        command_word = command.get_command_word()
        if command_word == "help":
            self.print_help()
        elif command_word == "go":
            self.go_room(command)
        elif command_word == "quit":
            want_to_quit = self.quit(command)
        
        return want_to_quit

    # implementations of user commands:

    def print_help(self):
        """ Print out some help information. """
        print("You are lost. You are alone. You wander")
        print("around at the university.")
        print()
        print("Your command words are:")
        self.parser.show_commands()

    """
     * Try to in to one direction. If there is an exit, enter the new
     * room, otherwise print an error message.
    """
    def go_room(self, command):
        """ Try to in to one direction. If there is an exit, enter the new
        room, otherwise print an error message.

        Parameters
        ----------
        command: Command
            The command to be processed
        """
        if command.has_second_word() == False:
            # if there is no second word, we don't know where to go...
            print("Go where?")
            return

        direction = command.get_second_word()

        # Try to leave current room.
        next_room = self.current_room.get_exit(direction)

        if next_room == None:           # None is a special Python value that says the variable contains nothing
            print("There is no door!")
        else:
            self.current_room = next_room
            print(self.current_room.get_long_description())

    def quit(self, command):
        """ "Quit" was entered. Check the rest of the command to see whether we really quit the game.

        Parameters
        ----------
        command: Command
            The command to be processed
        
        Returns true, if this command quits the game, false otherwise.
        """
        if command.has_second_word():
            print("Quit what?")
            return False
        else:
            return True  # signal that we want to quit
