import random 

class Characters:
    def __init__(self, name, description,current_room,msg):
      
        self.name = name
        self.description = description
        self.current_room = current_room 
        self.msg = msg 
        self.msg_history = []

    def __str__(self):
       
       
        
        return f"{self.name} : {self.description} ({self.msg})" 
    
    
    def move (self):
        l = ["Reste", "Deplace"]
        resultat = random. choice (l)
        print (resultat)
        if resultat == "Deplace" :
            adjacent_rooms = []
            for room in self.current_room.exits.values():
                if room is not None:
                    adjacent_rooms.append(room)
            next_room = random. choice(adjacent_rooms)
            del self.current_room.characters[self.name]
            self.current_room = next_room
            self.current_room.characters[self.name]= self
            print(f" {self.name} s'est déplacé dans {self.current_room.name}")
            return True

        else: 
            print(f" {self. name} ne se déplace pas") 
            return False
    
    
    def get_msg(self):
        if len(self.msg) > 0:
            # Récupérer et afficher le premier message
            msg = self.msg.pop(0)  # pop(0) retire et retourne le premier message
            self.msg_history.append(msg)  # Ajouter à l'historique des messages affichés
            print(f"{self.name} dit : {msg}")
        else:
            # Si tous les messages ont été affichés, recommencer
            print(f"{self.name} n'a plus rien à dire, les messages vont recommencer.")
            self.msg = self.msg_history.copy()  # Recommencer à partir de l'historique des messages
            self.msg_history = []  # Réinitialiser l'historique
            self.get_msg()  # Relancer la méthode pour afficher le premier message à nouveau 
        if True:
            print(f"Messages de {self.name} à afficher.")
        if self.messages:
            return self.messages.pop(0)  # Afficher le premier message et le retirer
        else:
            return f"{self.name} n'a plus rien à dire."    
