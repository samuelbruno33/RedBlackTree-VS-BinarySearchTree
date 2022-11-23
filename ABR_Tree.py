#import sys


# Definizione della classe Nodo
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


# Definizione di albero binario di ricerca
class ABRTree:
    def __init__(self):
        self.root = None

    # Funzione d'inserimento dell'albero
    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    # Funzione dove ricerco una chiave confrontando un nodo e la chiave che si vuole ricercare
    def findNode(self, node, key):
        if node is None or key == node.key:
            return node

        if key < node.key:
            return self.findNode(node.left, key)
        return self.findNode(node.right, key)

    # Funzione di ricerca vera e propria, dove viene passato l'albero stesso
    def find(self, k):
        return self.findNode(self.root, k)

    # Funzione dove trovo il minimo (valore più a sinistra)
    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Funzione dove trovo il massimo (valore più a destra)
    def maximum(self, node):
        while node.right is not None:
            node = node.right
        return node

    # Funzione dove trovo il successore
    def successor(self, x):
        if x.right is not None:
            a = self.minimum(x.right)
            return a

        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    # Funzione dove trovo il predecessore
    def predecessor(self, x):
        if x.left is not None:
            a = self.maximum(x.left)
            return a

        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    # Ritorna la radice
    def get_root(self):
        return self.root

    """
    # Creo il layout per poter stampare l'albero
    def __printHelper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(currPtr.key)

            self.__printHelper(currPtr.left, indent, False)
            self.__printHelper(currPtr.right, indent, True)

    # Funzione di stampa dell'albero vera e propria, dove viene passato l'albero stesso
    def print_abr_tree(self):
        self.__printHelper(self.root, "", True)
        """
