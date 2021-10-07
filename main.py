class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.dequeSize = 0

    def insert_front(self, new_data):
        new_node = Node(data=new_data)
        new_node.prev = None

        if self.front is None:
            new_node.next = None
            self.front = new_node
            self.rear = new_node
        else:
            self.front.prev = new_node
            new_node.next = self.front
            self.front = new_node
        self.dequeSize = self.dequeSize + 1

    def insert_rear(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = None

        if self.front is None:
            new_node.prev = None
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.dequeSize = self.dequeSize + 1

    def pop_front(self):
        prev_front = self.front.data
        if self.dequeSize == 0:
            raise Exception("Deque is Empty")
        else:
            self.front = self.front.next
            self.front.prev = None
        self.dequeSize -= 1
        return prev_front

    def pop_rear(self):
        prev_rear = self.rear.data
        if self.dequeSize == 0:
            raise Exception("Deque is Empty")
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.dequeSize -= 1
        return prev_rear

    def pick_front(self):
        if self.dequeSize == 0:
            raise Exception("Deque is Empty")
        else:
            return self.front.data

    def pick_rear(self):
        if self.dequeSize == 0:
            raise Exception("Deque is Empty")
        else:
            return self.rear.data

    def is_empty(self):
        if self.dequeSize == 0:
            return True
        else:
            return False

    def deque_length(self):
        return self.dequeSize
