"""
* This is the Item class
*
* It is used to create items to be placed in a room,
* players inventory, given to or by a character.
"""
class item():
    
    def __init__(self, name, description, weight):
        ""
        self.name = name
        self.weight = weight
        self.description = description
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
        #This method sets the position of an item
        if name == self.name :
            self.position = position
        
        
    def get_position(self):
        #This method retrieves the position of an item
            
        return self.position
    
    
    def get_weight(self):
        #This method retrieves the weight of an item
        
        return self.weight
        
    def get_description(self):
        #This method retrieves the description of an item
        
        return self.description
    
    
    def get_name (self):
        #This method retrieves the name of an item
        return self.name
    
    
    def get_item_info(self):
        #This method retrieves the information of an item
        
        return self.name +  " " + self.position
    
    
    def get_full_description(self):
        #This method retrieves the full description of an item
        #This is method is to be used by the player
        
        return self.name + "\n " + self.description + "\n Weight: " + str(self.weight)