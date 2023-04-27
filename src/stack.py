class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """

        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack = []
        self.top = None


    def __str__(self):
        return f'В стэке {len(self.stack)} элементов. Последний элемент {self.top.data}.'


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.stack) == 0:
            self.top = Node(data, None)
            return self.stack.append(self.top)

        self.top = Node(data, self.stack[-1])
        return self.stack.append(self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        deleted_item = self.stack.pop()

        if len(self.stack) == 0:
            self.top = None
            return deleted_item.data

        self.top = self.stack[-1]
        return deleted_item.data
