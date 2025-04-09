### **1. Basic Data Structures:**

* [ ] **Arrays/Lists** :

  * [ ] Implement dynamic arrays (resize when full).
  * [ ] Implement basic operations like insert, delete, search, and traverse.
  * [ ] Consider edge cases (e.g., insertion at the beginning, middle, or end).
* [ ] **Linked Lists** :

  * [ ] Singly Linked List: Create nodes, add operations (insert, delete, traverse), reverse the list.
  * [ ] Doubly Linked List: Add backward traversal, insert at both ends, remove specific nodes.
  * [ ] Circular Linked List: Handle circular traversal.
* [ ] **Stacks** :

  * [ ] Implement stack using arrays or linked lists.
  * [ ] Handle basic operations: push, pop, peek, and check if empty.
  * [ ] Implement operations to check for balanced parentheses or expressions.
* [ ] **Queues** :

  * [ ] Implement queue using arrays or linked lists.
  * [ ] Handle basic operations: enqueue, dequeue, peek, and check if empty.
  * [ ] Implement a  **circular queue** .
* [ ] **Deques** :

  * [ ] Implement a deque (double-ended queue) using arrays or linked lists.
  * [ ] Operations: add front, add back, remove front, remove back.
* [ ] **Hash Tables (Hash Maps)** :

  * [ ] Implement hash table with basic operations: insert, search, and delete.
  * [ ] Handle collisions using separate chaining (linked list) or open addressing (linear probing, quadratic probing).

  from abc import ABC, abstractmethod

  # Define the abstract class for Queue

  class Queue(ABC):

      @abstractmethod
      def enqueue(self, item):
          pass

      @abstractmethod
      def dequeue(self):
          pass

      @abstractmethod
      def is_empty(self):
          pass

      @abstractmethod
      def size(self):
          pass

  # Concrete implementation of a Queue using a list

  class ListQueue(Queue):
      def __init__(self):
          self.queue = []

      def enqueue(self, item):
          self.queue.append(item)

      def dequeue(self):
          if not self.is_empty():
              return self.queue.pop(0)
          return None  # Or raise an exception if needed

      def is_empty(self):
          return len(self.queue) == 0

      def size(self):
          return len(self.queue)

  # Concrete implementation of a Queue using a deque

  from collections import deque

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
* [ ] **Heaps** :

  * [ ] Implement **min-heap** and  **max-heap** .
  * [ ] Operations: insert, delete, and heapify.
  * [ ] Use heaps for priority queues.
* [ ] **Trees** :

  * [ ] **Binary Tree** : Implement tree, traverse (pre-order, in-order, post-order), search for a node.
  * [ ] **Binary Search Tree (BST)** : Insert, delete, and search for a node.
  * [ ] **AVL Tree** : Implement self-balancing binary search tree.
  * [ ] **Red-Black Tree** : Implement self-balancing BST with specific properties.
  * [ ] **Heap Tree** : Min-heap and max-heap as trees.
* [ ] **Graphs** :

  * [ ] Implement a **graph** using adjacency list and adjacency matrix.
  * [ ] Implement graph traversal algorithms (BFS, DFS).
  * [ ] Implement **Dijkstra’s algorithm** for shortest path.
  * [ ] Implement  **A* algorithm* * for pathfinding.

### **2. Advanced Data Structures:**

* [ ] **Tries** :
  * [ ] Implement a Trie (prefix tree) for fast string matching.
  * [ ] Implement insert, search, and delete operations.
* [ ] **Segment Trees** :
  * [ ] Implement segment trees for range queries (sum, minimum, maximum).
* [ ] **Fenwick Tree (Binary Indexed Tree)** :
  * [ ] Implement BIT for efficient range sum queries and updates.
* [ ] **Disjoint Set Union (Union-Find)** :
  * [ ] Implement union by rank and path compression for efficient union-find operations.
* [ ] **B-Trees and B+ Trees** :
  * [ ] Implement B-Trees for multi-level indexing and B+ Trees (used in databases).

### **3. Sorting Algorithms:**

* [ ] **Bubble Sort, Selection Sort, Insertion Sort** (simple, but valuable for understanding basic sorting principles).
* [ ] **Merge Sort** and **Quick Sort** (divide and conquer).
* [ ] **Heap Sort** (using a heap data structure).
* [ ] **Radix Sort** and **Counting Sort** (non-comparative sorting).
* [ ] **Tim Sort** (hybrid sorting algorithm, efficient in practice).
* [ ] **Shell Sort** (generalized insertion sort with gaps).

### **4. Searching Algorithms:**

* [ ] **Linear Search** .
* [ ] **Binary Search** (both iterative and recursive).
* [ ] **Interpolation Search** (used for sorted data with uniform distribution).

### **5. Graph Algorithms:**

* [ ] **Breadth-First Search (BFS)** : Use a queue to explore all neighbors.
* [ ] **Depth-First Search (DFS)** : Use recursion or a stack for exploring all paths.
* [ ] **Topological Sort** : For Directed Acyclic Graphs (DAGs).
* [ ] **Dijkstra's Algorithm** : For shortest path in weighted graphs (non-negative weights).
* [ ] **Bellman-Ford Algorithm** : For shortest path, including negative weights.
* [ ] **Floyd-Warshall Algorithm** : For finding all pairs shortest path.
* [ ] **Kruskal's Algorithm** and  **Prim's Algorithm** : For Minimum Spanning Tree.
* [ ] **A* Algorithm* *: For efficient pathfinding.

### **6. Dynamic Programming (DP):**

* [ ] **Memoization** : Storing intermediate results to avoid redundant computations.
* [ ] **Bottom-Up DP** : Solving problems iteratively from smaller subproblems.
* [ ] Classic DP problems:
  * [ ] Fibonacci Sequence.
  * [ ] Longest Common Subsequence (LCS).
  * [ ] Coin Change Problem.
  * [ ] 0/1 Knapsack Problem.
  * [ ] Matrix Chain Multiplication.
  * [ ] Longest Increasing Subsequence.
  * [ ] Rod Cutting Problem.
  * [ ] Edit Distance (Levenshtein Distance).
  * [ ] Partition Problem (Subset Sum Problem).

### **7. Greedy Algorithms:**

* [ ] **Activity Selection Problem** : Select activities that don’t overlap.
* [ ] **Fractional Knapsack Problem** : Use greedy for solving fractional knapsack problem.
* [ ] **Huffman Coding** : Greedy approach for data compression.
* [ ] **Interval Scheduling** : Greedy algorithm to select the maximum number of non-overlapping intervals.

### **8. Backtracking Algorithms:**

* [ ] **N-Queens Problem** : Place N queens on an NxN chessboard such that no two queens attack each other.
* [ ] **Sudoku Solver** : Solve Sudoku puzzle using backtracking.
* [ ] **Subset Sum Problem** .
* [ ] **Permutations and Combinations** : Generate all possible permutations or combinations of a set.
* [ ] **Rat in a Maze Problem** : Find a path from the start to the end in a maze.

### **9. Bit Manipulation:**

* [ ] **Set and Clear bits** : Set, clear, and toggle individual bits in an integer.
* [ ] **Count set bits** : Count the number of 1s in the binary representation of a number.
* [ ] **Find the XOR of two numbers** : XOR-related problems.
* [ ] **Bit Masking** : For problems involving subsets and operations on sets.
* [ ] **Binary to Decimal and Decimal to Binary Conversion** .

### **10. Miscellaneous Algorithms:**

* [ ] **KMP Algorithm** : Efficient string matching algorithm.
* [ ] **Rabin-Karp Algorithm** : String matching using hashing.
* [ ] **Fisher-Yates Shuffle** : Efficient random shuffling algorithm.
* [ ] **Merge Intervals** : Merge overlapping intervals in a collection.

### **11. Advanced Topics (Optional):**

* [ ] **String Algorithms** :
  * [ ] **Z Algorithm** .
* [ ] **Trie-based String Matching** .
* [ ] **Network Flow** : Implement algorithms like **Ford-Fulkerson** for maximum flow problems.
* [ ] **Suffix Arrays** : Used for efficient substring matching.
* [ ] **Bloom Filters** : Probabilistic data structure used for set membership testing.
