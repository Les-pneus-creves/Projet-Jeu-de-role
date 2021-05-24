from Slot_inventaire import Slot_inventaire
from Objet import Objet
import math


class Inventaire(list):

    def __init__(self, nbArme, nbEquipement, nbRessources):
        """ En faite se serais plus pour l'inventaire personnage toutes ces spécificité.
            Pour l'inventaire de base on ferait des slots capable d'accueillir tout types d'objets (les coffres)"""
        super(Inventaire, self).__init__()
        for i in range(nbArme):
            self.append(Slot_inventaire("Arme"))
        for i in range(nbEquipement):
            self.append(Slot_inventaire("Equipement"))
        for i in range(nbRessources):
            self.append(Slot_inventaire("Ressources"))

    def append(self, slot: Slot_inventaire):
        """Overload de la méthode append des list, cela permet d'ajouter que des Slot_inventaire à notre Inventaire"""
        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).append(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def insert(self, index, slot: Slot_inventaire):
        """ Overload de la méthode insert des list, cela permet d'ajouter que des Slot_inventaire à notre Inventaire
            Pas forcément utile mais pour que se soit jolie"""
        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).insert(index, slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def __add__(self, slot: Slot_inventaire):
        """ Overload de l'opérateur +, cela permet d'ajouter que des Slot_inventaire à notre Inventaire
            Pas forcément utile mais pour que se soit jolie"""
        if isinstance(slot, Slot_inventaire):
            super(Inventaire, self).__add__(slot)
        else:
            raise ValueError('Seul les Slot_inventaire sont autorisé')

    def __iadd__(self, slot: Slot_inventaire):
        """ Overload de l'opérateur +=, cela permet d'ajouter que des Slot_inventaire à notre Inventaire
            Pas forcément utile mais pour que se soit jolie"""
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

    def listObjetUnique(self):
        liste = []
        for objet in self.tolistofObjet():
            if objet not in liste and objet is not None:
                liste.append(objet)
        return liste

    def tolistofObjet(self):
        liste = []
        for slot in self:
            liste.append(slot.getObjet())
        return liste

    def slotsOfThisObjet(self, objet: Objet):
        listePos = []
        i = 0
        for element in self.tolistofObjet():
            if element is objet:
                listePos.append(i)
            i += 1
        return listePos

    def contientObjet(self, objet: Objet):
        i = 0
        for slot in self:
            slotObjet = slot.getObjet()
            if slotObjet is not None:
                if slotObjet.getNom() == objet.getNom():
                    return i
            i += 1
        return -1

    def ajouter(self, objet: Objet, nombre=1):
        position = self.contientObjet(objet)
        if position != -1 and not self[position].plein():
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
        position = self.contientObjet(objet)
        if position == -1:
            print("pas d'objets de ce type dans l'inventaire")
        else:
            retrait = self[position].retirer(nombre)
            if retrait < 0:
                self.retirer(objet, - retrait)

    def trier(self):
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
            if math.ceil(nb/objet.getStackable()) < nbslots:
                self.retirer(objet, nb)
                self.ajouter(objet, nb)

    def render(self, window, minx, miny):
        posx = minx
        posy = miny

        i = 1
        for slot in self:
            slot.render(window, posx, posy)
            if i % 4:
                posy += 60
                posx = minx
            else:
                posx += 60
            i += 1


if __name__ == "__main__":
    inventaire = Inventaire(1, 1, 5)
    patate = Objet("Ressources_Patate", "prout", 3)
    oignon = Objet("Ressources_Oignons", "prout", 4)
    fusil = Objet("Arme_Fusil", "prout", 1)

    inventaire.ajouter(patate, 2)
    inventaire.ajouter(patate, 3)
    inventaire.ajouter(oignon, 5)
    inventaire.ajouter(fusil)

    print(inventaire)
    inventaire.retirer(fusil)
    inventaire.retirer(patate, 2)

    print(inventaire)
    inventaire.trier()

    print(inventaire)
