from Objet import Objet


class Slot_inventaire:
    def __init__(self, typeObjet: str):
        self._objet = None
        self._typeObjet = typeObjet
        self._nbContenue = 0

    def __str__(self):
        return "[" + str(self._objet) + ", " + self._typeObjet + ", " + str(self._nbContenue) + "]"

    def vider(self):
        self._nbContenue = 0
        self._objet = None

    def ajouter(self, objet: Objet = None, nombre: int = 1):
        if objet is None and self._objet is not None:
            objet = self._objet

        if self.puisJeAjouter(objet):
            self._objet: Objet = objet
            if not self.plein():
                if self._nbContenue + nombre > self._objet.getStackable():
                    nombre -= self._objet.getStackable() - self._nbContenue
                    self._nbContenue = self._objet.getStackable()
                    return nombre
                else:
                    self._nbContenue += nombre
                    return 0
        return -1

    def retirer(self, nombre: int = 1):
        self._nbContenue -= nombre
        if self._nbContenue <= 0:
            nb = self._nbContenue
            self.vider()
            return nb
        else:
            return 0

    def puisJeAjouter(self, objet):
        if objet is not None:
            if self._objet is None:
                return objet.getNom().split("_")[0] == self._typeObjet
            else:
                return objet.getNom() == self._objet.getNom()
        return False

    def getObjet(self):
        if not self.vide():
            return self._objet
        return None

    def vide(self):
        if self._nbContenue == 0 and self._objet is None:
            return True
        return False

    def plein(self):
        if self._nbContenue == self._objet.getStackable():
            return True
        return False

    def getNbContenue(self):
        return self._nbContenue