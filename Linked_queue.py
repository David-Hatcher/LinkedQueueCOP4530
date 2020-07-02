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
        self.ifront = 0 # the position of the first element in the queue
        self.iback = None # the position of the last element in the queue
        self.linkedList = None # the head node of the linked list
        self.size = 0 # the queue size (the number of elements in the queue, not the number of linked list nodes)

    # copy constructor and destructors don't exist in python
    
    # returns true if the queue is empty, or false if it is not - not tested
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    # returns the size of the queue - not tested
    def size(self):
        return self.size

    # returns the number of nodes in the linked list - not tested
    def list_size(self):
        if self.linkedList == None:
            return 0
        else:
            tempNode = self.linkedList.next
            listCount = 1
            while tempNode.next != None:
                listCount += 1
            return listCount

    # returns the first element in the queue list - not tested
    def front(self):
        return self.linkedList.list[self.ifront]

    # swaps all of the member variables with the list in the argument - not completed
    def swap(self, Linked_queue):
        pass

    # push the argument to the end of the queue and increment the size of the queue - not tested

    # Here is the process described from the instructions:
    # If the queue is empty, allocate memory for a new array with the required capacity, push the address of that array onto the linked list, set both indices to zero and place the new argument at that location. The size of the queue is now one.
    # If the back index already points to the last entry of the array, reset it to zero, allocate memory for a new array with the required capacity, push the address of that array onto the linked list, and insert the argument into the first location. 
    # Otherwise, increment the back index and place the argument at that location.
    def push(self, element):
        if self.size == 0: # if the list is empty
            self.linkedList = List_Node() # create a new list node
            self.linkedList.list[0] = element # place the element in the first position of the node's list
            self.iback = 0 # set the position of the last element in the queue
            self.size += 1 # increments the size of the queue

        elif self.size > 0 and self.iback < 7: # if the queue is not empty but not at the end of a node's list
            currentNode = self.linkedList # a copy of the linked list's head to iterate through to find the end

            while currentNode.next != None: # iterating through the linked list to find the last node
                currentNode = currentNode.next
            
            currentNode.list[self.iback+1] = element # the element is added to the last index of the last node's list
            self.iback += 1 # increments the position of the last element in the queue
            self.size += 1 # increments the size of the queue

        elif self.iback == 7: # if the queue is at the end of a node's list
            currentNode = self.linkedList # a copy of the linked list's head to iterate through to find the end

            while currentNode.next != None: # iterating through the linked list to find the last node
                currentNode = currentNode.next

            currentNode.next = List_Node() # adding a new node to the end of the list
            currentNode = currentNode.next # the current node is set to the new node so that the element can be added to the node's list
            currentNode.list[0] = element # the element is placed in the node's list
            
            self.iback = 0 # set the position of the last element in the queue
            self.size += 1 # increments the size of the queue


    # pops the front of the queue and decrements the size of the queue - not completed

    # Here is the process described from the instructions:
    # Pop the front of the queue and increment the ifront index. 
    # If the front index equals the list capacity (8), reset it to zero and pop the front of the linked list while deallocating the memory allocated to that array. 
    # If the queue is emptied, also pop the front of the linked list while deallocated the memory allocated to that array. This member function may throw a underflow exception. 
    def pop(self):
        pass

    # prints the list, for testing purposes TODO: delete before project submission
    def printList(self):
        if self.size == 0:
            print("list is empty")
        else:
            currentNode = self.linkedList
            while currentNode != None:
                for element in currentNode.list:
                    if element != None:
                        print(element)
                currentNode = currentNode.next
                if currentNode != None:
                    print()
        


# this is class for the nodes of the linked list, it hold the lists the hold the elements of the queue
class List_Node:
    def __init__(self):
        self.list = [None, None, None, None, None, None, None, None] # 8 element list where the empty indexes use the placeholder None
        self.listSize = 0
        self.next = None

# just some simple testing for the push function and front function
myQueue = Linked_queue()

myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
myQueue.push(4)
myQueue.push(5)
myQueue.push(6)
myQueue.push(7)
myQueue.push(8)
myQueue.push(9)
myQueue.printList()
print(myQueue.front())