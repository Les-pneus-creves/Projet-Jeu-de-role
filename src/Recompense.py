from abc import ABC, abstractmethod
from Evenement import Evenement #Heritage
import EquipeDePersonnages
#import Personnage
import pygame_menu
import json
import random

class Recompense(Evenement):

    def __init__(self, equipe: EquipeDePersonnages):
        super().__init__()
        self.equipe = equipe        
        with open("src/dossierJson/recompenses.json") as fichier:
            data = json.loads(fichier.read())
            x = random.choice(list(data))
            y = data[x]
            self.creerMenu(y["titre"],y["texte"], y["image"])

    #propriétés héritées
    @property
    def texteDescr(self):
        return self.texteDescr

    @texteDescr.setter
    def setTexteDescr(self, value):
        self.texteDescr = value

    
    def getMenu(self):
        return self.__menu

    
    def setMenu(self, value):
        self.__menu = value
    
    #----------
        
    def lancement(self, equipePerso: EquipeDePersonnages):
        print("Lancement d'une récompense very nice")

    def creerMenu(self, titre: str, texte : str, image) -> None:
        self.__menu = pygame_menu.Menu(800,800, titre)
        self.__menu.add_label(texte)
        self.__menu.add_image(image)
        
        

    