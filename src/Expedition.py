import EquipeDePersonnages
import Evenement
from PlateauDeJeu import PlateauDeJeu

class Expedition:

    def __init__(self, equipe, plateau):
        self.__temps: int = 1             #Numéro du tour de l'expédition en cour
        self.__equipe: EquipeDePersonnages = equipe          #Equipe de personnage joueur du joueur
        self.__eventEnCours: Evenement = None      #Even ement actuellement en cours
        self.__plateau: PlateauDeJeu = plateau     #Plateau sur lequel l'éxpedition se déroule

    # lecture des evenements
    def on_event(self, event) -> None:
        pass
    
    #Calcul des mises à jours
    def on_loop(self) -> None:
        pass
    
    #Calcul des affichages
    def on_render(self, window) -> None:
        self.__plateau.render(window)

    #Méthode permettant de sélectionner aléatoirement (ou non?) un plateau
    def selectPlateau(self)  -> None:
        pass


    #Méthode lançant un événement précis
    def lancerEvenement(self,evenement) -> None:
        pass


    #Méthode retournant true ou false selon si des coordonnées (En pixel ou en case/hexagone??) sont effectivement dans la map
    def estDansLaMap(self,coord) -> bool:
        pass

    