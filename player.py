class Player():

    # Define the constructor.
    def __init__(self, name,starting_room=None):
        self.name = name
        self.current_room = None 
        self.history = []  
        self.inventory = {} 
    
        if starting_room is not None:
            self.history.append(starting_room)
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room. 
        if self.current_room is None:
            print("Vous n'êtes dans aucune pièce pour commencer.")
            return False
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        self.history.append(self.current_room)
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description()) 
        return True  
          
    def get_inventory(self): 
        # sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)  
        # self.inventory["sword"] = sword
        
         
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_description = "Vous disposez des items suivants :\n"  
       
        
        for name,item in self.inventory.items(): 

     
            inventory_description += f"  - {name} : {item}\n"
        return inventory_description 
    
    def get_history(self): 
        if not self.history:

            return "Aucune pièce visitée pour le moment."
        history_s="vous avez visité"
        for room in self.history: 
            history_s+= f"{room.description}"
            
        return history_s 
    




    