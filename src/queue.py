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
        self.queue = []
        self.head = None
        self.tail = None


    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if len(self.queue) == 0:
            return ''
        ret = []
        for i in self.queue:
            ret.append(i.data)
        return '\n'.join(ret)


    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """

        if len(self.queue) == 0:
            self.head = self.tail = Node(data, None)
            self.queue.append(self.head)
        else:
            self.tail = Node(data, None)
            self.queue[-1].next_node = self.tail
            self.queue.append(self.tail)



    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass
