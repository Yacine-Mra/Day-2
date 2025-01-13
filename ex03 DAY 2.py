class animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def parler (self):
        return ("je suis un animal")

class chat(animal):
    def parler(self):
        return ("Miaou")
        
class chien(animal):
    def parler(self):
        return ("Wouf")
        
class zoo:
    def __init__(self,):
        self.animal = [] 
        
    def ajouter_animal(self,animal):
        self.animal.append(animal)

    def faire_parler_tout_le_monde(self):
        for animal in self.animal:
            print(f" Le {animal.espece} : {animal.parler()}")

le_zoo = zoo()

chat1 = chat("Chat", "chat")
chien1 = chien("CHien", "chien")

le_zoo.ajouter_animal(chat1)
le_zoo.ajouter_animal(chien1)

le_zoo.faire_parler_tout_le_monde()
        






    