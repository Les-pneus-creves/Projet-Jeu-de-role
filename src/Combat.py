from abc import ABC, abstractmethod #module pour classe abstraite
from Evenement import Evenement # Heritage
import EquipeDePersonnages
import Personnage

class Combat(Evenement):

    def __init__(self, equipe: EquipeDePersonnages):
        super().__init__()
        self.__log: str = ""
        self.__equipeMechant: EquipeDePersonnages = None   #J'ai mis none en attendant


    #Méthode permettant de donner au combat l'équipe de personnage Joueur qui va se battre
    def lancement(self,equipePerso: EquipeDePersonnages) -> None :
        pass
    
    #Méthode permettant de déterminer l'ordre des tours des personnages lors du combat
    def __creerOrdreTour(self,ep1: EquipeDePersonnages, ep2: EquipeDePersonnages) -> list:
        pass
    
    #Méthode permmetant de selectionné une cible dans une équipe donnée
    def __choisirCible(self,equipePerso: EquipeDePersonnages) -> Personnage:
        pass
    