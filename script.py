from linear_ds.queue import Queue
from linear_ds.node import Node
from linear_ds.stack import Stack
from linear_ds.queue import Queue

# Node test code below
test_node = Node("This is a new node.")
print(test_node.value)

# Stack test code below
dish_stack = Stack(10)
dishes_list = ["plate", "cup", "bowl"]
for each in dishes_list:
    dish_stack.push(each)
    print(dish_stack.top_item.value)

# Queue test code below
mazzios_order = Queue(5)
order_list = ["cheesesticks", "pepperoni pizza", "pepperoni calzones", "taco pizza", "supreme pizza"]
for each in order_list:
    mazzios_order.enqueue(each)
    print(f"Adding {each} to the dinner order!")
while mazzios_order.get_size() > 0:
    print(f"Delivering {mazzios_order.dequeue()} to the address.")