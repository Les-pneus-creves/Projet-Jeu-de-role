import Evenement
import pygame
import pygame_menu
from persotest import persotest
from Recompense import Recompense
from Combat import Combat


class ModeEvenement:
    def __init__(self, typeCase: str):
        self._evenement = Recompense(typeCase.split("_")[0])
        # self._surface = pygame.display.set_mode((1600,1400))

    def getEvenement(self):
        return self._evenement

    # lecture des evenements
    def on_event(self, events) -> None:
        if self._evenement.getEnCours():
            if self._evenement.getMenu().is_enabled():
                self._evenement.getMenu().update(events)

    # Calcul des mises à jours
    def on_loop(self) -> None:
        pass

    # Calcul des affichages
    def on_render(self, window) -> None:

        if self._evenement.getEnCours():
            if self._evenement.getMenu().is_enabled():
                self._evenement.getMenu().draw(window)

    def getEnCours(self):
        return self._evenement.getEnCours()


if __name__ == "__main__":

    pygame.init()

    window = pygame.display.set_mode((1000, 1000), pygame.HWSURFACE | pygame.DOUBLEBUF)

    evenement = Recompense("Herbe")
    x = ModeEvenement(evenement)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if evenement.getEnCours():

            if x.getEvenement().getMenu().is_enabled():
                x.getEvenement().getMenu().update(events)
                x.getEvenement().getMenu().draw(window)

        # else:
        # pygame.draw.rect(window, (255,0,0),(0,0,1000,1000))
        pygame.display.flip()
