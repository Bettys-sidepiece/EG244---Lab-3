from item import item
"""
 * Class Room - a room in an adventure game.
 *
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
        name = item(name, description, weight)
        self.items.append(name)
        
        
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
            item.set_position(self.items[i],name,position)
        
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
            
            item_defination = item.get_item_info(self.items[0])
            return "You are " + self.description + ".\nThere is a " + item_defination + ".\n" + self.get_exit_string()
        
        else :
            first_string = "You are " + self.description
            item_defination = ""
            
            for i in range(len(self.items)):
                
                if self.items[i] == self.items[-1]:
                    item_defination += "a " + item.get_item_info(self.items[i])
                elif len(self.items) == 2 :
                    item_defination += "a " + item.get_item_info(self.items[i]) + " and "
                else :
                    item_defination += "a " + item.get_item_info(self.items[i]) + ", "
                
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
