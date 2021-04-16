class Slot_inventaire:
    def __init__(self, typeObjet: type):
        self._objet = None
        self._typeObjet = typeObjet
        self._nbContenue = 0

    def remplir(self, objet, nombre: int = 1):
        if self.puisJeAjouter(objet):
            self._objet = objet
            self._nbContenue = nombre
        else :
            print("Tu ne peux pas mettre cette objet dans ce slot ...")

    def vider(self):
        self._nbContenue = 0

    def ajouter(self, nombre: int = 1):
        self._nbContenue += nombre

    def retirer(self, nombre: int = 1):
        self._nbContenue -= nombre

    def puisJeAjouter(self, objet):
        return type(objet) is self._typeObjet
