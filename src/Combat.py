import Evenement

class Combat(Evenement):

    def __init__(self, equipe, plateau):
        super().__init__(self, )
        self.__log = ""
        self.__equipeMechant = None   #J'ai mis none en attendant


    #Méthode permettant de donner au combat l'équipe de personnage Joueur qui va se battre
    def lancement(self,EquipePerso):
        pass
    
    #Méthode permettant de déterminer l'ordre des tours des personnages lors du combat
    def __creerOrdreTour(self,ep1, ep2):
        pass
    
    #Méthode permmetant de selectionné une cible dans une équipe donnée
    def __choisirCible(self,EquipePerso):
        pass
    