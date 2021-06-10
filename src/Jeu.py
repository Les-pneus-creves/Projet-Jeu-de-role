"""
Programme principale
"""

import pygame
from enum import Enum
from EquipeDePersonnages import EquipeDePersonnages
from Personnage import Personnage
from Expedition import Expedition
from PlateauDeJeu import PlateauDeJeu
from ModeEvenement import ModeEvenement
from Recompense import Recompense
from Combat import Combat
import Objet

Etats = Enum('Etats', 'Gestion Expedition Evenement')
"""Enum permettant de gérer la machine à état du jeu de manière plus jolie"""


class Jeu:
    def __init__(self):
        self._nbTour: int = 0
        self._running: bool = True
        self._width: int = 1080
        self._height: int = 1080
        self._size: tuple = self._width, self._height
        self._window = None
        self._etatActuel: Etats = Etats.Expedition

    def on_init(self) -> None:
        """Méthode lancée une fois servant a initialise tout ce qu'il faut"""
        pygame.init()
        self._window = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self._running = True
        Objet.loadAllObjets()

        plateau = PlateauDeJeu('src/maps/1.tmx')
        equipe = EquipeDePersonnages(Personnage("Frank", 40, 12, 5, 5, "src/images/Smiguel.jpg"),
                                     Personnage("Albert", 30, 15, 3, 2, "src/images/kv2v2v2.jpg"))
        self._expedition = Expedition(equipe, plateau)
        self._modeEvenement = None

    def on_execute(self) -> None:
        """Méthode définissant la boucle de jeu principale"""
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

    def on_event(self, events) -> None:
        """Lecture des évènements pygame tel les clics"""
        for event in events:
            if event.type == pygame.QUIT:
                self._running = False

            if self._etatActuel == Etats.Gestion:
                pass

            elif self._etatActuel == Etats.Expedition:
                self._whatAppend = self._expedition.on_event(event)

            elif self._etatActuel == Etats.Evenement:
                self._modeEvenement.on_event(events, event)
                break

            else:
                print("Etat inexistant dsl ...")

    def on_loop(self) -> None:
        """Calcul des mises à jours du jeu"""

        if self._etatActuel == Etats.Gestion:
            pass

        elif self._etatActuel == Etats.Expedition:
            self._expedition.on_loop()

        elif self._etatActuel == Etats.Evenement:
            self._modeEvenement.on_loop()

        else:
            print("Etat inexistant dsl ...")

    def on_render(self) -> None:
        """Calcul des affichages et affichage sur la fenêtre"""

        if self._etatActuel == Etats.Gestion:
            self._window.fill((255, 70, 70))

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
        """Calcul gérant le changement d'état de la machine"""
        if self._etatActuel == Etats.Gestion:
            pass
        elif self._etatActuel == Etats.Expedition:
            if self._whatAppend is not None:
                self._etatActuel = Etats.Evenement
                TypeCase = self._expedition.returnTypeCase(self._whatAppend).split("_")
                event = Recompense(TypeCase[0])

                if TypeCase[0] == "Tour" or TypeCase[1].startswith("S"):
                    event = Combat(self._expedition.getEquipe(), "Bandit")
                    print("Combat contre Bandit")
                if TypeCase[0] == "Archer" or TypeCase[1].startswith("R"):
                    event = Combat(self._expedition.getEquipe(), "Soldat")
                    print("Combat contre Soldat")
                if TypeCase[0] == "Arche" or TypeCase[0] == "Maison" or TypeCase[0] == "Ferme" or TypeCase[1].startswith("A"):
                    event = Combat(self._expedition.getEquipe(), "Chien")
                    print("Combat contre Chien")
                if TypeCase[0] == "Mine":
                    event = Combat(self._expedition.getEquipe(), "Kv2v2v2")
                    print("Combat contre Kv2v2v2")

                event.lancement()
                self._modeEvenement = ModeEvenement(event, self._expedition.getEquipe())

        elif self._etatActuel == Etats.Evenement:
            if not self._modeEvenement.getEnCours():
                self._etatActuel = Etats.Expedition
                self._whatAppend = None
                print(self._modeEvenement.getVictoire())
                if self._modeEvenement.getVictoire() == False:
                    self._etatActuel = Etats.Gestion
        else:
            print("Etat inexistant dsl ...")

    def on_cleanup(self) -> None:
        """Méthode pour quitter le jeu proprement"""
        pygame.quit()


if __name__ == "__main__":
    leJeu = Jeu()
    leJeu.on_execute()
