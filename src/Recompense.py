from abc import ABC, abstractmethod
from Evenement import Evenement  # Heritage
import pygame
import pygame_menu
import json
import random
import Objet
from Inventaire import Inventaire

class Recompense(Evenement):

    def __init__(self, event_a_lancer: str):
        super().__init__()
        with open("src/dossierJson/recompenses.json") as fichier:
            data = json.loads(fichier.read())
            self.eventJson = data[event_a_lancer]

        self.nom = event_a_lancer

    def lancement(self):
        print("Lancement d'une récompense very nice")
        self.creerMenu(self.eventJson["titre"], self.eventJson["texte"], self.eventJson["image"])

    # Methode appelée dans l'init qui modifie le menu avec ce qu'il faut
    def creerMenu(self, titre: str, texte: str, image) -> None:
        taille = list(pygame.display.get_window_size())
        taille[0] /= 1.25
        taille[1] /= 1.25
        self._menu = pygame_menu.Menu(titre, taille[0], taille[1])
        self._menu.add.label(texte)
        self._menu.add.image(image)
        self._menu.add.button("ok", self.mettreFin)

    # Methode permettant de passer en cours a false
    def mettreFin(self):
        self._enCours = False
        self._menu._close()

    def getLoot(self):
        """Methode qui retourne un `src.Inventaire `de deux objets en fonction du loot possible au combat.

        Return
        ------
        inv: `src.Invetaire`
            inventaire lootable par le joueur.

        """

        listeObjet = self.eventJson["loot"]

        inv = Inventaire(0,0,4)

        if len(listeObjet) > 0:
            objet = random.choice(listeObjet)
            if objet == "Patate":
                inv.ajouter(Objet.objets[objet], random.randint(1,7))
            else:
                inv.ajouter(Objet.objets[objet])
        return inv
