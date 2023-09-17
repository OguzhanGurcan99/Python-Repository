# Linked List
class ListNode:
    def __init__(self,data, nextNode):
        self.data = data
        self.nextNode = nextNode

front = ListNode( 1, ListNode( 2, None))
linkedList_1 = ListNode( 3, ListNode( 4, None))

print(front.data)
print(front.nextNode.data)

front.nextNode.nextNode = linkedList_1
# front is inserted with another linked list.

print(front.nextNode.nextNode.data)
print(front.nextNode.nextNode.nextNode.data)

print()
front.nextNode = linkedList_1
# ListNode( 2, None ) is removed.

print(front.data)
print(front.nextNode.data)
print(front.nextNode.nextNode.data)
print()

# Stack
class Stack:
    view = []

    def __init__(self):
        self.top = None
        self.length = 0

    def insert_element(self, number):
        self.top = number
        self.length += 1
        self.view.append(number)

    def remove_element(self):
        last_element = self.view[-1]
        self.view.remove(last_element)
        self.top = self.view[-1]
        self.length += -1

stack = Stack()
stack.insert_element(4)
stack.insert_element(7)
stack.insert_element(10)
print(stack.view)

stack.remove_element()
stack.remove_element()
stack.insert_element(20)
print(stack.view)
print()

# Queue
class Queue:
    view = []

    def __init__(self):
        self.top = None
        self.length = 0

    def insert_element(self, number):
        self.top = number
        self.length += 1
        self.view.append(number)

    def remove_element(self):
        first_element = self.view[0]
        self.view.remove(first_element)
        self.length += -1

queue = Queue()
queue.insert_element(5)
queue.insert_element(10)
queue.insert_element(15)
print(queue.view)

queue.remove_element()
queue.remove_element()
print(queue.view)

queue.insert_element(20)
print(queue.view)

