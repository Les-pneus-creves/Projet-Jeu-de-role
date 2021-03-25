import Evenement
import pygame
import pygame_menu
from Recompense import Recompense

class ModeEvenement:
    def __init__(self, evenement: Evenement):
        self.evenement = evenement    #Evenement actuellement en cours (peut etre nul)
        self.__surface = pygame.display.set_mode((600,400))

    # lecture des evenements
    def on_event(self, event) -> None:
        pass
    
    #Calcul des mises à jours
    def on_loop(self) -> None:
        pass
    
    #Calcul des affichages
    def on_render(self, window) -> None:
        self.evenement.menu.mainloop(window)


if __name__ == "__main__" :

    pygame.init()

    window = pygame.display.set_mode((720,720), pygame.HWSURFACE | pygame.DOUBLEBUF)

    ter = Recompense(15)
    x = ModeEvenement(ter)
    x.menu = ter.creerMenu("Attaque de bandit!","Des bandits vous attaquent", "images/20124.jpg")
    while True:
        x.on_render(window)
        pygame.display.flip()


