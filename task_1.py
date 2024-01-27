# Завдання 1

import random
from app.node import Node
from app.methods import *

if __name__ == "__main__":

    # Ключі двійкового дерева пошуку
    root_keys = random.sample(range(1, 100), 15)
    print(f"Ключі дерева: {root_keys}")

    # Створення дерева
    root = Node(root_keys.pop())
    while root_keys:
        root = insert(root, root_keys.pop())

    # Вивід дерева
    print(root)

    # Найбільше значення в дереві
    max_val = max_value_node(root)
    print(f"Найбільше значення в дереві: {max_val}")
