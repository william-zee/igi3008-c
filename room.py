from characters import Characters

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {} 
        self.objet= {} 
        self.characters= {}

    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
         return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n  {self.personnages()}"
    
    def add(self,item):  
        self.objet[item.name]= item 
        if True:
            self.objet[item.name]= item 
  
    def get_object_lieu(self): 
        
        
        if not self.objet :
            return "Votre salle est vide."

        object = "il y a  les items suivants  :\n"  
      
        
        for item in self.objet.values(): 

     
            object += f"  - {item} \n"
        return object 
    

    def personnages(self): 
       
        if not self.characters :
            return "il n'y a pas de pnj"

        pnj = "il y a le personnage :\n"  
       
        
        for character in self.characters.values(): 

     
            pnj += f"  - {character} \n"
        return pnj
        from item import Item