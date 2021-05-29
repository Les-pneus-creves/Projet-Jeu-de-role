"""
Voici la commande pour générer la doc :
`pdoc --html --output-dir doc src/*.py --force`
"""

import pygame
from enum import Enum
from EquipeDePersonnages import EquipeDePersonnages
from Personnage import Personnage
from Expedition import Expedition
from PlateauDeJeu import PlateauDeJeu
from ModeEvenement import ModeEvenement
from Recompense import Recompense

Etats = Enum('Etats', 'Gestion Expedition Evenement')


class Jeu:
    def __init__(self):
        self._nbTour: int = 0
        self._running: bool = True
        self._width: int = 1080
        self._height: int = 1080
        self._size: tuple = self._width, self._height
        self._window = None
        self._etatActuel: Etats = Etats.Expedition

    # Méthode lancée une fois servant a initialisé tout ce qu'il faut
    def on_init(self) -> None:
        pygame.init()
        self._window = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self._running = True

        plateau = PlateauDeJeu('src/maps/1.tmx')
        equipe = EquipeDePersonnages(Personnage("Frank",40, 12, 5, 5, "src/images/Smiguel.jpg"), Personnage("Albert",30, 15, 3, 2, "src/images/kv2v2v2.jpg"))
        self._expedition = Expedition(equipe, plateau)
        self._modeEvenement = None

    # Méthode définissant la boucle de jeu principale
    def on_execute(self) -> None:
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.time.Clock().tick(60)
            events = pygame.event.get()
            self.on_event(events)
            self.on_loop()
            self.on_render()
            self.change_state()
        self.on_cleanup()

    # lecture des evenements
    def on_event(self, events) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                self._running = False

            if self._etatActuel == Etats.Gestion:
                pass

            elif self._etatActuel == Etats.Expedition:
                self._whatAppend = self._expedition.on_event(event)

            elif self._etatActuel == Etats.Evenement:
                self._modeEvenement.on_event(events)
                break

            else:
                print("Etat inexistant dsl ...")

    # Calcul des mises à jours
    def on_loop(self) -> None:

        if self._etatActuel == Etats.Gestion:
            pass

        elif self._etatActuel == Etats.Expedition:
            self._expedition.on_loop()

        elif self._etatActuel == Etats.Evenement:
            self._modeEvenement.on_loop()

        else:
            print("Etat inexistant dsl ...")

    # Calcul des affichages
    def on_render(self) -> None:

        if self._etatActuel == Etats.Gestion:
            pass

        elif self._etatActuel == Etats.Expedition:
            self._window.fill((0, 0, 0))
            self._expedition.on_render(self._window)

        elif self._etatActuel == Etats.Evenement:
            self._modeEvenement.on_render(self._window)

        else:
            print("Etat inexistant dsl ...")
        pygame.display.flip()
        pass

    def change_state(self) -> None:
        if self._etatActuel == Etats.Gestion:
            pass
        elif self._etatActuel == Etats.Expedition:
            if self._whatAppend is not None:
                self._etatActuel = Etats.Evenement
                self._modeEvenement = ModeEvenement(Recompense(self._expedition.returnTypeCase(self._whatAppend).split("_")[0]))

        elif self._etatActuel == Etats.Evenement:
            if not self._modeEvenement.getEnCours():
                self._etatActuel = Etats.Expedition
                self._whatAppend = None
        else:
            print("Etat inexistant dsl ...")

    # Méthode pour quitter le jeu proprement
    def on_cleanup(self) -> None:
        pygame.quit()


if __name__ == "__main__":
    leJeu = Jeu()
    leJeu.on_execute()
