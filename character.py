from room import Room
import random
"""
 * Character Class
 ---------------------------------------------------------------------------------------------------------
 * This class is part of The delivery, text based adventure game.  
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
        self.dialogue_counter = 0
        self.response = []
        self.inventory = []
        self.responses()
    
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
        self.inventory.append(item)
        
    def pop_item(self,name):
        """This method removes an item from the characters inventory
            
            Parameters
            ------------
            name : string
                name of the item being removed
        """
        count = 0
        for items in self.inventory:
            if name == items:
                self.total = self.total - self.inventory[count].weight
                del self.inventory[count]
            count += 1
        
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
        if next_room == None or next_room.is_restricted() == True:
            return False
        else:
            self.current_room = next_room
            return True
    

    def move(self):
        """ This method is meant to randomly move the character by generating
            a number from 0 to 3 which determines the direction of movement this
            result is then evaluated by the next_room() method.
        """
        r = random.randint(0,15) 
        r += r 
        if r > 20:
            r = 0
            n = random.randint(0,3)#generate a random number between 0 - 3
            if n == 0:
                self.next_room("north")
                n = 0 
        
            elif n == 1:
                self.next_room("south")
                n = 0 
            
            elif n == 2:
                self.next_room("east")
                n = 0
            
            elif n == 3:
                self.next_room("west")
                n = 0
                
    def responses(self):
        
        string_1 = (self.name.title()+":\n"+" What can I help you with?\n"+
                    "\n1) I need a silver chip to deliver this package."+
                    "\n2) What does rigdeworks do?")
        self.response.append(string_1)

        string_2 = (self.name.title()+":\n"+"Hello, welcome to RidgeWorks, what can i help you with?\n",
                         "1) Hi, I am here to deliver a package addressed to Mr.Samsa.",
                         "2) Where are your restrooms."
                        )
        self.response.append(string_2)

        string_3 = (self.name.title()+":\n"+" I need help finding my keycard, have you seen it?\n"+
                         "\n1) Yes, is this your keycard?"+
                         "\n2) No I havent seen it, I'll keep an eye out."
                        )
        self.response.append(string_3)
        
        string_4 = (self.name.title()+":\n"+" Hello, What can i help you with today?"+
                         "\n1) I need a delivery form"+
                         "\n2) Where can i get a bite eat"
                        )
        self.response.append(string_4)
        
        string_5 = (self.name.title()+":\n"+" Nice day we are having, huh?",
                    self.name.title()+":\n"+" Its time for my break.",
                    self.name.title()+":\n"+" I cant wait for the promotion, I have been working pretty hard \n these past two weeks.",
                    self.name.title()+":\n"+" She had made a poor job of hiding the damage.",
                    self.name.title()+":\n"+" The foodbank was sold out when I got there.",
                    self.name.title()+":\n"+" There'll be plenty more before this is over.",
                    self.name.title()+":\n"+" Have you read the newspaper stories about my wife."
                    )
        
        self.response.append(string_5)