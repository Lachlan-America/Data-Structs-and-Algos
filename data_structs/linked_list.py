from abc import ABC, abstractmethod

# A simple node class for a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    
    def __init__(self):
        self.head = Node(None)  # Dummy head node
        self.length = 0
    
    def append(self, data):
        if self.head.data is None:
            self.head.data = data
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def remove(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    # Attach the previous node to the next node
                    prev.next = current.next
                else:
                    # If the node to be removed is the head node
                    self.head = current.next
                self.length -= 1
                return True
            # Always the Node behind
            prev = current
            current = current.next
        return False
        
    