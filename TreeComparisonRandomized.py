from RB_Tree import RBTree
from ABR_Tree import ABRTree
import time
from random import randint


# Classe per comparare gli alberi
class TreeComparisonRandomized:
    # def __init__(self):
        # pass  # Dichiarazione di un costruttore vuoto

    def __init__(self):
        self.nums = []
        self.bst = ABRTree()  # Albero binario di ricerca
        self.rbtree = RBTree()  # Albero rosso nero
        self.a = None
        self.b = None

    # Fisher–Yates shuffle algorithm
    def shuffle_array(self, nums, n):
        # Inizio dall'ultimo elemento e faccio lo scambio uno per uno. Non abbiamo
        # bisogno d'iniziare dal primo elemento, ecco perché i > 0
        for i in range(n - 1, 0, -1):
            # Prendi un indice random da 0 a i
            j = randint(0, i + 1)

            # Scambia nums[i] con l'elemento dell'indice randomico, quindi j in questo caso
            nums[i], nums[j] = nums[j], nums[i]
        return nums

    def randomize_nums(self):
        self.nums = list(range(0, 10000))
        n = len(self.nums)
        self.shuffle_array(self.nums, n)

    def compare_random_insertion(self):
        self.randomize_nums()
        print("----- RANDOM INSERT -----")
        
        start_bst_time = time.process_time_ns()
        for num in self.nums:
            self.bst.insert(num)
        end_bst_time = time.process_time_ns() - start_bst_time
        print("BST: %s ns " % end_bst_time)

        start_rbt_time = time.process_time_ns()
        for num2 in self.nums:
            self.rbtree.insert_node(num2)
        end_rbt_time = time.process_time_ns() - start_rbt_time
        print("RBT: %s ns " % end_rbt_time)

        delta = end_bst_time - end_rbt_time
        print("Delta: %s ns " % delta)
        print("----------------------------\n")

    def compare_random_find(self, key):
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

    def compare_random_successor(self):
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

    def compare_random_predecessor(self):
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

    def compare_random_get_root(self):
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
