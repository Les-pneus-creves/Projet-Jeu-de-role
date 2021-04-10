import pygame
from enum import Enum
from EquipeDePersonnages import EquipeDePersonnages
from Expedition import Expedition
from PlateauDeJeu import PlateauDeJeu
from ModeEvenement import ModeEvenement


Etats = Enum('Etats', 'Gestion Expedition Evenement')

class Jeu:
    def __init__(self):
        self.__nbTour: int = 0    
        self.__running: bool = True
        self.__width: int = 1080
        self.__height: int = 1080
        self.__size: tuple = self.__width, self.__height
        self.__window = None
        self.__etatActuel: Etats = Etats.Expedition

    #Méthode lancée une fois servant a initialisé tout ce qu'il faut
    def on_init(self) -> None:
        pygame.init()
        self.__window = pygame.display.set_mode(self.__size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.__running = True

        plateau = PlateauDeJeu('src/maps/1.tmx')
        equipe = EquipeDePersonnages([1, 2, 3])
        self.__expedition = Expedition(equipe, plateau)
        self.__modeEvenement = None
    
    #Méthode définissant la boucle de jeu principale
    def on_execute(self) -> None:
        if self.on_init() == False:
            self.__running = False

        while(self.__running ):
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
                self.__running = False
            
            if self.__etatActuel == Etats.Gestion:
                pass

            elif self.__etatActuel == Etats.Expedition:
                self.__whatAppend = self.__expedition.on_event(event)

            elif self.__etatActuel == Etats.Evenement:
                self.__modeEvenement.on_event(events)
                break

            else:
                print("Etat inexistant dsl ...")

    #Calcul des mises à jours
    def on_loop(self) -> None:
        
        if self.__etatActuel == Etats.Gestion:
            pass

        elif self.__etatActuel == Etats.Expedition:
            self.__expedition.on_loop()

        elif self.__etatActuel == Etats.Evenement:
            self.__modeEvenement.on_loop()

        else:
            print("Etat inexistant dsl ...")

    #Calcul des affichages
    def on_render(self) -> None:
        
        if self.__etatActuel == Etats.Gestion:
            pass

        elif self.__etatActuel == Etats.Expedition:
            self.__expedition.on_render(self.__window)

        elif self.__etatActuel == Etats.Evenement:
            self.__modeEvenement.on_render(self.__window)

        else:
            print("Etat inexistant dsl ...")
        pygame.display.flip()
        pass

    def change_state(self) -> None:
        if self.__etatActuel == Etats.Gestion:
            pass
        elif self.__etatActuel == Etats.Expedition:
            if(self.__whatAppend is not None):
                self.__etatActuel = Etats.Evenement
                self.__modeEvenement = ModeEvenement(self.__expedition.returnTypeCase(self.__whatAppend))

        elif self.__etatActuel == Etats.Evenement:
            if(not self.__modeEvenement.getEnCours()):
                self.__etatActuel = Etats.Expedition
                self.__whatAppend = None
        else:
            print("Etat inexistant dsl ...")

    #Méthode pour quitter le jeu proprement  
    def on_cleanup(self) -> None:
        pygame.quit()

        

if __name__ == "__main__" :
    leJeu = Jeu()
    leJeu.on_execute()