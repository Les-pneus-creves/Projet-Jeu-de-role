from abc import ABC, abstractmethod
from Evenement import Evenement #Heritage
import EquipeDePersonnages
#import Personnage
import pygame_menu

class Recompense(Evenement):

    def __init__(self, equipe: EquipeDePersonnages):
        super().__init__()
        self.equipe = equipe
        self.log: str = ""

    #propriétés héritées
    @property
    def texteDescr(self):
        return self.texteDescr

    @texteDescr.setter
    def setTexteDescr(self, value):
        self.texteDescr = value

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value
    
    #----------
        
    def lancement(self, equipePerso: EquipeDePersonnages):
        print("Lancement d'une récompense very nice")

    def creerMenu(self, titre: str, texte : str, image):
        self.__menu = pygame_menu.Menu(300,400, titre)
        self.__menu.add_label(texte)
        self.__menu.add.image(image)
        return self.__menu
        

    