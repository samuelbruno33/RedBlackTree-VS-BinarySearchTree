from RB_Tree import RBTree
from ABR_Tree import ABRTree
import time
import matplotlib.pyplot as plt   # Import della libreria per effettuare i grafici in Python

count_bst = 0
count_rbt = 0
elements = []
elements2 = []
times = []
times2 = []


# Classe per comparare gli alberi in cui il nostro albero ABR ha elementi totalmente sbilanciati
class TreeComparisonUnbalanced:
    def __init__(self):
        self.arr = []
        self.bst = ABRTree()  # Albero binario di ricerca
        self.rbtree = RBTree()  # Albero rosso nero
        self.a = None
        self.b = None
        self.y = None

    def compare_unbalanced_insertion(self):
        self.arr = list(range(0, 10000))
        self.y = len(self.arr)

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

    def unbalanced_insertion_with_plot(self):
        count = 0
        count2 = 0
        self.arr = list(range(0, 300))
        self.y = len(self.arr)

        for num in self.arr:
            start_bst_time = time.process_time()
            self.bst.insert(num)
            count += 1
            end_bst_time = time.process_time() - start_bst_time
            elements.append(count)
            times.append(end_bst_time)

        for num2 in self.arr:
            start_rbt_time = time.process_time()
            self.rbtree.insert_node(num2)
            count2 += 1
            end_rbt_time = time.process_time() - start_rbt_time
            elements2.append(count2)
            times2.append(end_rbt_time)

        plt.title("INSERIMENTO UNBALANCED")
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.xlabel("Elementi")
        plt.ylabel("Tempo Operazioni")
        plt.plot(elements, times, marker="o", color='red')  # BST
        plt.plot(elements2, times2, marker="v", color='blue')   # RBT
        plt.show()

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

    def unbalanced_find_with_plot(self, key):
        global count_bst, count_rbt

        start_bst_time = time.process_time()
        self.a = self.bst.find(key)
        count_bst += 1
        end_bst_time = time.process_time() - start_bst_time
        elements.append(count_bst)
        times.append(end_bst_time)

        start_rbt_time = time.process_time()
        self.b = self.rbtree.find(key)
        count_rbt += 1
        end_rbt_time = time.process_time() - start_rbt_time
        elements2.append(count_rbt)
        times2.append(end_rbt_time)

        return self.a, self.b

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

    def unbalanced_predecessor_with_plot(self, a, b):
        global count_bst, count_rbt

        start_bst_time = time.process_time()
        self.bst.predecessor(a)
        count_bst += 1
        end_bst_time = time.process_time() - start_bst_time
        elements.append(count_bst)
        times.append(end_bst_time)

        start_rbt_time = time.process_time()
        self.rbtree.predecessor(b)
        count_rbt += 1
        end_rbt_time = time.process_time() - start_rbt_time
        elements2.append(count_rbt)
        times2.append(end_rbt_time)

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
