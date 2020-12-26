"""
 * Class Item
 ---------------------------------------------------------------------------------------------------------
 * This class is part of The Delivery, text based adventure game.  
 * An "Item" represents an intractable object in the game. Items can be found in rooms or on characters.
 * Items can also be held in the players inventory and can be used to access doors in the case of keycards
 * or trade for other items
 *  
"""
class Item():
    
    def __init__(self,name,info,weight):
        """
            Create an item described by "name", "info - description".
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
        """
            "set_position" sets the location of an item in a room.

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
        """
            Returns the position of  the item in the room
            (the one that was defined in the constructor).
            
        """
            
        return self.position
    
    
    def get_weight(self):
        """
            Returns the weight of the item.
            (the one that was defined in the constructor).
            
        """
        return self.weight
        
        
    def get_info(self):
        """
            Returns the description of the item.
            (the one that was defined in the constructor).
            
        """
        return self.info
    
    
    def get_name (self):
        """
            Returns the name of the item.
            (the one that was defined in the constructor).
            
        """
        return self.name
    
    
    def get_item_info(self):
        """
            Returns a string of the name and position of the item.
            (the one that was defined in the constructor).
            
        """
        
        return self.name +  " " + self.position
    
    
    def get_full_description(self):
        """This method retrieves the full description of an item """
     
        return self.name + "\n " + self.info + "\n Weight: " + str(self.weight)


class Consumable(Item):
    """
        The consumable class is a subclass of the item class.
        this class describes items that the player can use i.e.
        consume and experience and  effect.
        
    """
    def __init__(self,name,info,weight):
        super().__init__(name,info,weight)
        self.health_points = 0
        self.type = " "
        
    def set_type(self, item):
        
        self.type = item
        
    def get_type(self):
        
        return self.type
        
        
class Key(Item):
    """
        The key class is a subclass of the item class. The key class describes
        items hows purpose is to unlock a door or feature within the game. for example,
        a key can be a literal key or it can be an item the player has to give to a charecter
        to complete a task.
    """
    def __init__(self, name, info, weight):
        super().__init__(name,info,weight)
        self.id = ""
    
    
    def set_id(self,lock):
        """ set_id, is meant to set the a unique identification string
            this string is compared to  the string each room has if it
            is restricted.
            
            Parameters
            ----------
            lock : String
            
            lock is the ID string expected from the room
        """
        self.id = lock
    
    def get_id(self):
        """ get_id returns the identification string of the key"""
        return self.id
            
    
class teleport(Item):
    """
        The teleport class is a sub-class of the item class.
        This class is is similar to the transport room class
        in that the item teleports the player to any room in
        in the game.
    """
    def __init__(self, name, info, weight):
        super().__init__(name,info,weight)
        self.rooms = []
        self.next_room = None
        self.rm_name = ""
        
        
    def add_rooms(self, rooms):
        """
        add_rooms adds rooms to the rooms list, this allows the
        teleporter to have a reference of the rooms in the game.
        
        Parameter
        ---------
        rooms : Room
        
        rooms is a Room in the game
        
        """
        if rooms not in self.rooms: #checks if the room is already in the list
            self.rooms.append(rooms)
             
    def can_teleport(self):  
        if self.next_room.rm_name == self.rm_name:
            return True
        else:
            return False
        
    def get_rooms_string(self):
        string  = ""
        newline = 0
        
        for room in self.rooms:
            if newline < 2:
                string += room.rm_name.title() + " | "
                newline += 1
                    
            elif newline == 2:
                string += room.rm_name.title() + "\n"*2
                newline = 0
                
            elif room == self.rooms[-1]:
                string += room.rm_name.title()
                newline =  0
                
        return string
        
        
    def print_menu(self):
        """print_rooms_list displays the possible rooms for teleportation"""
        rm = None
        case = False
        exit_menu = False
        while exit_menu == False:
            print("\n"*10,"\n--------------------------------------------\n"
                    ,self.get_rooms_string(),
                  "\n-----------------------------------------------")
            print("\ngoto room | exit")
                
            entry = input("> ")
            split = entry.split(" ")
            print(split)
            for room in self.rooms:
                if room.rm_name == split[1]:
                    rm = room
                    case = True
                    
            if entry == ("goto " + rm.rm_name) and case == True:
                self.rm_name = rm.rm_name
                self.teleport(rm)
                exit_menu = True
                break
            elif entry == "exit":
                exit_menu = True
                break
            else: 
                print("\n"*10,"\n--------------------------------------------\n"
                    ,self.get_rooms_string(),
                  "\n-----------------------------------------------")
                print("\ngoto room | exit")
                print("\nI dont know what you mean...")
                entry = input("> ")
            
        
    def teleport(self,room):
        """
            teleport sets the room selected by the player as the next room
            
            Parameters
            ----------
            room : Room
            
            room is the selected Room
            
        """
        for rm in self.rooms:
            if room == rm:
                self.next_room = room
            else:
                print("")