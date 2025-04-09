from abc import ABC, abstractmethod
from collections import deque

# Define the abstract class for Queue
class Queue(ABC):
    
    @abstractmethod
    def enqueue(self, item):
        """ 
        Adds an item to the end of the queue.

        Args:
            item (object): The item to be added to the queue.
        """
        pass
    
    @abstractmethod
    def dequeue(self):
        """ 
        Removes and returns the item from the front of the queue.

        Args:
            item (object): The item to be added to the queue.
        """
        pass
    
    @abstractmethod
    def is_empty(self):
        """ Returns True if the queue is empty, False otherwise. """
        pass

    @abstractmethod
    def size(self):
        """ Returns the number of items in the queue. """
        pass

# Concrete implementation of a Queue using a list
class ListQueue(Queue):
    
    def __init__(self):
        # Initialize an empty list to store the queue elements
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Concrete implementation of a Queue using a deque
class DequeQueue(Queue):
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)