import abc #module pour classe abstraite

class Evenement(metaclass=abc.ABCMeta):

    def __init__(self):
        self.__enCours = True
        self.__texteDescr = ""

    @abc.abstractmethod
    def lancement(self,EquipePerso):
        pass