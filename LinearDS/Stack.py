from LinearDS.Node import Node

class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, new_value):
        if self.has_space():
            new_item = Node(new_value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
        else:
            print("The stack is full.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("There is nothing to see in this stack.")

    def pop(self):
        if not self.is_empty():
            removed_item = self.top_item
            self.top_item = removed_item.get_next_node()
            self.size -= 1
            return removed_item.get_value()
        else:
            print("There is nothing to pop in this stack.")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0