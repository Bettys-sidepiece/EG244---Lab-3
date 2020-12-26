from room import Room, Transport_Room
from item import Item, Key, Consumable, teleport
from character import Character 
from player import Player
from game_assets import Assets
from command_parser import Parser
import random


"""
 Game Class
 ------------------------------------------------------------------------------
 *  This class is the main class of the "The Delivery" application. 

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
        self.asset = Assets()
       
       
    def add_to_history(self, room):
        """Add the rooms the player has been in to the history list"""
        self.history.append(room)     
       
       
    def refresh(self):
        """Refresh the screen after an event"""
        self.char_in_room()
        self.character_move()
        self.char_in_room()
        
        print("\n\n"+self.current_room.get_long_description())
                
    def characters(self):
        """ Create all characters and place them in a room"""
        self.char_list = [] #Stores the existing characters in the game for interaction
        
        # Create all the charecters and antagonists    
        self.receptionist = Character("receptionist","Works at the front dest of ridgeworks")
        self.char_list.append(self.receptionist)
        self.receptionist.set_current_room(self.reception_copy)
       
        self.security = Character("officer.david","Deals with security in the building")
        self.char_list.append(self.security)
        self.security.set_current_room(self.security_copy)
        self.security.add_item(self.chip)
        
        self.technician_1 = Character("mr.smith","lab technician")
        self.char_list.append(self.technician_1)
        self.technician_1.set_current_room(self.reception_copy)
         
        self.rudy = Character("rudy","custodial worker")
        self.char_list.append(self.rudy)
        self.rudy.set_current_room(self.atrium_copy)
         
        self.researcher_1 = Character("dr.hsu","researcher at RigdeWorks")
        self.char_list.append(self.researcher_1)
        self.researcher_1.set_current_room(self.cafe_copy)
         
        self.technician_2 = Character("ms.chungu","lab technician")
        self.char_list.append(self.technician_2)
        self.technician_2.set_current_room(self.cafe_copy)
         
        self.researcher_2 = Character("dr.solis","researcher at RigdeWorks")
        self.char_list.append(self.researcher_2)
        self.researcher_2.set_current_room(self.atrium_copy)
         
        self.researcher_3 = Character("dr.hay","resarcher at RidgeWorks")
        self.char_list.append(self.researcher_3)
        self.researcher_3.set_current_room(self.cafe_copy)
         
        self.clerk = Character("mr.bore","deals with build vistors")
        self.char_list.append(self.clerk)
        self.clerk.set_current_room(self.arrivals_copy)
        self.clerk.add_item(self.form)
       
 
    def char_in_room(self):
        count = 0
        for char in self.char_list:
            if char.current_room == self.current_room:
                self.current_room.characters.append(char)
                self.current_room.characters = list(set(self.current_room.characters))
                 
            elif char in self.current_room.characters and char.current_room != self.current_room:
                try: 
                    del self.current_room.characters[count]
                    count = 0
                except IndexError:
                    print()
                
            count += 1
            
    def character_move(self):
        self.technician_1.move()
        self.rudy.move()
        self.technician_2.move()
        self.researcher_1.move()
        self.researcher_2.move()
        self.researcher_3.move()
               
    def create_rooms(self):
        self.string = ""
        """ Create all the rooms and link their exits together. """
        #create the items
        keycard_1 = Key("keycard-B29","Property of Ridge-works (TRD division)",0.1)
        keycard_1.set_id("B29")
        
        keycard_2 = Key("keycard-R25","Property of Ridge-works (TRD division)",0.1)
        keycard_1.set_id("J27")
        
        keycard_3 = Key("keycard-T07","Property of Ridge-works (Dr. Hsu)",0.1)
        keycard_3.set_id("T07")
        
        box = Item("box","----",6)
        box_1 = Item("box","----",9)
        
        self.chip = Key("chip","Security RFID Chip",0.05)
        self.chip.set_id("37A")
        
        serum_69 = Consumable("U-69","Red liquid in test-tube",0.7)
        serum_69.set_type("1A")
    
        serum_56 = Consumable("U-56","Blue liquid in test-tube",0.7)
        serum_69.set_type("1A")
        
        bar = Consumable("candybar","High in sugar", 0.25)
        bar.set_type("1B")
        water = Consumable("water bottle","Literally just water",0.8)
        water.set_type("1C")
        
        self.form = Key("document","Delivery Form, containing the weight of the parcel and date of shipment ",0.01)
        self.form.set_id("25H")
        
        self.package = Key("package","Addressed to Mr.G Samsa at Rigid-Works, 917 Administration Ave, Arkansas.",2.5)
        self.package.set_id("T19")
        
        teleporter_ = teleport("teleporter","Portable teleporter, can be used to teleport anywhere in the building.\n Has a small LCD screen.",2.5)
        
        
        #create the rooms and place the items
        reception = Room("at the front desk")
        reception.set_name("front_desk")
        reception.set_item(box)
        reception.set_item_position('box',"next to the front desk")
        self.reception_copy = reception
        
        east_hallway = Room("in a east hallway")
        east_hallway.set_name("east_hallway")
        
        arrivals = Room("in the arrivals")
        arrivals.set_name("arrivals")
        self.arrivals_copy = arrivals
        
        atrium = Room("in the Atrium")
        atrium.set_name("atrium")
        self.atrium_copy = atrium
        
        east_restroom = Room("in the arrivals restroom")
        east_restroom.set_name("east_restroom")
        east_restroom.set_item(keycard_1)
        east_restroom.set_item_position("keycard-B29","on the restroom floor")
        
        security = Room("in the Security room")
        security.set_name("security")
        self.security_copy = security
        
        west_restroom = Room("in the main restroom")
        west_restroom.set_name("west_restroom")
        west_restroom.set_item(keycard_3)
        west_restroom.set_item_position("keycard-T07","in one of the sinks")
        
        west_hallway = Room("in the west hallway")
        west_hallway.set_name("west_hallway")
        west_hallway.set_item(box_1)
        west_hallway.set_item_position("box","on the hallway floor")
        
        
        cafeteria = Room("in the cafeteria")
        cafeteria.set_name("cafeteria")
        cafeteria.set_item(keycard_2)
        cafeteria.set_item(bar)
        cafeteria.set_item(water)
        cafeteria.set_item_position("keycard-R25","on the floor underneath a table")
        self.cafe_copy = cafeteria
        
        
        lab = Room("in the Teleportation RD Laboratory")
        lab.set_name("lab")
        lab.set_item(serum_69)
        lab.set_item_position("U-69","on the table next to the east exit")
        lab.set_item(serum_56)
        lab.set_item_position("U-56","on a shelf")
        lab.set_id("T06")
        lab.restrict(1)
        
        storage = Room("in equipment storage")
        storage.set_name("storage")
        storage.set_item(teleporter_)
        storage.restrict(1)
        storage.set_id("B29")
        
        marketing = Room("in the marketing offices")
        marketing.set_name("marketing")
        marketing.restrict(1)
        
        office = Room("you are in Mr.Samsa's Office")
        office.set_name("office")
        office.restrict(1)
        office.set_id("J27")
        self.office_copy = office
        
        teleporter = Transport_Room("in a faulty experimental teleporter")
        
        # initialise room exits
        reception.set_exit("west",atrium)
        reception.set_exit("east",east_hallway)

        east_hallway.set_exit("west", reception)
        east_hallway.set_exit("north", arrivals)
        east_hallway.set_exit("east", east_restroom)
        
        east_restroom.set_exit("west", east_hallway)
        
        arrivals.set_exit("south",east_hallway)
        arrivals.set_exit("east", lab)
        
       
        
        atrium.set_exit("west", west_hallway)
        atrium.set_exit("north", security)
        atrium.set_exit("south", cafeteria)
        atrium.set_exit("east", reception)
        
        
        security.set_exit("south",atrium)

        west_restroom.set_exit("east", west_hallway)
        
        west_hallway.set_exit("west", west_restroom)
        west_hallway.set_exit("north", marketing)
        west_hallway.set_exit("east", atrium)
        
        
        cafeteria.set_exit("north", atrium)
        
        lab.set_exit("west", arrivals)
        lab.set_exit("north", teleporter)
        lab.set_exit("east", storage)
        
        storage.set_exit("west",lab) 
        storage.set_item(box)
        
        marketing.set_exit("south", west_hallway)
        marketing.set_exit("north", office)
        
        self.current_room = reception  # start game at the front desk
        
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
        
        self.teleporter = teleporter #Room
        
        #add rooms to the portable teleporter list
        teleporter_.add_rooms(marketing)
        teleporter_.add_rooms(office)
        teleporter_.add_rooms(west_restroom)
        teleporter_.add_rooms(east_restroom)
        teleporter_.add_rooms(security)
        teleporter_.add_rooms(atrium)
        teleporter_.add_rooms(cafeteria)
        teleporter_.add_rooms(west_hallway)
        teleporter_.add_rooms(east_hallway)
        teleporter_.add_rooms(storage)
        teleporter_.add_rooms(reception)
        
        self.teleport_item = teleporter_ #Item
    
        
    def teleport(self):
        """  'teleport' transports the player to a random room in the game """
        if self.current_room == self.teleporter:
            self.current_room = self.teleporter.random_room()
            self.refresh()
            self.history.pop(-1)
        
    def play(self):
        """ Main play routine. Loops until end of play """
        while True:
            self.asset.intro_screen()
            self.asset.options()
            entry = self.int_input()
        
            if entry == 1:
                print("\n"*1000)
                self.asset.case = 1
                self.player.set_capacity(5.0)
                self.player.add_item(self.package)
                self.asset.print_plot()
                self.refresh()
                self.char_in_room()
        
                # Enter the main command loop.  Here we repeatedly read commands and
                # execute them until the game is over.      
                finished = False
                while finished == False:
                    self.add_to_history(self.current_room)
                    self.teleport()
                    command = self.parser.get_command()
                    if self.has_won() == True or self.process_command(command)== True:
                        finished = True
                        break
                    else:
                        finished = False
        
                if self.string == "won":
                    print("\n\nCONGRATULATIONS YOU WON!\nThank you for playing. Goodbye")
                    break
                else:    
                    print("\nYou quit the game.\nThank you for playing. Good bye.")
                    break
                
            elif entry == 2:
                self.asset.help_(1)
            elif entry == 3:
                print("\n"+"Exiting game. Good bye.")
                break
                
                
                

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
            print("\n[ I don't know what you mean. ]")
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
        elif command_word == "interact":
            self.character_interact(command)
        elif command_word == "back":
            self.back(command)
        elif command_word == "pick":
            self.player_interact(command)
        elif command_word == "open":
            self.player_interact(command)
        elif command_word == "unlock":
            self.player_interact(command)
        elif command_word == "drop":
            self.player_interact(command)
        elif command_word == "quit":
            want_to_quit = self.quit(command)
        
        return want_to_quit

    # implementations of user commands:

    def print_help(self):
        """ Print out some help information. """
        self.asset.help_(2)
        print("\n"*1000)
        self.refresh()



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
                print("[ Go where? ]")
                self.refresh()
                self.history.pop(-1)
                self.history.pop(-1)
                return

            direction = command.get_second_word()

            # Try to leave current room.
            next_room = self.current_room.get_exit(direction)

            if next_room == None:           # None is a special Python value that says the variable contains nothing
                print("[ There is no door! ]\n")
                self.history.pop(-1)
                self.refresh()
    
            elif next_room.is_restricted() == False:
                self.current_room = next_room
                self.refresh()
            
            else:
                self.refresh()
                self.history.pop(-1)
                print("\n[ The door is locked. Try using a keycard to unlock it ]")
      
    """
     * Go back to the previous room you were in, if you at the start
     * a message is shown informing you of this.
    """   
    def back(self, command):
        """ back allows the player to retrace their steps, by going backwards in each room
        the has already been
        
        Parameters
        ----------
        command: Command
            The command to be processed
        """
        if command.get_command_word() == "back":
            if len(self.history) <= 1:
                self.refresh()
                print("\n[ This is your start point ]")
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
    def player_interact(self, command):
        """ Try to interact with the items. If there is an item in the room, you can pick
        it up, if you have an item in your inventory you can drop the item and you can open
        your inventory to view the items you have, otherwise print an error message.

        Parameters
        ----------
        command: Command
            The command to be processed
        """
        count = 0
        exit_inventory = False
        entry = ""
        p = random.randint(0,49)
        r = random.randint(0,999)
        n = random.randint(0,9)
        
        if command.get_command_word() == "pick": #Allows the player to interact with items in the room
            if command.has_second_word() == False:
                print("[ Pick up what? ]")
                self.refresh()
                self.history.pop(-1)
                return
            if command.get_second_word() == "up":
                #Trying to pick up a specific item
                item = command.get_third_word()
                self.history.pop(-1)
                for items in self.current_room.items:
                    if item == items.get_name() and self.player.has_space(items.weight) != False:
                    
                        #The selected item is added to the player's inventory and  removed from the current room
                    
                        self.player.add_item(items)
                        self.current_room.pop_item(items)
                        self.refresh()
                        print("\n[ " + items.name + " has been added to your inventory ]\n")
                    
                    elif self.player.has_space(items.weight) == False:
                    
                        #This ensures that the set player limit is not exceeded                    
                        self.refresh()
                        print("\n[ You'll exceed your inventory capacity ]\n")
                    
                    elif item != items.get_name() and count == len(self.current_room.items):
                        self.refresh()
                        print("[ "+item + " is not in the area ]\n")
                    count += 1
            else:
                print("\n[ Are you trying to say 'pick up'? ]")
                self.refresh()
                self.history.pop(-1)
                
        elif command.get_command_word() == "drop": #Allows the player to drop an item in their inventory
            if command.has_second_word() == False: 
                print("[ Drop what? ]")
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
                    self.current_room.set_item(items)
                    self.refresh()
                    print("\n[ " + items.name + " has been drop from your inventory ]\n")
                    
                else:
                    self.refresh()
                    print("[ "+item + " is not in the your inventory ]\n")
                        
                        
        elif command.get_command_word() == "open": #Allows the player to view their inventory 
            if command.has_second_word() == False:
                print("[ Open what? ]")
                self.refresh()
                self.history.pop(-1)
                return
            
            #This is one of the special features of the game. It is a portable teleporter that allows the user to
            #Teleport whereever they want. you will have to find  it within the game.
            if command.get_second_word() == "teleporter":
                for item in self.player.inventory:
                    if item.name == "teleporter":
                        item.print_menu()
                        if item.can_teleport() == True:
                            self.current_room = item.next_room
                            self.history.pop(-1)
                            self.refresh()
            
                        else:
                            print("[ ERROR: INVALID COORDINATES RECIEVED ]\n[ SYSTEM FAILURE. SEQUENCE JHB-2910 ABORTED. ]")
                            self.history.pop(-1)
                            self.refresh()
                    else:
                        self.history.pop(-1)
                        print("\n\nYou dont have a teleporter.") 
                        self.refresh() 

            # Try and open inventory            
            elif command.get_second_word() == "inventory":
                if len(self.player.inventory) == 0:
                    self.refresh()
                    print("\n[ There are no items in your inventory ]")
                
                else:
                    item = None
                    print("\n" * 15)
                    self.inventory_options()
                    entry = input("> ")
                    split_str = entry.split(" ")
                    for i in self.player.inventory:
                        try:
                            if i.name  == split_str[1]:
                                item = i
                            else:
                                print("[ That is not in your inventory ]")
                        except IndexError:
                            print()
                                
                    while exit_inventory == False:
                    
                        if entry == "exit":
                            print("\n"*1000)
                            exit_inventory = True
                        elif item != None:        
                            if entry == ("show " + item.name): #try and view an items details i.e weight, description and name
                                print("\n" * 1000)
                                print(item.get_full_description())
                                print("\n Actions: back | exit | use |drop item")
                                entry = input("> ")
                                if entry == "back": #This back command only affects the inventory menu 
                                    print("\n" * 1000)
                                    self.inventory_options()
                                    entry = input("> ")
                                
                            elif entry == ("drop " + item.name): #This allows the player to drop and item from the inventory menu
                                self.player.pop_item(item)
                                self.current_room.set_item(item)
                                if len(self.player.inventory) == 0:
                                    exit_inventory = True
                                
                                else:
                                    self.inventory_options()
                                    entry = input("> ")
                                
                            elif entry == ("use " + item.name):
                                try:
                                    if item.type == "1A":
                                        if item.name == "U-69":
                                            self.player.pop_item(item)
                                            self.player.add_item(Item("testtube","empty test-tube",0.3))
                                            if r == 50:
                                                print("\n[ You drank the unknown serum ].\nYou died.\n")
                                                exit_inventory = True
                                            elif n == 4:
                                                print()
                                            else:
                                                self.inventory_options()
                                                print("\n[ You drank the unknown serum.Nothing happened ]\n")
                                                entry = input("> ")
                                            
                                    elif item.name == "U-56":
                                        print("\n[ You drank the unknown serum ]\n")
                                        self.player.pop_item(item)
                                        self.player.add_item(Item("testtube","empty test-tube",0.3))
                                        if p == 25:
                                            self.current_room = self.office_copy
                                            exit_inventory = True
                                        
                                        else:
                                            self.inventory_options()
                                            entry = input("> ")
                                        
                                    elif item.type == "1B":
                                        self.inventory_options()
                                        print("\n[ You ate the "+item.name+" ]\n")
                                        entry = input("> ")
                                
                                    elif item.type == "1C":
                                        self.inventory_options()
                                        print("\n[ You drank the "+item.name+" ]\n")
                                        entry = input("> ")
                                
                                except AttributeError:
                                    print("\n"*15)
                                    self.inventory_options()
                                    print("\n[ You can't use that ]\n")
                                    entry = input("> ")
              
                        else: #error message
                            print("\n"*20+"[ I dont know what you mean ]\n")
                            self.inventory_options()
                            entry = input("> ")
                                
                    self.history.pop(-1)
                    print("\n"*10)
                    self.refresh()
            else:
                self.history.pop(-1)
                self.refresh()
                print("[ I dont know what that means. ]")
                
                
        elif command.get_command_word() == "unlock": #Allows the player to interact with room exits
            if command.has_second_word() == False:
                print("[ unlock what? ]")
                self.refresh()
                self.history.pop(-1)
                return
            
            direction = command.get_second_word()
            next_room = self.current_room.get_exit(direction)
                
            if next_room == None:
                self.history.pop(-1)
                self.refresh()
                print("[ There is no door! ]\n")
    
            elif next_room.is_restricted() == False:
                self.history.pop(-1)
                self.refresh()
                print("\n[ You can only interact with locked doors ]")
                    
            else:
                print("enter action.")
                entry = input("> ")
                for item in self.player.inventory:
                    if entry == "swipe " + item.name:
                        if item.id == next_room.id:
                            next_room.restrict(0)
                            self.refresh()
                            self.history.pop(-1)
                            print("\n[ The "+ direction +" exit is now accessible ]\n")
                                
                        else:
                            self.refresh()
                            self.history.pop(-1)
                            print("\n[ Unknown identification card! ]")
                    else:
                        print("\n[ Please use a keycard! ]\n")
                                
        else:
            print("[ I dont know what that means ]")
            
    """
     * Allows interactions with character in the room
    """           
    def character_interact(self,command):
        count = 1
        case = 0
        item = Item("","",0)
        char = Character("","")
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
                print("give what?")
                self.refresh()
                self.history.pop(-1)
                return
            
            self.history.pop(-1) 
            for npc in self.char_list: #check if the character exists
                if npc.name == command.get_second_word():
                    char = npc

            if command.get_second_word() == char.name and char.current_room == self.current_room:
                if char == self.receptionist:
                    for i in self.player.inventory: #check if the item exists
                        if i.name == command.get_third_word():
                            item = i
                    
                    if item.name == "chip" and case == 0:
                        case = 1
                        self.player.pop_item(item)
                        char.add_item(item)
                        print("\n\n[ You have given the "+ char.name+", the silver chip ]\n")
                        print("Receptionist:\n"+" Thank you, now you can hand in the package.")
                        self.refresh()
                      
                    elif case == 0 and (self.chip not in char.inventory) == True:
                        print("\n\nReceptionist:")
                        print(" Sorry, I cannot take the package without the chip.")
                        self.refresh()
                            
                    elif item.name == "package":
                        char.inventory.pop(0)
                        char.add_item(item)
                        self.player.pop_item(item)
                        print("\nReceptionist:\nThank you and have a great day.")
                    
                    else:
                        print("\nReceptionist:\n You can hand in the package now")
                        self.refresh()
                        
                elif char == self.security:
                    for i in self.player.inventory: #check if the item exists
                        if i.name == command.get_third_word():
                            item = i
                            
                    if item.name == "document":
                        char.add_item(item)
                        self.player.pop_item(item)
                        print("\n"*2+"[ You have given "+char.name.title()+" a delivery form ]\n\n")
                        self.player.add_item(char.inventory[0])
                        char.pop_item(item)
                        print(char.name.title()+":\n"+" Thanks, Now take that sliver chip to the front desk.")
                        print("\n"*2+"[ A silver chip has been added to your inventory ]")
                        self.refresh()
                    
                    else:
                        print("\n\n"+char.name.title()+":\n"+" Can you bring me the form first.")
                        self.refresh()     
                else:    
                    for item in self.player.inventory: #check if the item exists
                        if command.get_third_word() == item.name:
                            char.add_item(item)
                            self.player.pop_item(item)
                            self.refresh()
                            print("\n[ You have given "+char.name+", a "+item.name+" ]")
                 
                        else:
                            self.refresh()
                            print("\n[ ", command.get_third_word(),"is not in your inventory ]")
            else:
                print("\n[ I dont know who that is ]")
                self.refresh()
        
        if command.get_command_word() == "interact":
            if command.has_second_word() == False:
                print("[ interact with who? ]")
                self.refresh()
                self.history.pop(-1)
                return
            
            if command.get_second_word() == "with":
                for ch in self.char_list: #check if the character exists
                    if ch.name == command.get_third_word():
                        char = ch
                    elif count > len(self.char_list):
                        print("[ I dont know who that is ]")
                        count = 1
                        break
                    count += 1
                        
                if char.name == self.receptionist.name and char.current_room == self.current_room:
                    if char.dialogue_counter == 0:
                        char.dialogue_counter += 1
                        print("\n")
                        response = char.response[1]
                        for string in response:
                            print(str(string))
                        print("\n")
                        
                        choice = self.int_input()
                        
                        if choice == 1:
                            print("Receptionist:\n I have to let you know that due to security reasons all deliveries \n have to be inspected by our security officer."
                                  "After inspection a\n silver chip will be given to you. hand in the chip with\n the delivery"+
                                  " and you'll be on your way.\n"
                                  "\n1) Okay\n2) Where is the security room ")
                            
                            entry = self.int_input()
                                
                            if entry == 2:
                                print("\nReceptionist:\n The security room is through the west exit\n"
                                      " into the atrium taking the north exit.")
                                  
                            elif entry == 1:    
                                print("\nReceptionist:\n Have a great day.")
      
                        elif choice == 2:
                            print("\nReceptionist:\n To get the closest restroom take the east exit,"
                                    "\n into the east hallway then take the east exit.")
                            char.dialogue_counter  = 0
                        else:          
                            print ("\n[ Invalid Input ]\n")
                            
                    elif char.dialogue_counter == 1:
                        char.dialogue_counter += 1
                        print("\nReceptionist:\n Hi again, did you manage to get the silver chip?\n"
                              "\n1)Yes"
                              "\n2)No")
                        
                        entry = self.int_input()
                        
                        if entry == 1:
                            print("\nReceptionist:\n Please hand it in to complete your delivery.")
                                
                        elif entry == 2:
                            print("\nReceptionist:\n Please come back when you have chip with you, thank you. ")
                            
                    elif char.dialogue_counter == 2:
                        print("\nReceptionist:\n Sorry, no time to chat we are just so busy today,",
                              "please on come back when you have the chip with you.")
                        
    
                elif char.name == self.security.name and char.current_room == self.current_room:
                    if char.dialogue_counter == 0:
                        char.dialogue_counter += 1
                        response = char.response[0]
                        print("\n"*2)
                        print(response)
                    
                        entry = self.int_input()
                        if entry == 1:
                            print("\n"*2+char.name.title()+":\n"" Alright, I'll need a delivery form first.")
                            print("\n\n1) Where can I get this form from?")
                            print("2) This does not seem very efficient?")
                            entry = self.int_input()
                            if entry == 1:
                                print("\n"*2+char.name.title()+":")
                                print(" Go to the arrivals and talk to Mr.Bore, he will give you the delivery form.\n")
                            elif entry == 2:
                                char.dialogue_counter = 0
                                print("\n"*2+char.name.title()+":")
                                print(" I'm just the security, you best take that up with the administration.\n")
                                
                            elif entry > 2:
                                print("\n[ Invalid entry ]\n")
                                
                        elif entry == 2:
                            char.dialogue_counter = 0
                            print("\n"*2+char.name.title()+":")
                            print(" No idea, I think marketing or something of the sort.\n I dont get paid to ask questions.\n")
                        
                            
                    elif char.dialogue_counter == 1:
                        print("\n"*2+char.name.title()+":")
                        print(" Did you manage to get the delivery form?\n")
                        print("1) Where is Arrivals again?")
                        print("2) Yes, here it is.")
                        entry = self.int_input()
                        if entry == 1:
                            print("\n"*2+char.name.title()+":")
                            print(" It is east of the reception, then north of the hallway."
                                  "\n Talk to Mr.Bore when you are in there.\n")
                            
                        elif entry == 2:
                            if self.form in self.player.inventory:
                                item = self.linear_search(self.player.inventory,"document")
                                self.player.pop_item(item)
                                print("\n[ A delivery form has been removed from your inventory ]")
                                char.add_item(item)
                                self.player.add_item(char.inventory[0])
                                print("\n"+char.name.title()+":")
                                print(" Give this silver chip to the receptionist before you deliver the package.")
                                print("\n\n[ A silver chip has been added to your inventory ]\n")
                                
                            else:
                                print("\n"*2+char.name.title()+":")
                                print(" Please only comeback when you have the form with you.")
                        
                        elif entry > 2:
                            print ("\n[ Invalid entry ]\n")
                    

                elif char.name == self.researcher_1.name and char.current_room == self.current_room:
                    print("\n"*2+char.response[2])
                    entry = self.int_input()
                    if entry == 1:
                        char.dialogue_counter += 1
                        item = self.linear_search(char.inventory,"keycard-T07")
                        
                        if item == None:
                            print("\n"*2+char.name.title()+":")
                            print("No it is not, thank you for trying to help.")
                            
                        else:
                            print("\n"*2+char.name.title()+":")
                            print("Yes thats my keycard, thank you.")
                            self.player.pop_item(item)
                            char.add_item(item)
                            print ("\n[ Keycard-T07 has been removerd from your inventory ]\n")
                            print("\n"*2+char.name.title()+":")
                            print("Here have this, Hope it was the trouble.\n")
                            print ("\n[ $15 has been added to your inventory ]")

                elif char.name == self.clerk.name and char.current_room == self.current_room: 
                    if char.dialogue_counter == 0:
                        print("\n"*2)
                        print(str(char.response[3]))
                        entry = self.int_input()
                        if entry == 1:
                            char.dialogue_counter += 1
                            item = self.linear_search(self.clerk.inventory,"document")
                            self.player.add_item(item)
                            print("\n"*2+char.name.title()+":")
                            print(" There you go have a nice day.\n")
                            print("[ A delivery form has been added to your inventory ]\n")
                        elif entry == 2:
                            print("\n"*2+char.name.title()+":")
                            print(" The cafeteria, or the bagel store across the road.\n")
                        elif entry > 2:
                            print("\n[ Invalid entry ]\n")
                        
                    elif char.dialogue_counter == 1:
                        print("\n"*2+char.name.title()+":")
                        print(" Hi again.\n")
                    
                else:
                    r = random.randint(0,2)
                    if char.dialogue_counter == 0:
                        char.dialogue_counter += 1
                        responses = char.response[4]
                        print("\n"*2)
                        print(responses[r])
                        
                    elif char.dialogue_counter == 1:
                        char.dialogue_counter = 0
                        print("\n"*2+char.name.title()+":")
                        print(" Hey there.")
                        
            self.history.pop(-1)
            self.refresh()
                
            
    def inventory_options(self):
        #print the inventory of the player        
        self.player.print_inventory()
        print("\n Actions: show item | use item | drop item | exit")
    
    def linear_search(self, List,reference):
        Element = None
        for element in List:
            if element.name == reference:
                Element = element
        return Element
        
    def int_input(self):
        choice = 0
        while True:
            try:
                choice = int(input("> "))
                break
            except ValueError:
                print("[ Invalid input, please try again ]")
        return choice    
        
        
    def has_won(self):
        # case 1
        
        for item in self.receptionist.inventory:
            if item.id == "T19":
                self.string = "won"
                return True
            else:
                return False
            
        for item in self.office_copy.items:
            if item.id == "T19":
                self.string = "won"
                return True
            else:
                return False

    def quit(self, command):
        """ "Quit" was entered. Check the rest of the command to see whether we really quit the game.

        Parameters
        ----------
        command: Command
            The command to be processed
        
        Returns true, if this command quits the game, false otherwise.
        """
        if command.has_second_word():
            print("[ Quit what? ]")
            return False
        else:
            return True  # signal that we want to quit
