from TreeComparisonRandomized import TreeComparisonRandomized
from TreeComparisonUnbalanced import TreeComparisonUnbalanced


# Dichiarazione della funzione main
def main():

    # Comparo il RBTree con il BST sbilanciato
    obj = TreeComparisonUnbalanced()
    print("--------------- UNBALANCED BST ---------------\n")
    obj.compare_unbalanced_insertion()
    obj.compare_unbalanced_find(11)
    obj.compare_unbalanced_successor()
    obj.compare_unbalanced_predecessor()
    obj.compare_unbalanced_get_root()
    print("--------------- END UNBALANCED ---------------\n")

    # Comparo il RBTree con il BST Randomizzato
    obj2 = TreeComparisonRandomized()
    print("--------------- RANDOMIZED BST ---------------\n")
    obj2.compare_random_insertion()
    obj2.compare_random_find(11)
    obj2.compare_random_successor()
    obj2.compare_random_predecessor()
    obj2.compare_random_get_root()
    print("--------------- END RANDOMIZED ---------------\n")


# In questo modo viene richiamato il main come funzione di run del programma
if __name__ == '__main__':
    main()
