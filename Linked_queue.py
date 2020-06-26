# class Linked_queue:
#     def __init__(self):
#         self.queue = []
#         self.ifront = 0
#         self.iback = None
#         self.count = 0
#         self.next = self
#         self.head = self
#         self.tail = self
    
#     def push(self,val):
#         self.count += 1
#         self.queue.append(val)
#         if(self.iback == None):
#             self.iback = 0
#         else:
#             self.iback += 1
    
#     def pop(self):
#         try:
#             popVal = self.queue[self.ifront]
#             self.queue[self.ifront] = None
#             self.ifront += 1
#             self.count -= 1
#         except:
#             return None
#         return popVal
    
#     def size(self):
#         return self.count

# linked queue object based on project instructions
class Linked_queue:
    def __init__(self):
        self.ifront = 0
        self.iback = None
        self.linkedList = None
        self.size = 0

    # copy constructor and destructors don't exist in python
    
    # returns true if the queue is empty, or false if it is not
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    # returns the size of the queue
    def size(self):
        return self.size

    # returns the number of nodes in the linked list - not completed
    def list_size(self):
        pass

    # returns the first element in the queue list - not completed
    def front(self):
        pass

    # swaps all of the member variables with the list in the argument - not completed
    def swap(self, Linked_queue):
        pass

    # push the argument to the end of the queue and increment the size of the queue - not completed

    # Here is the process described from the instructions:
    # If the queue is empty, allocate memory for a new array with the required capacity, push the address of that array onto the linked list, set both indices to zero and place the new argument at that location. The size of the queue is now one.
    # If the back index already points to the last entry of the array, reset it to zero, allocate memory for a new array with the required capacity, push the address of that array onto the linked list, and insert the argument into the first location. 
    # Otherwise, increment the back index and place the argument at that location.
    def push(self, element):
        pass

    # pops the front of the queue and decrements the size of the queue - not completed

    # Here is the process described from the instructions:
    # Pop the front of the queue and increment the ifront index. 
    # If the front index equals the list capacity (8), reset it to zero and pop the front of the linked list while deallocating the memory allocated to that array. 
    # If the queue is emptied, also pop the front of the linked list while deallocated the memory allocated to that array. This member function may throw a underflow exception. 
    def pop(self):
        pass

# this is class for the nodes of the linked list, it hold the lists the hold the elements of the queue
class List_Nodes:
    def __init__(self):
        self.list = []
        self.listSize = 0
        self.next = None
