import random
"""
 * Room Class
 * ----------------------------------------------------------
 * This class is part of the "World of Zuul" application. 
 * "World of Zuul" is a very simple, text based adventure game.  
 *
 * A "Room" represents one location in the scenery of the game.  It is 
 * connected to other rooms via exits.  For each existing exit, the room 
 * stores a reference to the neighboring room.
 * 
"""

class Room():
    """ A "Room" represents one location in the scenery of the game.  It is 
    connected to other rooms via exits.  For each existing exit, the room 
    stores a reference to the neighboring room.
    """

    def __init__(self, description):
        """ Create a room described "description". Initially, it has
        no exits. "description" is something like "a kitchen" or
        "an open court yard".

        Paramaters
        ----------
        description: string
            The room's description
        """
        self.description = description
        self.exits = {}
        self.items = []
        self.rm_name = ""
    
    def set_name(self, name):
        
        self.rm_name = name
        
    def set_item(self, name, description,weight):
        """set_position" sets the location of an item in a room.

        Parameters
        ----------
        name: String
            name of the item
        
        description: String
            description of  the item
        
        weight: float
            weight of the item

        """
        name = Item(name, description, weight)
        self.items.append(name)
     
    def get_name(self):
        
        return self.rm_name
        
    def get_item(self,name):
        """get_item" returns a particular item in a room.

        Parameters
        ----------
        name: item
            Address of the chosen item
        """
        item = None
        count = 0
        for items in self.items:
            if name == items:
                item = self.items[count]
            count += 1
        return item
    
    
    def pop_item(self,name):
        """pop_item" returns a particular item in a room.

        Parameters
        ----------
        name: Item
            Address of the chosen item
        """
        count = 0
        for items in self.items:
            if name == items:
                del self.items[count]
            count += 1
        
        
    def set_item_position(self,name,position):
        """set_position" sets the location of an item in a room.

        Parameters
        ----------
        name: String
            name of the item
        
        position: String
            position of the item in the room
        """
        for i in range(len(self.items)):
            Item.set_position(self.items[i],name,position)
        
        
    def set_exit(self, direction, neighbour):
        """ Define an exit from this room.

        Parameters
        ----------
        direction: string
            The direction of the exit
        neighbour: Room
            The room to which the exit leads
        """
        self.exits[direction] = neighbour
        

    def get_short_description(self):
        """ Returns The short description of the room
        (the one that was defined in the constructor).
        """
        return self.description


    def get_long_description(self):
        """ Return a description of the room in the form:
        You are in the kitchen.
        Exits: north west
        
        Returns A long description of this room
        """
        
        if len(self.items) == 0:
            
            return "You are " + self.description + ".\n" + self.get_exit_string()
        
        elif len(self.items) == 1:
            
            item_defination = Item.get_item_info(self.items[0])
            return "You are " + self.description + ".\nThere is a " + item_defination + ".\n" + self.get_exit_string()
        
        else :
            first_string = "You are " + self.description
            item_defination = ""
            
            for i in range(len(self.items)):
                
                if self.items[i] == self.items[-1]:
                    item_defination += "a " + Item.get_item_info(self.items[i])
                elif len(self.items) == 2:
                    item_defination += "a " + Item.get_item_info(self.items[i]) + " and "
                else :
                    item_defination += "a " + Item.get_item_info(self.items[i]) + ", "
                
            return first_string + ".\nThere is " + item_defination + ".\n" + self.get_exit_string()


    def get_exit_string(self):
        """ Return a string describing the room's exits, for example
        "Exits: north west".
     
        Returns Details of the room's exits.
        """
        return_string = "Exits:"
        for room_exit in self.exits.keys():
            return_string += " " + room_exit
        return return_string

    """
     * Return the room that is reached if we go from this room in direction
     * "direction". If there is no room in that direction, return None.
     *     direction The exit's direction.
     *     Returns The room in the given direction.
    """
    
    def get_exit(self, direction):
        """ Return the room that is reached if we go from this room in direction
        "direction". If there is no room in that direction, return None.

        Parameters
        ----------
        direction: string
            direction The exit's direction.
        
        Returns The room in the given direction.
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None        # None is a special Python value that says the variable contains nothing
    

class Transport_Room(Room):
    """ A "Transport_Room" represents one location in the scenery of the game.  It is 
    connected to other rooms via exits.  For each existing exit, the room 
    stores a reference to the neighboring room.
    """
    def __init__(self,description):
        super().__init__(description)
        self.rooms = []
        
    def random_room(self):
        r = random.randint(0, len(self.rooms)-1)
        return self.rooms[r]
    
    def add_rooms(self, room):
        self.rooms.append(room)
    
    def get_rooms(self,room):
        next_room = None
        for rooms in self.rooms:
            if room == rooms:
                next_room = rooms
        return next_room
    

"""
 * Class Item
 ---------------------------------------------------------------------------------------------------------
 * This class is part of -----, text based adventure game.  
 * An "Item" represents an intractable object in the game. Items can be found in rooms or on characters.
 * Items can also be held in the players inventory and can be used to access doors in the case of keycards
 * or trade for other items
 *  
"""
class Item():
    
    def __init__(self,name,info,weight):
        """ Create an item described by "name", "info - description".
        Initially, it has a position of "Somewhere in the area".
        "name " is something like "ball" or "keycard".
        
        "info" describes the utility of the items for example,
        a "key" can have info like "unlocks doors"
        
        "weight" describes how heavy the item is. The weight of an
        item accumulates and if limited by a characters/ players
        carry capacity

        Paramaters
        ----------
        name: string
            The item's name
        
        info: string
            The item's description
            
        weight: float
            The item's weight
        """
        self.name = name
        self.info = info
        self.weight = weight
        self.position = "somewhere in the area"
        
        
    def set_position(self,name,position):
        """ "set_position" sets the location of an item in a room.

        Parameters
        ----------
        name: String
            name of the item
        
        position: String
            position of the item in the room
        
        initialises the position attribute
        """
        if name == self.name :
            self.position = position
        
        
    def get_position(self):
        """ Returns the position of  the item in the room
        (the one that was defined in the constructor).
        """
            
        return self.position
    
    
    def get_weight(self):
        """ Returns the weight of the item.
        (the one that was defined in the constructor).
        """
        return self.weight
        
        
    def get_info(self):
        """ Returns the description of the item.
        (the one that was defined in the constructor).
        """
        return self.info
    
    
    def get_name (self):
        """ Returns the name of the item.
        (the one that was defined in the constructor).
        """
        return self.name
    
    
    def get_item_info(self):
        """ Returns a string of the name and position of the item.
        (the one that was defined in the constructor).
        """
        
        return self.name +  " " + self.position
    
    
    def get_full_description(self):
        """This method retrieves the full description of an item """
     
        return self.name + "\n " + self.info + "\n Weight: " + str(self.weight)

class Consumables(Item):
    def __init__(self,name,info,weight):
        super().__init__(name,info,weight)
        self.health_points = 0
        self.effect = 0.0
        
class Key(Item):
    
    def __init__(self, name, info, weight):
        super().__init__(name,info,weight)
        self.pair = {}
    
    def set_pair(self, key, lock):
        
        self.pair[key.name] = lock
        
    def check_lock(self, room):
        
        for lock in self.pair:
            if room == lock:
                return True
                
            else:
                return False
            
            
        
class teleporter(Item):
    
    def __init__(self, name, info, weight):
        
        super().__init__(name,info,weight)
        self.rooms = []
        
    def add_rooms(self, rooms):
        if rooms not in self.rooms:
            self.rooms.append(rooms)
            
    def print_rooms_list(self):
        rooms = ""
        exit_menu = False
        for room in self.rooms:
            rooms += room.description +"\n"
            while exit_menu == False:
                print(rooms+"\n")
                print("goto room | exit")
                entry = input("> ")
                if entry == "goto" and room.rm_name:
                    self.teleport(room)
                    
                elif entry == "exit":
                    exit_menu = True
                else:
                    print("I dont know what you mean...")
                    print(rooms+"\n")
                    print("goto room | exit")
                    entry = input("> ")
            
    def teleport(self,room):
        next_room = None
        for rm in self.rooms:
            if room == rm:
                next_room = rm
        return next_room
        
        
        
"""
 * Character Class
 ---------------------------------------------------------------------------------------------------------
 * This class is part of -----, text based adventure game.  
 * A "Character" represents an intractable character in the game. characters can be found in rooms.
 * Characters sometimes hold items and can willing give and recieve items. characters move randomly
 *  
"""  
class Character():
        
    def __init__(self,name,description):
        
        """ Create a character is described by "name" and "description". "name" is the name of the character.
        "description" is the  description of the  character. The characters have a reference to their current
        room via the current_room attribute. The move method allows a characterto randomly move within the game
        the inventory is a list that stores the items a character has.
        Paramaters
        ----------
        name: string
            The item's name
        
        description: string
            The item's description
        """
        self.name = name
        self.description = description
        self.capacity = 2.0
        self.current_room = Room("None")
        self.total = 0
        self.inventory  = []
        self.move()
    
    def set_current_room(self,room):
        """
        this method sets the characters current room
        
        Paramaters
        ----------
        room: Room
            the characters current room
        """
        self.current_room = room
        
    def set_capacity(self, capacity):
        """
        this method sets the characters capacity
        
        Paramaters
        ----------
        capacity: float
            the characters current room
        """
        self.capacity = capacity
           
    def set_total(self,item):
        """
        this method sums the weight of items each time an item is added to the charecter
        
        Paramaters
        ----------
        room: Room
            the characters current room
        """
        self.total = self.total + item
       
    def get_capacity(self):
        """ Returns the characters inventory capacity"""
        return self.capacity
    
    def get_total(self):
        """ Returns the characters summed inventory weight"""
        return self.total
      
    def has_space(self, weight):
        """
        Checks if an item is too heavy to be added to the inventory
        
        Parameter
        ---------
        weight: float
        
        Returns: boolean
        """
        total = 0
        total = self.total + weight
        if total > self.capacity:
            return False
        else:
            return True
        
    def add_item(self, item):
        """
        Adds items to the inventory and adds the item's weight to the weight
        
        Parameters
        -------------
        item: Item
            item to be added
        """
        self.set_total(item.weight)
        self.inventory.append(Item(item.name,item.info,item.weight))
        
    def get_current_room(self):
        """returns the characters current room"""
        return self.current_room
    
    def is_current_room(self,room):
        """
        Checks if the player's current room is the same as the characters
        
        Parameter
        ---------------
        room : Room
            Room that is being compared
        
        returns : boolean
        """
        if self.current_room.get_short_description() == room.get_short_description():
            print((self.name).title()+" is in the the area")
            return True
        else:
            return False
    
    def next_room(self,direction):
        """
        Gets the next avaliable room depending on the result of the move() method.
        if the result is valid the character moves to the next room.otherwise they don't
        
        Parameters
        ---------------
        direction : string
            string of the direction
        return : Boolean (this return is there for debugging)
        """
        next_room = self.current_room.get_exit(direction)
        if next_room == None:
            return False
        else:
            self.current_room = next_room
            return True
    
    def move(self):
        """ This method is meant to randomly move the character by generating
            a number from 0 to 3 which determines the direction of movement this
            result is then evaluated by the next_room() method.
        """
        r = random.randint(0,3) #generate a random number between 0 - 3
        
        if r == 0:
            self.next_room("north")
        
        elif r == 1:
            self.next_room("south")
            
        elif r == 2:
            self.next_room("east")
            
        elif r == 3:
            self.next_room("west")
            
