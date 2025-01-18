# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1].upper() 
        if direction == 'NORD':
            direction='N'
        elif direction =='SUD':
            direction='S'
        elif direction=='EST':
            direction='E'
        elif direction=='OUEST':
            direction='O'
        valideok  = {'N','S','E','O','U','D','SUD','OUEST','EST','NORD'} 
        if direction not in valideok: 
            print("impossible , faites une nouvelle commande") 
        else: 
        # Move the player in the direction specified by the parameter.
            player.move(direction)
            return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True 
    def back(game, list_of_words, number_of_parameters): 
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        y=game.player.history 
        
        # Revenir à la pièce précédente
        if len(y) == 0:
            print("Impossible de revenir en arrière, aucun historique.")
            return False

        # Revenir à la pièce précédente dans l'historique
        a=y.pop()
        print("Vous êtes de retour dans ",a.description)
        return True 
    

    def look(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False 
        y= game.player.current_room.get_object_lieu() 
        x= game.player.current_room.personnages() 
        print(x,y)
    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False  
        if  True:
            print(f"Tentative de prise de l'objet {list_of_words[1]}")
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        game.player.inventory[list_of_words[1]]=game.player.current_room.objet[list_of_words[1]] 
        print(game.player.inventory)
        del game.player.current_room.objet[list_of_words[1]]  
        if True:
                print(f"{list_of_words[1]} a été ajouté à l'inventaire.")
                print(f"Vous avez pris {list_of_words[1]}.")
                print(f"{list_of_words[1]} n'est pas dans cette salle.")
                return

        
      

    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False 
        game.player.current_room.objet[list_of_words[1]]= game.player.inventory[list_of_words[1]]
        print(game.player.inventory)
        del game.player.inventory[list_of_words[1]]



    def check(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False  
    
    def talk(game, list_of_words, number_of_parameters): 
        if True:
            print(f"Le joueur parle à {character.name}")
        print(character.get_msg())
        l = len(list_of_words)
        # Vérifier que la commande a bien un seul paramètre (le nom du PNJ)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"\nLa commande '{command_word}' prend 1 paramètre.\n")
            return False

        # Récupérer le nom du personnage à qui parler
        character_name = list_of_words[1]
        
        # Chercher le personnage dans la pièce actuelle du joueur
        player_room = game.player.current_room
        if character_name in player_room.characters:
            character = player_room.characters[character_name]
            character.get_msg()  # Appeler la méthode get_msg() du personnage
            return True
        else:
            print(f"\nIl n'y a pas de personnage nommé '{character_name}' ici.\n")
            return False
        
    def get_inventory(game,list_of_words, number_of_parameters): 
        # sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)  
        # self.inventory["sword"] = sword  
        inventory=game.player.inventory
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        if not inventory:
            return "Votre inventaire est vide."
        inventory_description = "Vous disposez des items suivants :\n"
        for name,item in inventory.items(): 
            inventory_description += f"  - {name} : {item}\n"
        print(inventory_description) 
 
    def get_history(game,list_of_words, number_of_parameters): 
        room = game.rooms
        history=game.player.history
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        if not history:

            print("Aucune pièce visitée pour le moment.")
        history_s="vous avez visité"
        for room in history: 
            history_s+= f"{room.description}"   
        print(history_s)