from abc import ABC, abstractmethod
from Evenement import Evenement #Heritage
import EquipeDePersonnages
#import Personnage
import pygame_menu
import json
import random

class Recompense(Evenement):

    def __init__(self, event_a_lancer : str):
        super().__init__()      
        with open("src/dossierJson/recompenses.json") as fichier:
            data = json.loads(fichier.read())
            eventJson = data[event_a_lancer]
            self.creerMenu(eventJson["titre"],eventJson["texte"], eventJson["image"])
        




    #----------
        
    def lancement(self, equipePerso: EquipeDePersonnages):
        print("Lancement d'une récompense very nice")

    #Methode appelée dans l'init qui modifie le menu avec ce qu'il faut
    def creerMenu(self, titre: str, texte : str, image) -> None:
        self._menu = pygame_menu.Menu(titre, 1000,1000)
        self._menu.add.label(texte)
        self._menu.add_image(image)
        self._menu.add_button("ok", self.mettreFin)

    #Methode permettant de passer en cours a false
    def mettreFin(self):
        self._enCours = False
        self._menu._close()
    


        
        

    