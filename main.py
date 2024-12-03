import avl_tree as avl
import binary_search_tree as bst
import red_black_tree as rbt
import search
import utilities as util
from drawing import draw_tree

import matplotlib.pyplot as plt
import random
import numpy as np

def generate_bst_heights():
    bst_heights = []
    bsTree = bst.BinarySearchTree()
    for _ in range(100):
        for _ in range(100):
            while True:
                num = random.randint(0, 10000)
                if not util.find(bsTree.root, num):
                    bsTree.insert(num)
                    break
        height = bsTree.get_height(bsTree.root)
        bst_heights.append(height)
    return bst_heights

def generate_avl_heights():
    avl_heights = []
    for i in range(1, 101):
        keys = list(range(1, 100 * i + 1))

        avl_tree = avl.AVLTree()
        for key in keys:
            avl_tree.root = avl_tree.insert(avl_tree.root, key)
        avl_heights.append(avl_tree.get_height(avl_tree.root))

    return avl_heights


def generate_rb_heights():
    rb_heights = []

    for i in range(1, 101):
        keys = list(range(1, 100 * i + 1))

        rb = rbt.RedBlackTree()
        for key in keys:
            rb.insert(key)
        rb_heights.append(rb.get_height(rb.root))

    return rb_heights


def calculate_regression(n, heights):
    coefficients = np.polyfit(n, heights, 2)
    polynomial = np.poly1d(coefficients)
    equation = f"h = {coefficients[0]:.10f}n² + {coefficients[1]:.6f}n + {coefficients[2]:.2f}"
    return polynomial, equation

def plot_graph(n, heights, polynomial, equation, title, tree_label, fit_color, log_color, height_color):
    x_fit = np.linspace(min(n), max(n), 500)
    y_fit = polynomial(x_fit)

    plt.plot(x_fit, y_fit, color=fit_color, label=f"Regression Polynomial {equation}", linestyle=':')
    plt.step(n, np.log2(n), label='h = log(n)', color=log_color, linestyle='--', where='post')
    plt.step(n, heights, label=tree_label, color=height_color, where='post')
    plt.xlabel('Number of Keys')
    plt.ylabel('Tree Height')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

def get_height_on_number_of_elements_dependance():
    number_of_elements = [_ for _ in range(100, 10001, 100)]

    Hbst = generate_bst_heights()
    Havl = generate_avl_heights()
    Hrb = generate_rb_heights()

    poly_bst, eq_bst = calculate_regression(number_of_elements, Hbst)
    poly_avl, eq_avl = calculate_regression(number_of_elements, Havl)
    poly_rb, eq_rb = calculate_regression(number_of_elements, Hrb)

    plot_graph(number_of_elements, Hbst, poly_bst, eq_bst,
               'BST Height vs Number of Keys',
               'BST Height Dependence on Keys',
               'green', 'green', 'blue')

    plot_graph(number_of_elements, Havl, poly_avl, eq_avl,
               'AVL Tree Height vs Number of Keys',
               'AVL Height Dependence on Keys',
               'green', 'green', 'red')

    plot_graph(number_of_elements, Hrb, poly_rb, eq_rb,
               'Red-Black Tree Height vs Number of Keys',
               'Red-Black Tree Height Dependence on Keys',
               'green', 'green', 'purple')


def show_search_variations():
    BST = bst.BinarySearchTree()
    AVL = avl.AVLTree()
    RBT = rbt.RedBlackTree()

    keys = [_ for _ in range(10)]
    random.shuffle(keys)
    for key in keys:
        BST.insert(key)
        AVL.root = AVL.insert(AVL.root, key)
        RBT.insert(key)

    travs = { 'inorder', 'postorder', 'preorder' }

    for trav in travs:
        print("BST")
        search.traverse(BST.root, trav)
        print('\n')
        print("AVL")
        search.traverse(AVL.root, trav)
        print('\n')
        print("RBT")
        search.traverse(RBT.root, trav)
        print('\n')

    print("Обход в ширину")
    print("BST")
    print(search.bfs(BST.root))
    print('\n')
    print("AVL")
    print(search.bfs(AVL.root))
    print('\n')
    print("RBT")
    print(search.bfs(RBT.root))
    print('\n')


if __name__ == "__main__":
    get_height_on_number_of_elements_dependance()
    show_search_variations()