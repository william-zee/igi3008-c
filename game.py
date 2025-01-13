from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item 
from characters import Characters  

class Game:
      # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None 
        self.inventory={} 
        self.characters={}
        
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go 
        back=Command("back","retourne en arrière",Actions.back, 0)
        self.commands["back"] = back  
        look=Command("look","regarde il y a :",Actions.look, 0)
        self.commands["look"] = look 
        take=Command("take","prend l'object :",Actions.take, 1)
        self.commands["take"] = take 
        drop=Command("drop","dépose l'object :",Actions.drop, 1)
        self.commands["drop"] = drop 
        check=Command("check","tu as dans ton inventaire :",Actions.check, 0)
        self.commands["check"] = check 
        talk=Command("Talk","tu peux discuter avec le personnage :",Actions.talk, 1)
        self.commands["talk"] = talk
        get_history=Command("get_history","/ntu peux voir ton historique :",Actions.get_history, 0)
        self.commands["get_history"] = get_history
   
        
        # Setup rooms

        forest = Room("Forest", " une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", " une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", " une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", " un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", " un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = Room("Castle", " un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)  
        mountain = Room("Mountain", " une énorme montagne  avec des douves et des rochers énormes. Au sommet, l'Everest.")
        self.rooms.append(mountain)  
        temple = Room("temple", " un énorme temple  avec des douves et des statues. Au sommet, une girouette.")
        self.rooms.append(temple)  

    #SETUP OBJECTS

        pistolet=Item("pistolet","la meilleur arme",3) 
        swamp.add(pistolet) 
        hache=Item("hache","la meilleur arme tranchante",3) 
        tower.add(hache) 

    #SETUP Personnage 
        gandalf = Characters("Gandalf", "Un magicien blanc", "Forest", ["Abracadabra !", "Je suis Gandalf, le magicien!", "Le danger est proche..."])
        swamp.characters[gandalf.name] = gandalf 
        mario =Characters("Mario", "un plombier qui sauve des princesses",tower.name,["Ahhhhhhh!"])
        tower.characters[mario.name] = mario 
     

    # Create exits for rooms

        forest.exits = {"N" : cave, "E" : None, "S" : castle, "O" : None,"U" : None,"D" :None}
        tower.exits = {"N" : cottage, "E" : mountain, "S" : None, "O" : None,"U" : None,"D" :None}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None,"U" : None,"D" :None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave,"U" : None,"D" :None}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle,"U" : None,"D" :None}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None,"U" : None,"D" :None} 
        mountain.exits = {"N" : None, "E" : None, "S" : None, "O" : tower, "U" : temple, "D" : None }
        temple.exits = {"N" : None, "E" : None, "S" : mountain, "O" : None,"U" : None,"D" : mountain }

    # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome() 
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

  

    # Process the command entered by the player
    def process_command(self, command_string) -> None: 
        if not command_string:
            return None

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
            if command_word == "go": 
                print(self.player.get_inventory())  

                if len(self.player.current_room.characters) == 0:
                    print("\n Il n'y aucun PNJ dans la pièce")
                else:
                    print("\n Il y a les PNJ suivants dans la pièce:")
                    copie = list(self.player.current_room.characters.values())
                    for characters in copie:
                        print(f" - {characters} \n")
                        print (characters.move())
      

    # Print the welcome mesage
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
