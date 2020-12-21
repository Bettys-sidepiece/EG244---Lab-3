from room import Room
from room import Transport_Room
from room import Character
from player import Player
from command_parser import Parser

"""
 Game Class
 ------------------------------------------------------------------------------
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
    rooms,creates all the characters, initialises player abilities,creates the parser, stores the room history
    and starts the game.  It also evaluates and executes the commands that the parser returns.
    """
    def __init__(self):
        """ Create the game and initialise its internal map. """
        self.create_rooms()
        self.parser = Parser()
        self.player = Player()
        self.characters()
        self.history = []
        
    def add_to_history(self, room):
        """Add the rooms the player has been in to the history list"""
        self.history.append(room)     
               
    def refresh(self):
        """Refresh the screen after an event"""
        print("\n")
        print(self.current_room.get_long_description())
        
    def characters(self):
        """ Create all characters and place them in a room"""
        self.char_list = [] #Stores the existing characters in the game for interaction
       # self.evan = Character("evan","Student")
       # self.evan.set_current_room(self.evan_room)
       # self.char_list.append(self.evan)
        
    def create_rooms(self):
        """ Create all the rooms and link their exits together. """
        
        # create the rooms
        reception = Room("in the reception")
        reception.set_name("Reception")
        
        east_hallway = Room("in a east hallway")
        east_hallway.set_name("east hallway")
        
        arrivals = Room("in the arrivals")
        arrivals.set_name("arrivals")
        
        atrium = Room("in the Atrium")
        atrium.set_name("atrium")
        
        east_restroom = Room("in the arrivals restroom")
        east_restroom.set_name("east Restroom")
        
        security = Room("in the Security room")
        security.set_name("security")
        
        west_restroom = Room("in the main restroom")
        west_restroom.set_name("west restroom")
        
        west_hallway = Room("in the west hallway")
        west_hallway.set_name("west hallway")
        
        cafeteria = Room("in the cafeteria")
        cafeteria.set_name("cafeteria")
        
        lab = Room("In the Teleportation RD Laboratory")
        lab.set_name("Lab")
        
        storage = Room("In equipment storage")
        storage.set_name("storage")
        
        marketing = Room("In the marketing offices")
        marketing.set_name("marketing")
        
        office = Room("you are in Mr.Samsa's Office")
        office.set_name("office")
        
        teleporter = Transport_Room("in a faulty experimental teleporter")
        
        # initialise room exits and items
        reception.set_exit("west",atrium)
        reception.set_exit("east",east_hallway)
        reception.set_item("Box","Labelled Rigid-works",5.1)
        reception.set_item_position("Box","next to the reception counter")

        east_hallway.set_exit("east", reception)
        east_hallway.set_exit("west", east_restroom)
        east_hallway.set_exit("north", arrivals)
        
        east_restroom.set_exit("east", east_restroom)
        
        arrivals.set_exit("south",east_hallway)
        arrivals.set_exit("east", lab)
        
        atrium.set_exit("east", reception)
        atrium.set_exit("north", security)
        atrium.set_exit("west", west_hallway)
        atrium.set_exit("south", cafeteria)
        
        security.set_exit("south",atrium)

        west_restroom.set_exit("east", west_hallway)
        
        west_hallway.set_exit("east", atrium)
        west_hallway.set_exit("west", west_restroom)
        west_hallway.set_exit("north", marketing)
        
        cafeteria.set_exit("north", atrium)
        
        lab.set_exit("north", teleporter)
        lab.set_exit("west", arrivals)
        lab.set_exit("east", storage)
        
        storage.set_exit("west",lab)
        
        marketing.set_exit("south", west_hallway)
        marketing.set_exit("north", office)
        
        self.current_room = reception;  # start game outside
        #self.evan_room = pub
        
        #add rooms to list to enable random transportation
        teleporter.set_exit('????',lab)
        teleporter.add_rooms(marketing)
        teleporter.add_rooms(office)
        teleporter.add_rooms(west_restroom)
        teleporter.add_rooms(east_restroom)
        teleporter.add_rooms(security)
        teleporter.add_rooms(atrium)
        teleporter.add_rooms(cafeteria)
        teleporter.add_rooms(west_hallway)
        teleporter.add_rooms(east_hallway)
        teleporter.add_rooms(storage)
        teleporter.add_rooms(reception)
        self.teleporter = teleporter
        
    def teleport(self):
        if self.current_room == self.teleporter:
            self.current_room = self.teleporter.random_room()
            self.refresh()
            self.history.pop(-1)
    
    def play(self):
        """ Main play routine.  Loops until end of play """
        self.player.set_capacity(5.0)
        self.print_welcome()
        
        # Enter the main command loop.  Here we repeatedly read commands and
        # execute them until the game is over.
                
        finished = False
        while finished == False:
            self.add_to_history(self.current_room)
            self.teleport()
            command = self.parser.get_command()
            finished = self.process_command(command)
        print("Thank you for playing. Good bye.")


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
            self.refresh()
            self.history.pop(-1)
            return False

        command_word = command.get_command_word()
        if command_word == "help":
            self.print_help()
        elif command_word == "go":
            self.go_room(command)
        elif command_word == "give":
            self.character_interact(command)
        elif command_word == "back":
            self.back(command)
        elif command_word == "pick":
            self.interact(command)
        elif command_word == "open":
            self.interact(command)
        elif command_word == "drop":
            self.interact(command)
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
        if command.get_command_word() == "go":
            if command.has_second_word() == False:
                # if there is no second word, we don't know where to go...
                print("Go where?")
                self.refresh()
                self.history.pop(-1)
                self.history.pop(-1)
                return

            direction = command.get_second_word()

            # Try to leave current room.
            next_room = self.current_room.get_exit(direction)

            if next_room == None:           # None is a special Python value that says the variable contains nothing
                print("There is no door!\n")
                self.history.pop(-1)
                self.refresh()
    
            else:
                self.current_room = next_room
                self.refresh()
      
    """
     * Go back to the previous room you were in, if you at the start
     * a message is shown informing you of this.
    """   
    def back(self, command):
        """ back allows the player to retrace their steps, by going backwards in each room
        the had already been
        
        Parameters
        ----------
        command: Command
            The command to be processed
        """
        if command.get_command_word() == "back":
            if len(self.history) <= 1:
                self.refresh()
                print("\nThis is your start point")
                self.history.pop(-1)
            else:
                
                if self.history[0] == self.history[1]:
                    self.history.pop(1)
                    
                elif len(self.history) == 2:
                    self.current_room = self.history[0]
                    self.history.pop(1)
                else:
                    self.history.pop(-1)
                    self.current_room = self.history[-1]
                    self.history.pop(-1)
                self.refresh()
            
    
    """
     * Go back to the previous room you were in, if you at the start
     * a message is shown informing you of this.
    """           
    def interact(self, command):
        """ Try to interact with the items. If there is an item, you can pick
        it up, if you have an item you can drop the item and you can open your
        inventory to view the items you have, otherwise print an error message.

        Parameters
        ----------
        command: Command
            The command to be processed
        """
        count = 0
        exit_inventory = False
        entry = ""
        
        if command.get_command_word() == "pick": #Allows the player to interact with items in the room
            if command.has_second_word() == False:
                print("Pick what?")
                self.refresh()
                self.history.pop(-1)
                return
            
            #Trying to pick up a specific item
            item = command.get_second_word()
            self.history.pop(-1)
            for items in self.current_room.items:
                if item == items.get_name() and self.player.has_space(items.weight) != False:
                    
                    #The selected item is added to the player's inventory and  removed from the current room
                    
                    self.player.add_item(items)
                    self.current_room.pop_item(items)
                    self.refresh()
                    
                elif self.player.has_space(items.weight) == False:
                    
                    #This ensures that the set player limit is not exceeded                    
                    self.refresh()
                    print("\nYou'll exceed your inventory capacity.\n")
                    
                elif item != items.get_name() and count == len(self.current_room.items):
                    self.refresh()
                    print(item + " is not in the area\n")
                count += 1

                
        elif command.get_command_word() == "drop": #Allows the player to drop an item in their inventory
            if command.has_second_word() == False: 
                print("Drop what?")
                self.refresh()
                self.history.pop(-1)
                return
            
            # Try to drop a specific item            
            self.history.pop(-1)
            item = command.get_second_word()
            for items in self.player.inventory:
                if item == items.get_name():
                    
                    # The selected item is removed from the inventory and placed in the current room
                    
                    self.player.pop_item(items)
                    self.current_room.set_item(items.name, items.info, items.weight)
                    self.refresh()
                    
                else:
                    self.refresh()
                    print(item + " is not in the your inventory\n")
                        
                        
        elif command.get_command_word() == "open": #Allows the player to view their inventory 
            if command.has_second_word() == False:
                print("Open what?")
                self.refresh()
                self.history.pop(-1)
                return
            # Try and open inventory            
            if command.get_second_word() == "inventory":
                if len(self.player.inventory) == 0:
                    self.refresh()
                    print("\nThere are no items in your inventory.")
                
                else:
                    print("\n" * 20)
                    self.inventory_options()
                    entry = input("> ")
                    
                    while exit_inventory == False:
                        for item in self.player.inventory:
                            if entry == "exit":
                                exit_inventory = True
                                
                            elif entry == ("show " + item.name): #try and view an items details i.e weight, description and name
                                print("\n" * 20)
                                print(item.get_full_description())
                                print("\n Actions: back | exit | drop item")
                                entry = input("> ")
                                if entry == "back": #This back command only affects the inventory menu 
                                    print("\n" * 20)
                                    self.inventory_options()
                                    entry = input("> ")
                                
                            elif entry == ("drop " + item.name): #This allows the player to drop and item from the inventory menu
                                self.player.pop_item(item)
                                self.current_room.set_item(item.name, item.info, item.weight)
                                if len(self.player.inventory) == 0:
                                    exit_inventory = True
                                else:
                                    print("\n Actions: show item | exit | drop item")
                                    entry = input("> ")
                                
                            else: #error message
                                print("\n"*20+"I dont know what you mean\n")
                                self.inventory_options()
                                entry = input("> ")
                                
                    self.history.pop(-1)            
                    self.refresh()
            else:
                print("I dont know what that means")
        else:
            print("I dont know what that means")
        
        
    """
     * Allows interactions with character in the room
    """           
    def character_interact(self,command):
        """ Try to interact with the characters. If there is a character in the room
        the player can give the character and item, characters can sometimes give
        items to players. the command required looks something like "give 'character''item'"
        where character is the name of the prefered character and item an item in the player's
        inventory. otherwise an error message is printed
        
        Parameters
        ----------
        command: Command
            The command to be processed
        """
        if command.get_command_word() == "give": # try and give a character and item
            if command.has_second_word() == False:
                print("Open what?")
                self.refresh()
                self.history.pop(-1)
                return
            
            self.history.pop(-1)
            for npc in self.char_list: #check if the character exists
                if command.get_second_word() == npc.name and npc.current_room == self.current_room:
                    for item in self.player.inventory: #check if the item exists
                        if command.get_third_word() == item.name:
                            npc.add_item(item)
                            self.player.pop_item(item)
                            self.refresh()
                            print("\nyou have given "+npc.name+", a "+item.name)
                            
                        else:
                            self.refresh()
                            print("\n", command.get_third_word,"is not in your inventory.")
                else:
                    print("\nI dont know who that is")
                    self.refresh()
            
            
    def inventory_options(self):
        #print the inventory of the player        
        self.player.print_inventory()
        print("\n Actions: show item | exit | drop item")
        
    def has_won(self):
        None
    
    
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
