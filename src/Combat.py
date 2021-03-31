from abc import ABC, abstractmethod #module pour classe abstraite
from Evenement import Evenement # Heritage
import EquipeDePersonnages
#import Personnage
import pygame_menu
import json
import pygame
import random


class Combat(Evenement):

    def __init__(self, equipe: EquipeDePersonnages):
        super().__init__()
        self.__log: str = ""
        self.__equipeMechant: EquipeDePersonnages = None   #J'ai mis none en attendant
        self._equipe = equipe 

        with open("src/dossierJson/combats.json") as fichier:
            data = json.loads(fichier.read())
            event_a_lancer = random.choice(list(data))
            eventJson = data[event_a_lancer]
            self.creerMenu(eventJson["titre"],eventJson["texte"], eventJson["image"])


    #----------

    #Méthode permettant de donner au combat l'équipe de personnage Joueur qui va se battre
    def lancement(self,equipePerso: EquipeDePersonnages) -> None :
        print("un combat se lance bruh bruh bruh bruh")


        #Methode appelée dans l'init qui modifie le menu avec ce qu'il faut
    def creerMenu(self, titre: str, texte : str, image) -> None:
        self._menu = pygame_menu.Menu(800,800, titre, columns= 2, rows = 2, column_max_width=(200,200))
        self._menu.add_label(texte)
        self._menu.add_image(image, scale = (0.5,0.5))
        self._menu.add_label("Ici c'est des logs de combat") # \n ouais un vrai combat de bonhomme \n y'a du sang partout \n call an ambulance, but not for me")
        self._menu.add_button("ok", self.mettreFin)

    #Methode permettant de passer en cours a false
    def mettreFin(self):
        self._enCours = False
        self._menu._close()
    
    
    #Méthode permettant de déterminer l'ordre des tours des personnages lors du combat
    def __creerOrdreTour(self,ep1: EquipeDePersonnages, ep2: EquipeDePersonnages) -> list:
        pass
    
    #Méthode permmetant de selectionné une cible dans une équipe donnée
 #   def __choisirCible(self,equipePerso: EquipeDePersonnages) -> Personnage:
 #       pass
    