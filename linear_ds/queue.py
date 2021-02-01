from linear_ds.node import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def get_size(self):
        return self.size

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            return "There is nothing to see here."

    def enqueue(self, value):
        if self.has_space():
            item_to_enqueue = Node(value)
            if self.is_empty():
                self.head = item_to_enqueue
                self.tail = item_to_enqueue
            else:
                self.tail.set_next_node(item_to_enqueue)
                self.tail = item_to_enqueue
            self.size += 1
        else:
            return "The queue is full!"

    def dequeue(self):
        if self.get_size() > 0:
            item_to_dequeue = self.head
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_dequeue.get_value()
        else:
            return "The queue is empty!"

    def has_space(self):
        return self.max_size > self.size

    def is_empty(self):
        return self.size == 0
