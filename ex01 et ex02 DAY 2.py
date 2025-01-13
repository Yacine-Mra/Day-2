class voiture:

    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher_details(self):
        print(f"Marque: {self.marque}")
        print(f"Modele: {self.modele}")
        print(f"Annee: {self.annee}")
        print(f"Kilometrage: {self.kilometrage}")

    def augmenter_kilometrage(self):
        self.kilometrage += 10
        

    def calculer_age(self):
        return 2025 - self.annee
    
    def est_vieille(self):
        if self.calculer_age() > 10:
            print("True") 
        else:
            print("False")
        
bugatti=voiture("Bugatti","Type 35",1924,300000) 
audi=voiture("Audi ", "A4", 2015, 20)
bugatti.augmenter_kilometrage()
audi.augmenter_kilometrage() 
print("Voici les détails de l'audi : ")
audi.afficher_details()
print("Voici les détails de la bugatti : ")
bugatti.afficher_details()
print("Voici l'age de l'audi : ")
print(audi.calculer_age())
print(audi.est_vieille())
print("Voici l'age de la bugatti : ")
print(bugatti.calculer_age())
print(bugatti.est_vieille())




    
    
