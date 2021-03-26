# from Personnage import Personnage

class EquipeDePersonnages:
    def __init__(self,personnages):
        self.__coord = (0,0)
        self.__estVivant = True
        self.__personnages = personnages

    def __len__(self):
        return len(self.__personnages)

    def deplacement(self, coord):
        self.__coord = coord
    
    def render(self):
        pass
        