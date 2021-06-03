import Evenement
import pygame
import pygame_menu
import Objet  # pour faire test
from EquipeDePersonnages import EquipeDePersonnages
from Personnage import Personnage  # pour faire test
from Recompense import Recompense
from Combat import Combat


class ModeEvenement:
    def __init__(self, evenement: Evenement):
        self._evenement = evenement
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

    def getVictoire(self):
        return self._evenement.getVictoire()


if __name__ == "__main__":

    pygame.init()

    window = pygame.display.set_mode((1000, 1000), pygame.HWSURFACE | pygame.DOUBLEBUF)

    jean = Personnage("Jean", 15, 7, 8, 15, None)
    bob = Personnage("Bob", 10, 8, 6, 12, None)
    jeanCastex = Personnage("JeanCastex", 12, 9, 4, 4, None)
    pz = Objet.Arme("Arme_Panzerschreck", "src/images/Objets/Panzerschreck.png", 25, 2)
    bob.addToInventaire(pz)

    equipe = EquipeDePersonnages(jean, bob, jeanCastex)

    c = Combat(equipe)

    evenement = c

    c.lancement()
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
