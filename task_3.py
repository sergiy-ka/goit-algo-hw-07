# Завдання 3

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

    # Сума всіх значень у дереві
    sum_val = sum_values(root)
    print(f"Сума всіх значень у дереві: {sum_val}")
