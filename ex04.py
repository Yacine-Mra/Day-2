class produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
    
    def afficher_produit(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}, Quantité: {self.quantite}")

class magasin:
    def __init__(self):
        self.inventaire = [] 

    def ajouter_produit(self, produit):  
        self.inventaire.append(produit) 
        print(f"Produit '{produit.nom}' ajouté avec succès.")

    def rechercher_produit(self, nom):
        for produit in self.inventaire:
            if produit.nom == nom:
                produit.afficher_produit()
                return
        print(f"Produit '{nom}' non trouvé.")
        
    def afficher_inventaire(self):
        print("Inventaire du magasin :")
        for produit in self.inventaire:
            produit.afficher_produit()
    
    def vendre_produit(self, nom):
        for produit in self.inventaire:
            if produit.nom == nom:
                if produit.quantite > 0:
                    produit.quantite -= 1
                    print(f"Vente du produit '{produit.nom}'. Quantité restante : {produit.quantite}")
                    if produit.quantite == 0:
                        print(f"Le produit '{produit.nom}' est épuisé.")
                else:
                    print(f"Le produit '{produit.nom}' est déjà épuisé.")
                return
            print(f"Produit '{nom}' non trouvé.")


pain = produit("Pain", 1.5, 10)
poire = produit("Poire", 2.0, 15)
peche = produit("Peche", 3.0, 20)

le_magasin = magasin()

le_magasin.ajouter_produit(pain)
le_magasin.ajouter_produit(poire)
le_magasin.ajouter_produit(peche)

le_magasin.rechercher_produit()

le_magasin.vendre_produit()

le_magasin.afficher_inventaire()







       