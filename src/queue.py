class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node



class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None


    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''
        current = self.head
        list_objects = []
        # в цикле добавляем в список данные из каждой ноды
        while current.next_node:
            list_objects.append(current.data)
            current = current.next_node

        list_objects.append(current.data) #отдельно добавляем в список данные из последней ноды, так как в цикле последняя нода проигнорируется
        return '\n'.join(list_objects)


    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if not self.head:
            self.head = Node(data, None)
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data, None)
        self.tail = current.next_node



    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass
