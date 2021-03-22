from abc import ABC, abstractmethod
from Evenement import Evenement #Heritage
import EquipeDePersonnages
import Personnage

class Recompense(Evenement):

    def __init__(self, equipe: EquipeDePersonnages):
        super().__init__()
        self.equipe = equipe
        self.__log: str = ""
        
    def lancement(self, equipePerso: EquipeDePersonnages):
        print("Lancement d'une récompense very nice")

    