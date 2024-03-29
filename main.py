import TreeComparisonRandomized as TCR
import TreeComparisonUnbalanced as TCU
import random


def main():

    # Comparo il RBTree con il BST sbilanciato
    obj = TCU.TreeComparisonUnbalanced()
    print("--------------- UNBALANCED BST ---------------\n")
    obj.compare_unbalanced_insertion()
    obj.compare_unbalanced_find(11)
    obj.compare_unbalanced_successor()
    obj.compare_unbalanced_predecessor()
    obj.compare_unbalanced_get_root()
    print("--------------- END UNBALANCED ---------------\n")

    # Comparo il RBTree con il BST Randomizzato
    obj2 = TCR.TreeComparisonRandomized()
    print("--------------- RANDOMIZED BST ---------------\n")
    obj2.compare_random_insertion()
    obj2.compare_random_find(11)
    obj2.compare_random_successor()
    obj2.compare_random_predecessor()
    obj2.compare_random_get_root()
    print("--------------- END RANDOMIZED ---------------\n")


def main2():

    # Grafici di RBTree con il BST sbilanciato
    obj = TCU.TreeComparisonUnbalanced()
    arr = []
    arr2 = []
    print("--------------- UNBALANCED BST ---------------\n")
    obj.unbalanced_insertion_with_plot()

    TCU.elements.clear()
    TCU.elements2.clear()
    TCU.times.clear()
    TCU.times2.clear()
    for i in range(300):
        a, b = obj.unbalanced_find_with_plot(random.randint(0, 1000))
        if a is not None and b is not None and a.key != 0 and b.key != 0:
            arr.append((a, b))
    TCU.plt.title("FIND UNBALANCED")
    TCU.plt.plot(TCU.elements, TCU.times, marker="o", color='red')  # BST
    TCU.plt.plot(TCU.elements2, TCU.times2, marker="v", color='blue')  # RBT
    TCU.plt.show()

    TCU.elements.clear()
    TCU.elements2.clear()
    TCU.times.clear()
    TCU.times2.clear()
    TCU.count_bst = 0
    TCU.count_rbt = 0
    for i, y in arr:
        obj.unbalanced_predecessor_with_plot(i, y)
    TCU.plt.title("PREDECESSOR UNBALANCED")
    TCU.plt.plot(TCU.elements, TCU.times, marker="o", color='red')  # BST
    TCU.plt.plot(TCU.elements2, TCU.times2, marker="v", color='blue')  # RBT
    TCU.plt.show()
    print("--------------- END UNBALANCED ---------------\n")

    # Grafici di RBTree con il BST Randomizzato
    obj2 = TCR.TreeComparisonRandomized()
    print("--------------- RANDOMIZED BST ---------------\n")
    obj2.random_insertion_with_plot()

    TCR.elements.clear()
    TCR.elements2.clear()
    TCR.times.clear()
    TCR.times2.clear()
    for i in range(300):
        a, b = obj2.random_find_with_plot(random.randint(0, 1000))
        if a is not None and b is not None and a.key != 0 and b.key != 0:
            arr2.append((a, b))
    TCR.plt.title("FIND RANDOMIZED")
    TCR.plt.plot(TCR.elements, TCR.times, marker="o", color='green')  # BST
    TCR.plt.plot(TCR.elements2, TCR.times2, marker="v", color='blue')  # RBT
    TCR.plt.show()

    TCR.elements.clear()
    TCR.elements2.clear()
    TCR.times.clear()
    TCR.times2.clear()
    TCR.count_bst = 0
    TCR.count_rbt = 0
    for i, y in arr2:
        obj2.random_predecessor_with_plot(i, y)
    TCR.plt.title("PREDECESSOR RANDOMIZED")
    TCR.plt.plot(TCR.elements, TCR.times, marker="o", color='green')  # BST
    TCR.plt.plot(TCR.elements2, TCR.times2, marker="v", color='blue')  # RBT
    TCR.plt.show()
    print("--------------- END RANDOMIZED ---------------\n")


if __name__ == '__main__':
    main2()


# if __name__ == '__main__':
#     main()
