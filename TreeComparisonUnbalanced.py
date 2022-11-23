from RB_Tree import RBTree
from ABR_Tree import ABRTree
import time


# Classe per comparare gli alberi in cui il nostro albero BST ha elementi totalmente sbilanciati
class TreeComparisonUnbalanced:
    # def __init__(self):
        # pass  # Dichiarazione di un costruttore vuoto

    def __init__(self):
        self.arr = []
        self.bst = ABRTree()  # Albero binario di ricerca
        self.rbtree = RBTree()  # Albero rosso nero
        self.a = None
        self.b = None

    def compare_unbalanced_insertion(self):
        self.arr = list(range(0, 10000))

        print("----- UNBALANCED INSERT -----")

        start_bst_time = time.process_time_ns()
        for num in self.arr:
            self.bst.insert(num)
        end_bst_time = time.process_time_ns() - start_bst_time
        print("BST: %s ns " % end_bst_time)

        start_rbt_time = time.process_time_ns()
        for num2 in self.arr:
            self.rbtree.insert_node(num2)
        end_rbt_time = time.process_time_ns() - start_rbt_time
        print("RBT: %s ns " % end_rbt_time)

        delta = end_bst_time - end_rbt_time
        print("Delta: %s ns " % delta)
        print("----------------------------\n")

    def compare_unbalanced_find(self, key):
        print("----- FIND -----")
        start_bst_time = time.process_time_ns()
        self.a = self.bst.find(key)
        end_bst_time = time.process_time_ns() - start_bst_time
        print("BST: %s ns " % end_bst_time)

        start_rbt_time = time.process_time_ns()
        self.b = self.rbtree.find(key)
        end_rbt_time = time.process_time_ns() - start_rbt_time
        print("RBT: %s ns " % end_rbt_time)

        delta = end_bst_time - end_rbt_time
        print("Delta: %s ns " % delta)
        print("----------------------------\n")

    def compare_unbalanced_successor(self):
        print("----- SUCCESSOR -----")

        start_bst_time = time.process_time_ns()
        self.bst.successor(self.a)
        end_bst_time = time.process_time_ns() - start_bst_time
        print("BST: %s ns " % end_bst_time)

        start_rbt_time = time.process_time_ns()
        self.rbtree.successor(self.b)
        end_rbt_time = time.process_time_ns() - start_rbt_time
        print("RBT: %s ns " % end_rbt_time)

        delta = end_bst_time - end_rbt_time
        print("Delta: %s ns " % delta)
        print("----------------------------\n")

    def compare_unbalanced_predecessor(self):
        print("----- PREDECESSOR -----")

        start_bst_time = time.process_time_ns()
        self.bst.predecessor(self.a)
        end_bst_time = time.process_time_ns() - start_bst_time
        print("BST: %s ns " % end_bst_time)

        start_rbt_time = time.process_time_ns()
        self.rbtree.predecessor(self.b)
        end_rbt_time = time.process_time_ns() - start_rbt_time
        print("RBT: %s ns " % end_rbt_time)

        delta = end_bst_time - end_rbt_time
        print("Delta: %s ns " % delta)
        print("----------------------------\n")

    def compare_unbalanced_get_root(self):
        print("----- GET_ROOT -----")

        start_bst_time = time.process_time_ns()
        self.bst.get_root()
        end_bst_time = time.process_time_ns() - start_bst_time
        print("BST: %s ns " % end_bst_time)

        start_rbt_time = time.process_time_ns()
        self.rbtree.get_root()
        end_rbt_time = time.process_time_ns() - start_rbt_time
        print("RBT: %s ns " % end_rbt_time)

        delta = end_bst_time - end_rbt_time
        print("Delta: %s ns " % delta)
        print("----------------------------\n")
