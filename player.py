"""  
 * Player Class
 ---------------------------------------------------------------------------------------------------------
 * This class is part of -----, text based adventure game.  
 * This class creates attributes of the player, such as inventory and a limit on the inventory capacity
 * 
""" 
class Player():
     
    def __init__(self):
        """ the player constructor has the attributes inventory to store items, total to hold the summed weights
        and capacity to set a limit to the total weight possible to be carried.
        """
        self.inventory = []
        self.total = 0.0
        self.capacity = 0.0
        self.tolerance = 0.0

        
    def set_capacity(self, capacity):
        """
        this method sets the players capacity
        
        Paramaters
        ----------
        capacity: float
            floating point number
        """
        
        self.capacity = capacity
        
        
    def set_total(self,item):
        """
        this method sums the weight of items each time an item is added to the player
        
        Paramaters
        ----------
        item: float
            the items weight
        """
        
        self.total = float("{:.2f}".format(self.total + item))
    
    
    def set_tolerance(self,tolerance):
        
        self.tolerance = tolerance
        
    def get_tolerance(self):
        
        return self.tolerance
       
    def get_capacity(self):
        """ Returns the players inventory capacity"""
        
        return self.capacity
    
    
    def get_total(self):
        """ Returns the players summed inventory weight"""
        
        return self.total
      
      
    def has_space(self, weight):
        """
        Checks if an item is too heavy to be added to the inventory
        
        Parameter
        ---------
        weight: float
            floating point number(items weight)
        Returns: boolean
        """
        
        total = 0
        total = self.total + weight
        
        if total > self.capacity:
            return False
        else:
            return True
    
    
    def add_item(self,item):
        """Adds items to the inventory and adds the item's weight to the weight"""
    
        self.set_total(item.weight)
        self.inventory.append(item)
       
       
    def pop_item(self,name):
        """This method removes an item from the players inventory
            
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
            
            
    def print_inventory(self):
        """print_inventory prints the items present in the players inventory, otherswise an error message is printed"""
        count = 0
        mid = ""
        upper = ("-----------Inventory-------------\n")
        lower = ("\n---------------------------------\n"+ "Capacity : "+str(self.total) + " / " + str(self.get_capacity()))
        
        for item in self.inventory:
            if len(self.inventory) > 0:
                mid += item.get_name() + " "
            
            elif self.inventory[count] == self.inventory[-1]:
                mid += item.get_name()
            
            count += 1
        print(upper + mid + lower)