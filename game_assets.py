class Assets():
    def __init__(self):
        self.intro_screen()
        self.options()
        self.case = 0

    def intro_screen(self):
        print("\n"*1000)
        print(" ████████╗██╗  ██╗███████╗    ██████╗ ███████╗██╗     ██╗██╗   ██╗███████╗██████╗ ██╗   ██╗")
        print(" ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔════╝██║     ██║██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝")
        print("    ██║   ███████║█████╗      ██║  ██║█████╗  ██║     ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝ ")
        print("    ██║   ██╔══██║██╔══╝      ██║  ██║██╔══╝  ██║     ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝  ")
        print("    ██║   ██║  ██║███████╗    ██████╔╝███████╗███████╗██║ ╚████╔╝ ███████╗██║  ██║   ██║   ")
        print("    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ")
        print("\n")
    
    def print_plot(self):
        print("You are on your 57th delivery of the day, you approach")
        print("a modern looking building. You drive up to a parking spot")
        print("and park your delivery van and proceed to walk to the front")
        print("door. It should be the same as always, walk in, drop off and")
        print("leave for the next delivery.")
    
    def options(self):
        print("                                   [1]     [ Start ]  ")
        print("                                   [2] [ How To Play ]  ")
        print("                                   [3]     [ Quit ]  \n\n")
        
    def help_(self,index):
        
        while True:
            if index == 1:
                print("\n"*100)
                print("In 'The Delivery' you are a courier attempting to deliever a package.")
                print("to win the game you will have to deliver the package, you can do this\n")
                print("by first talking to the receptionist and following their instructions, or")
                print("you can explore and interact with the people and items spread out at ridgeworks.")
                print("\n[ Exit - Menu ] [ Next - Controls ] \n")
                choice = input("> ")
                if choice.title() == "Exit":
                    break
                elif choice.title() == "Next":
                    index = 2
                else:
                    print("[ Invalid Entry ]")
                    
            elif index == 2:
                print("\n"*100)
                print("How to Play [Controls]\n")
                print("The Delivery is a textbased game that uses specific command words to\nmove and interact.\n")
                print("Command Words")
                print(" go, back, interact, give, pick, drop, show, open, use, unlock ")
                if self.case == 0:
                    print("\n[ Back - Introduction ] [ Next - Using 'go' ]")
                    choice = input("> ")
                    if choice.title() == "Back":
                        index = 1
                    elif choice.title() == "Next":
                        index = 3
                    else:
                        print("[ Invalid Entry ]")
                        
                elif self.case == 1:
                    print("\n[Exit - Game][ Next - Using 'go' ]")
                    choice = input("> ")
                    
                    if choice.title() == "Next":
                        index = 3
                    elif choice.title() == "Exit":
                        break
                    else:
                        print("[ Invalid Entry ]")
                    
            elif index == 3:
                print("\n"*100)
                print("Using the 'go' command\n")
                print("Description:\n\nThe 'go' command allows the player to use exits in the game.\n")
                print("Usage:\ngo north\ngo east")
                print("\n[ Back - How to play ] [ Next - Using 'back' ]")
                index = self.select(3)
                
                        
            elif index == 4:
                print("\n"*100)
                print("Using the 'back' command\n")
                print("Description:\n\nThe 'back' command allows the player to retrace their movements \nthrough the rooms.")
                print("Usage:\n\nback ")
                print("\n[ Back - Using 'go' ] [ Next - Using 'interact' ]")
                index = self.select(4)        
                        
            elif index == 5:
                print("\n"*100)
                print("Using the 'interact' command \n")
                print("Description:\n\nThe 'interact' command allows the player to interact with characters\n"
                      "The command is followed by 'with' and finally the character name.\n")
                print("Usage:\n interact with david \n interact with jane")            
                print("\n[ Back - using 'back' ] [ Next - Using 'give' ]")
                index = self.select(5)
                        
            elif index == 6:
                print("\n"*100)
                print("Using the 'give' command \n")
                print("Description:\n\nThe 'give' command allows the player to give items to characters"
                      "The command is followed by 'character' and finally the item name.\n")
                print("Usage:\n give david cup \n give jane pencil")            
                print("\n[ Back - using 'interact' ] [ Next - Using 'pick' ]")
                index = self.select(6) 
                 
            elif index == 7:
                print("\n"*100)
                print("Using the 'pick' command \n")
                print("Description:\n\nThe 'pick' command allows the player to pick up items\n"
                      "\nThe command is followed by 'up' and finally the item name.\n")
                print("Usage:\n pick up key \n pick up spoon")            
                print("\n[ Back - using 'give' ] [ Next - Using 'drop' ]")
                index = self.select(7)
                        
            elif index == 8:
                print("\n"*100)
                print("Using the 'drop' command \n")
                print("Description:\n\nThe 'drop' command allows the player to drop items"+
                      "The command\ncan be used in the inventory or in game."
                      "\n\tThe commandis followed by the item name.\n")
                print("Usage:\n drop key ")            
                print("\n[ Back - using 'drop' ] [ Next - Using 'show' ]")
                index = self.select(8)
                        
            elif index == 9:
                print("\n"*100)
                print("Using the 'show' command \n")
                print("Description:\n\nThe 'show' command allows the player to item details in the inventory\n"
                      "The command is followed by the item name.\n")
                print("Usage:\n show key")            
                print("\n[ Back - using 'drop' ] [ Next - Using 'open' ]")
                index = self.select(9)  
                        
            elif index == 10:
                print("\n"*100)
                print("Using the 'open' command \n")
                print("Description:\n\nThe 'open' command allows the player to open the \ninventory or the portable teleporter if in inventory"
                      "The command is \nfollowed by either invetory or teleporter.\n")
                print("Usage:\n open inventory \n open teleporter")            
                print("\n[ Back - using 'show' ] [ Next - Using 'use' ]")
                index = self.select(10)   
                 
                        
            elif index == 11:
                print("\n"*100)
                print("Using the 'use' command \n")
                print("Description:\nThe 'use' command allows the player to use certain items in their inventory\n"
                      "The command is followed by the item name.\n")
                print("Usage:\n use candybar")            
                print("\n[ Back - using 'open' ][ Next - Using 'unlock' ]")
                index = self.select(11)
                
                    
            elif index == 12:
                print("\n"*100)
                print("Using the 'unlock' command \n")
                print("Description:\nThe 'unlock' command allows the player to unlock restricated exits\n"
                      "The command is followed by the direction and the exit.\n")
                print("Usage:\n unlock east exit")
                print("\nNote: The player will be prompted to swipe an item, in order to do this")
                print("      enter;\n\tswipe item ")
                if self.case == 0:
                    print("\n[ Back - using 'use' ] [ Exit - Menu ]")
                    choice = input("> ")
                    if choice.title() == "Exit":
                        break
                    if choice.title() == "Back":
                        index = 11
                    
                elif self.case == 1:
                    print("\n[ Back - using 'use' ][ Exit - Game ]")
                    if choice.title() == "Exit":
                        break
                    
                    if choice.title() == "Back":
                        index = 11
             
    def select(self, index):
        number = 0
        choice = ""
        while True:
            choice = input("> ")
            if choice.title() == "Back":
                number = index - 1
                break
            elif choice.title() == "Next":
                number = index + 1
                break
            else:
                print("\n[ Invalid entry ]\n")
        return number
                
                    

   