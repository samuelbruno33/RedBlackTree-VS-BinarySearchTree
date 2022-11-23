import sys


# Definizione della classe Nodo dell'albero RB
class RBNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.red = False  #di default è nero


# Definizione dell'albero rosso-nero
class RBTree:
    def __init__(self):
        self.rbnode = RBNode(0)
        self.rbnode.red = False
        self.rbnode.left = None
        self.rbnode.right = None
        self.root = self.rbnode

    # Funzione d'inserimento dell'albero
    def insert_node(self, key):
        node = RBNode(key)
        node.parent = None
        node.left = self.rbnode
        node.right = self.rbnode
        node.red = True  # un nuovo nodo deve essere rosso

        parent = None
        current = self.root
        while current != self.rbnode:
            parent = current
            if node.key < current.key:
                current = current.left
            elif node.key > current.key:
                current = current.right
            else:
                return

        # Setta il parent e inserisce un nuovo nodo
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        # se il nuovo nodo è una radice, fai un return
        if node.parent is None:
            node.red = False
            return

        # se il nonno non esiste, fai un return
        if node.parent.parent is None:
            return

        self.rb_insert_fixup(node)

    # Funzione di fixup per l'inserimento
    def rb_insert_fixup(self, node):
        while node != self.root and node.parent.red:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left  # E' lo zio
                if u.red:
                    u.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right  # E' lo zio

                if u.red:
                    u.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.right_rotate(node.parent.parent)
        self.root.red = False

    # Funzione di rotazione sinistra dei nodi per bilanciare l'albero
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.rbnode:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Funzione di rotazione destra dei nodi per bilanciare l'albero
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.rbnode:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Funzione dove ricerco una chiave confrontando un nodo e la chiave che si vuole ricercare
    def findNode(self, node, key):
        if node == self.rbnode:
            return node

        if key == node.key:
            return node

        if key < node.key:
            return self.findNode(node.left, key)
        return self.findNode(node.right, key)

    # Funzione di ricerca vera e propria, dove viene passato l'albero stesso
    def find(self, k):
        return self.findNode(self.root, k)

    # Funzione dove trovo il minimo (valore più a sinistra)
    def minimum(self, node):
        while node.left != self.rbnode:
            node = node.left
        return node

    # Funzione dove trovo il massimo (valore più a destra)
    def maximum(self, node):
        while node.right != self.rbnode:
            node = node.right
        return node

    # Funzione dove trovo il successore
    def successor(self, x):
        if x.right != self.rbnode:
            successor = self.minimum(x.right)
            return successor

        # Se x ha sotto albero destro vuoto, allora il suo successore è l'antenato più prossimo di x
        # il cui figlio sinistro è anche antenato di x
        y = x.parent
        while y != self.rbnode and x == y.right:
            x = y
            y = y.parent
        return y

    # Funzione dove trovo il predecessore
    def predecessor(self, x):
        if x.left != self.rbnode:
            predecessor = self.maximum(x.left)
            return predecessor

        y = x.parent
        while y != self.rbnode and x == y.left:
            x = y
            y = y.parent
        return y

    # Ritorna la radice
    def get_root(self):
        return self.root

    # Creo il layout per poter stampare l'albero
    def __print_helper(self, node, indent, last):
        if node != self.rbnode:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "  # Indenta di 5 spazi la linea sotto la R
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.red is True else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)  # Va a sinistra e inizia a scrivere dall'ultimo nodo sinistro che trova facendo ricorsione all'indietro
            self.__print_helper(node.right, indent, True)

    # Funzione di stampa dell'albero vera e propria, dove viene passato l'albero stesso
    def print_rb_tree(self):
        self.__print_helper(self.root, "", True)
