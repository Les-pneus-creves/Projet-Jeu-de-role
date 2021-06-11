from Slot_inventaire import Slot_inventaire
import Objet
import math


class Inventaire(list):

    def __init__(self, nbArme, nbEquipement, nbRessource):
        """ Un `Inventaire` est une liste de plusieurs `src.Slot_inventaire` dans lequel est stocké un `src.Objet`.

            Parameters
            ----------
            nbArme : int
                le nombre de slots d'armes
            nbEquipement : int
                le nombre de slots d'équipement
            nbRessources : int
                le nombre de slots ressources
        """

        super(Inventaire, self).__init__()
        for i in range(nbArme):
            self.append(Slot_inventaire(Objet.Arme))
        for i in range(nbEquipement):
            self.append(Slot_inventaire(Objet.Equipement))
        for i in range(nbRessource):
            self.append(Slot_inventaire(Objet.Objet))

    def append(self, slot: Slot_inventaire):
        """Overload de la méthode append des list, cela permet d'ajouter que des `Slot_inventaire` à notre Inventaire"""

        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).append(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisés')

    def insert(self, index, slot: Slot_inventaire):
        """ Overload de la méthode insert des list, cela permet d'être sur d'ajouter que des `Slot_inventaire` à notre `Inventaire`.

            Pas forcément utile mais pour que ce soit jolie
        """

        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).insert(index, slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisés')

    def __add__(self, slot: Slot_inventaire):
        """ Overload de l'opérateur +, cela permet d'ajouter que des `Slot_inventaire` à notre `Inventaire`

            Pas forcément utile mais pour que se soit jolie
        """

        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).__add__(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def __iadd__(self, slot: Slot_inventaire):
        """ Overload de l'opérateur +=, cela permet d'ajouter que des `Slot_inventaire` à notre `Inventaire`

            Pas forcément utile mais pour que se soit jolie
        """

        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).__iadd__(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def __str__(self):
        retour = "["
        i = 0
        for slot in self:
            retour += str(slot)
            if i < len(self) - 1:
                retour += ", "
                i += 1
        retour += "]"
        return retour

    def getArme(self):
        """Retourne l'arme contenue dans l'inventaire

        Retourne `None` si il n'y a pas d'arme
        """

        for slot in self:
            if slot.getTypeObjet() is Objet.Arme:
                return slot.getObjet()
        return None

    def getEquipement(self):
        """Retourne l'équipement contenue dans l'inventaire

        Retourne `None` si il n'y a pas d'équipement
        """

        for slot in self:
            if slot.getTypeObjet() is Objet.Equipement:
                return slot.getObjet()
        return None


    def listObjetUnique(self) -> list:
        """Retourne une liste des objets présent dans l'`Inventaire`."""

        liste = []
        for objet in self.tolistofObjet():
            if objet not in liste and objet is not None:
                liste.append(objet)
        return liste

    def tolistofObjet(self) -> list:
        """Retourne sous forme de liste l'objet contenue dans chaque slots
        (l'emplacement de la liste est vide s'il n'y a pas d'objet dans le slot).
        """

        liste = []
        for slot in self:
            liste.append(slot.getObjet())
        return liste

    def slotsOfThisObjet(self, objet: Objet) -> list:
        """Retourne la liste des slots dans lequel ce trouve l'objet précisé en paramètre.

         Si l'objet n'est pas dans l'inventaire la méthode retourne une liste vide.
         """

        listePos = []
        i = 0
        for element in self.tolistofObjet():
            if element is objet:
                listePos.append(i)
            i += 1
        return listePos

    def contientObjet(self, objet: Objet) -> int:
        """Retourne le numéro du slot dans lequel ce trouve l'objet précisé en paramètre.

        Si l'objet n'est pas dans l'inventaire la méthode retourne `-1`.
        """

        i = 0
        for slot in self:
            slotObjet = slot.getObjet()
            if slotObjet is not None:
                if slotObjet.getNom() == objet.getNom():
                    return i
            i += 1
        return -1

    def ajouter(self, objet: Objet, nombre: int = 1):
        """Ajoute dans l'inventaire l'objet donné en paramètre autant de fois que précisé (par défaut 1 seul)."""

        positions = self.slotsOfThisObjet(objet)
        for position in positions:
            if not self[position].plein():
                ajout = self[position].ajouter(nombre=nombre)
                if ajout > 0:
                    self.ajouter(objet, ajout)
                    return
                elif ajout == 0:
                    return
        else:
            for slot in self:
                ajout = slot.ajouter(objet, nombre)
                if ajout == 0:
                    break
                elif ajout == -1:
                    continue
                else:
                    self.ajouter(objet, ajout)
                    return

    def retirer(self, objet: Objet, nombre=1):
        """Retire de l'inventaire l'objet donné en paramètre autant de fois que précisé (par défaut 1 seul)."""

        position = self.contientObjet(objet)
        if position == -1:
            print("pas d'objets de ce type dans l'inventaire")
        else:
            retrait = self[position].retirer(nombre)
            if retrait < 0:
                self.retirer(objet, - retrait)
        self.trier()

    def trier(self):
        """Tri l'inventaire de sorte à ce qu'il n'y ai pas plusieurs slots d'un même objet à moitié vide."""

        repetitionObjects = dict.fromkeys(self.listObjetUnique(), 0)
        # Analyse de l'inventaire
        for objet in repetitionObjects:
            # On récupère les positions dans l'inventaire de chaque objets contenue dans l'inventaire
            positionsObjet = self.slotsOfThisObjet(objet)

            # On compte combien on a d'élément de cette objets dans l'inventaire en comptant tous les slots.
            nb = 0
            for pos in positionsObjet:
                nb += self[pos].getNbContenue()

            # On enregistre l'information de nb d'élément et du nombre de slots pris pour chaque objets
            repetitionObjects[objet] = nb, len(positionsObjet)

        # Trie de l'inventaire en conséquence
        for objet, (nb, nbslots) in repetitionObjects.items():
            if math.ceil(nb / objet.getStackable()) < nbslots:
                self.retirer(objet, nb)
                self.ajouter(objet, nb)

    def vide(self):
        for slot in self:
            if not slot.vide():
                return False
        return True

    def render(self, window, minx, miny):
        """Permet d'afficher l'inventaire dans une fenêtre pygame à une position donné.

        Parameters
        ----------
        window : pygame.Surface
            La fenêtre sur laquelle on veut afficher l'inventaire.
        minx : int
            Position x (en pixel) à partir de laquelle l'inventaire sera affiché sur la fenêtre.
        miny : int
            Position y (en pixel) à partir de laquelle l'inventaire sera affiché sur la fenêtre.
        """

        posx = minx
        posy = miny

        i = 1
        for slot in self:
            slot.render(window, posx, posy)
            if not i % 4:
                posy += 60
                posx = minx
            else:
                posx += 60
            i += 1


if __name__ == "__main__":
    inventaire = Inventaire(1, 1, 5)
    patate = Objet.Objet("Patate", "prout", 3)
    oignon = Objet.Objet("Oignons", "prout", 4)
    fusil = Objet.Arme("Fusil", "prout", 1)

    inventaire.ajouter(patate, 2)
    inventaire.ajouter(patate, 3)
    inventaire.ajouter(oignon, 5)
    inventaire.ajouter(fusil)

    print(inventaire)
    inventaire.retirer(fusil)
    inventaire.retirer(patate, 1)
    inventaire.ajouter(patate, 3)

    print(inventaire)
