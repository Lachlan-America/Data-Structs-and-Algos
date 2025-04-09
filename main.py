from data_structs.queue import ListQueue

myQueue = ListQueue()
for i in range(5):
    myQueue.enqueue(i)

print(f"My first item: {myQueue.dequeue()}")
print(f"Queue size: {myQueue.size()}")
print(f"Queue empty?: {myQueue.is_empty()}")