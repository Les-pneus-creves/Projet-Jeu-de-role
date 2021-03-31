import Evenement
import pygame
import pygame_menu
from Recompense import Recompense
from Combat import Combat

class ModeEvenement:
    def __init__(self, evenement: Evenement):
        self._evenement = evenement    #Evenement actuellement en cours (peut etre nul)
       # self.__surface = pygame.display.set_mode((1600,1400))

    def getEvenement(self):
        return self._evenement

    # lecture des evenements
    def on_event(self, event) -> None:
        pass
    
    #Calcul des mises à jours
    def on_loop(self) -> None:
        pass
    
    #Calcul des affichages
    def on_render(self, window) -> None:
        pass


if __name__ == "__main__" :

    pygame.init()

    window = pygame.display.set_mode((1000,1000), pygame.HWSURFACE | pygame.DOUBLEBUF)
    
    evenement = Combat(15)
    x = ModeEvenement(evenement)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if evenement.getEnCours() == True: 

            if x.getEvenement().getMenu().is_enabled():
                x.getEvenement().getMenu().update(events)
                x.getEvenement().getMenu().draw(window)

        
        #else:
           # pygame.draw.rect(window, (255,0,0),(0,0,1000,1000))
        pygame.display.flip()


