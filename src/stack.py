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
        self.top = None

    def __str__(self):
        if not self.top:
            return 'Stack is empty'
        data_list = []
        current_status = self.top
        while current_status.next_node:
            data_list.append(current_status.data)
            current_status = current_status.next_node
        data_list.append(current_status.data)
        return '\n'.join(data_list)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        if not self.top:
            self.top = Node(data, None)
            return

        current_status = self.top
        self.top = Node(data, current_status)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения
        :return: данные удаленного элемента
        """
        current_status = self.top
        self.top = current_status.next_node
        return current_status.data
