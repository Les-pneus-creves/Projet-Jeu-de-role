import Evenement
import pygame_menu

class ModeEvenement:
    def __init__(self, evenement: Evenement):
        self.__evenement = None    #Evenement actuellement en cours (peut etre nul)
        self.__menu = None

    # lecture des evenements
    def on_event(self, event) -> None:
        pass
    
    #Calcul des mises à jours
    def on_loop(self) -> None:
        pass
    
    #Calcul des affichages
    def on_render(self, window) -> None:
        pass

