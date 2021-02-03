class Node:
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_value(self, new_value):
        self.value = new_value

    def set_next_node(self, new_node):
        self.next_node = new_node

    def set_previous_node(self, new_node):
        self.previous_node = new_node
