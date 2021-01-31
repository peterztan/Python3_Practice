from LinearDS.Node import Node
from LinearDS.Stack import Stack

# Node test code below
test_node = Node("This is a new node.")
print(test_node.value)

# Stack test code below
dish_stack = Stack(10)
dishes_list = ["plate", "cup", "bowl"]
for each in dishes_list:
    dish_stack.push(each)
    print(dish_stack.top_item.value)