import pygame


class Jeu:
    
    def __init__(self):
        self.__nbTour = 0
        self.on_init()

    
    def on_init(self):
        pygame.init()
        self.__display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.__running = True
    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        pass

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.flip()
        pass
        
    def on_cleanup(self):
        pygame.quit()



if __name__ == "__main__" :
    leJeu = Jeu()
    leJeu.on_execute()