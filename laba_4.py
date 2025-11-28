class Node:
    """Узел бинарного дерева поиска"""
    def __init__(self, data: int):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    """Бинарное дерево поиска с ограничением глубины только для дубликатов"""
    def __init__(self, max_level: int = 5):
        self.root: Node | None = None
        self.max_level = max_level

    def create_tree(self, data: int) -> bool:
        """Добавление элемента.
           - Уникальные значения можно добавлять на любую глубину.
           - Дубликаты — только пока глубина не превышает max_level.
        """

        if self.root is None:
            self.root = Node(data)
            print(f"Элемент {data} добавлен как корень дерева.")
            return True

        current = self.root
        level = 0

        while True:
            # === Дубликат — действуем с ограничением глубины ===
            if data == current.data:
                if level >= self.max_level:
                    print(f"Дубликат {data} НЕ добавлен — превышена глубина {self.max_level}.")
                    return False

                # Добавляем дубликаты вправо (как в твоём варианте)
                if current.right is None:
                    current.right = Node(data)
                    return True

                current = current.right
                level += 1
                continue

            # === Уникальное значение — БЕЗ ограничения глубины ===
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return True
                current = current.left

            else:
                if current.right is None:
                    current.right = Node(data)
                    return True
                current = current.right

            level += 1

    def count_occurrences(self, value: int) -> int:
        """Подсчет количества узлов с заданным значением"""

        def _count(node: Node | None) -> int:
            if node is None:
                return 0
            return (node.data == value) + _count(node.left) + _count(node.right)

        return _count(self.root)

    def print_tree(self):
        """Печать дерева повернутого на 90°"""

        def _print(node: Node | None, level: int):
            if node is None:
                return
            _print(node.right, level + 1)
            print(" " * (level * 4) + str(node.data))
            _print(node.left, level + 1)

        if self.root is None:
            print("Дерево пустое.")
            return

        _print(self.root, 0)

    def get_tree_depth(self) -> int:
        """Фактическая глубина дерева"""

        def _depth(node: Node | None) -> int:
            if node is None:
                return -1
            return max(_depth(node.left), _depth(node.right)) + 1

        return _depth(self.root)


def safe_input_int(prompt: str) -> int:
    """Безопасный ввод целого числа"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def main():
    bst = BinarySearchTree(max_level=5)

    print("-1 — окончание построения дерева\n")

    while True:
        data = safe_input_int("Введите число: ")

        if data == -1:
            print("\nПостроение дерева окончено.\n")
            break

        bst.create_tree(data)
        print(f"Текущая глубина дерева: {bst.get_tree_depth()}\n")

    print("Построенное дерево:")
    bst.print_tree()
    print(f"\nФактическая глубина дерева: {bst.get_tree_depth()}\n")

    value = safe_input_int("Введите число для подсчёта вхождений: ")
    count = bst.count_occurrences(value)
    print(f"Число вхождений элемента {value}: {count}")


if __name__ == "__main__":
    main()
