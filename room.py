from item import  Item
import random

"""
 * Room Class
 * ----------------------------------------------------------
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
        self.characters = []
        self.case = False
        self.id = ""
        self.rm_name = ""
    
    def set_name(self, name):
        """
        set_name" sets the name of a room.

        Parameters
        ----------
        name: String
            name of the room
            
        """
        self.rm_name = name
        
    def set_item(self,item):
        """
        set_item" sets an item in a room.

        Parameters
        ----------
        name: String
            name of the item
        
        description: String
            description of  the item
        
        weight: float
            weight of the item

        """
        self.items.append(item)
     
    def get_name(self):
        """

        "get_name" returns the name of room
        
        """
        return self.rm_name
        
    def get_item(self,name):
        """
        get_item" returns a particular item in a room.

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
        """
        pop_item" returns a particular item in a room.

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
        """
        set_position" sets the location of an item in a room.

        Parameters
        ----------
        name: String
            name of the item
        
        position: String
            position of the item in the room
        """
        for i in range(len(self.items)):
            Item.set_position(self.items[i],name,position)
        
    def set_id(self,key):
        """ """
        self.id = key

    def set_exit(self, direction, neighbour):
        """
        Define an exit from this room.

        Parameters
        ----------
        direction: string
            The direction of the exit
        neighbour: Room
            The room to which the exit leads
        """
        self.exits[direction] = neighbour
        

    def get_short_description(self):
        """
        Returns The short description of the room
        (the one that was defined in the constructor).
        
        """
        return self.description

    def get_id(self):
        """ "get_id" returns the room id """
        return self.id

    def get_long_description(self):
        """
        Return a description of the room in the form:
        You are in the kitchen.
        Exits: north west
        
        Returns A long description of this room
        
        Expected_string : You are in the "Room" , Character, Character and Character are in this area.
                          there is an item somewhere and an item somewhere else.
                          exits: north east
        """

        first_string = "You are " + self.description 
        char_description = ""
        item_description = ""
        end_string = self.get_exit_string()
        full_string = ""
        
        if len(self.characters) > 0:
            for i in range(len(self.characters)):
                if self.characters[i] == self.characters[-1] and len(self.characters) > 1:
                    char_description += "and " + self.characters[i].name.title() + " are in this area."
                
                elif len(self.characters) == 1:
                    char_description += self.characters[0].name.title() + " is in the area."
                    
                elif len(self.characters) == 2:
                    char_description +=  self.characters[i].name.title()+" "
                    
                elif len(self.characters) > 2 :
                    char_description += self.characters[i].name.title() + ", "
           
        if len(self.items) > 0:
            for i in range(len(self.items)):
                if len(self.items) == 1:
                    item_description += "There is a "+ Item.get_item_info(self.items[0])+"."
                    
                elif self.items[i] == self.items[-1] and len(self.items) > 1:
                    item_description += " and a "+ Item.get_item_info(self.items[i])
                    
                elif len(self.items) == 2:
                    item_description += "a " + Item.get_item_info(self.items[i])
                    
                elif len(self.items) > 2:
                    item_description += "There is " + Item.get_item_info(self.items[i]) + "\n"
                    
        if len(self.items) > 0 and len(self.characters)== 0:
            full_string = first_string +", "+ item_description +"\n"+end_string
        
        elif len(self.items) == 0 and len(self.characters) > 0:
            full_string = first_string +", "+ char_description +"\n"+end_string
            
        elif len(self.items) > 0 and len(self.characters) > 0: 
            full_string = first_string +", "+char_description +"\n"+item_description +" \n"+end_string
            
        else:
            full_string = first_string+ "." + " \n" +end_string
            
        return full_string
        
              

    def get_exit_string(self):
        """
        Return a string describing the room's exits, for example
        "Exits: north west".
     
        Returns Details of the room's exits.
        
        """
        return_string = "Exits:"
        for room_exit in self.exits.keys():
            return_string += " " + room_exit
        return return_string

    """
         Return the room that is reached if we go from this room in direction
         direction". If there is no room in that direction, return None.
         direction The exit's direction.
         Returns The room in the given direction.
         
    """
    
    def get_exit(self, direction):
        """
            Return the room that is reached if we go from this room in direction
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
            
    def restrict(self,state):
        """
            "restrict" locks or unlocks a room exit depending on the user setting,i.e. if the user
            sets a room to 0 the room is unlocked and if the room is set to 1 it is locked
            
            Parameters
            -----------
            
            state : Int
            
            state is an integer value to set the state of the room exit. yes we could have used bool :).
            
        """
        try:
            if state == 0:
                self.case = False
            elif state == 1:
                self.case = True
            return self.case
        except state > 1:
            print("Value not valid")

    def is_restricted(self):
        """
            "is_restricted" checks if the room is restricted or not and returns
            "True" if restricted and "False" if otherwise
        
        """
        if   self.case == True:
            return True
        else:
            return False



class Transport_Room(Room):
    """
        A "Transport_Room" represents a room in the game that allows the player to
        teleport from one room to the other. Transport_Room is a subclass of Room
    """
    def __init__(self,description):
        super().__init__(description)
        self.rooms = []
        
    def random_room(self):
        """
            "random_room" generates a random number that from 0 to how every  any rooms
            are in the game. This number is used to select the room to teleport to.
        """
        r = random.randint(0, len(self.rooms)-1)
        return self.rooms[r]
    
    def add_rooms(self, room):
        """
            "add_rooms" adds rooms to the list rooms, these roomsare used as a reference for
            "random_room"
        """
        self.rooms.append(room)
    
    def get_rooms(self,room):
        """
        "get_rooms" this function is used to return the next room
        
        """
        next_room = None
        for rooms in self.rooms:
            if room == rooms:
                next_room = rooms
        return next_room
    