class personnage:
    def __init__(self,nom,points_de_vie,force):
        self.nom=nom
        self.points_de_vie=points_de_vie
        self.force = force

    def attaquer (self, autre_personnage):
        autre_personnage.force -= self.force

class guerrier(personnage):
    def guerrrier (self):
        self.force += 10

class mage(personnage):
    def attaque_magique(self):
        self.force += 5

    def attaque_normal(self):
        self.force -= 0

class combat:
    def __init__(self, guerrier, mage):
        self.guerrier = guerrier
        self.mage = mage

    def lancer_combat(self):
        while self.guerrier.points_de_vie > 0 and self.mage.points_de_vie > 0:
            self.guerrier.attaquer(self.mage)
            self.mage.attaquer(self.guerrier)

mage = mage("Api", 100, 10)
guerrier = guerrier("Lancelot", 100, 10)

print ("Voici le combat")
print (mage.nom + " a " + str(mage.points_de_vie) + " points de vie pour une force de " + str(mage.force))
print (guerrier.nom + " a " + str(guerrier.points_de_vie) + " points de vie pour une force de " + str(guerrier.force))

    