import math

# linked queue object based on project instructions
class Linked_queue:
    def __init__(self):
        self.ifront = 0  # the position of the first element in the queue
        self.iback = None  # the position of the last element in the queue
        self.linkedList = None  # the head node of the linked list
        # the queue size (the number of elements in the queue, not the number of linked list nodes)
        self.size = 0

    # Destructor deletes all the elements in the Linked Queue then deletes Linked Queue object
    def __del__(self):
        
        current = self.linkedList
        while current != None:
            for element in current.list:
                del element
            current = current.next
        del self

    # Copy constructor will copy all data from LLQ to another
    # Usage: copyQueue = Linked_queue.copy()
    def copy(self):

        current = self.linkedList
        temp = Linked_queue()

        if current.next != None:
            for element in current.list:
                temp.push(element)
            current = current.next

        while current != None:
            for element in current.list:
                if element != None:     
                    temp.push(element)
            current = current.next
        return temp

    # Returns True if the queue is empty, or False if it is not
    #############     TESTING COMMENTS    ##################
    # Tested on 7/4/2020 working properly. - D Hatcher     #
    ########################################################
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

    # returns the size of the queue

    #############     TESTING COMMENTS    ##################
    # Testing Notes: I had to change the name of this function in order to be able to call it as
    # Python does not like having a function and member variable with the same names
    # Tested on 7/4/2020, working properly. - D Hatcher
    def getSize(self):
        return self.size

    # returns the number of nodes in the linked list - updated to be O(1)

    #############     TESTING COMMENTS    ##################
    # Tesed on 7/4/2020, working properly after a few changes
    # changed tempNode = self.linkedList.next -> tempNode = self.linkedList
    # added tempNode = tempNode.next during the while loop
    def list_size(self):
        if self.linkedList == None:
            return 0
        else:
            return math.ceil((self.ifront+self.size)/8)

    # returns the first element in the queue list

    #############     TESTING COMMENTS    ##################
    # Tested on 7/4/2020, working properly. D Hatcher
    def front(self):
        return self.linkedList.list[self.ifront]

    # Swaps all of the member variables with the list in the argument
    def swap(self, other):

        current = self.linkedList
        temp = Linked_queue()

        if current.next != None:
            for element in current.list:
                temp.push(element)
                self.pop()
                
            current = current.next

        while current != None:
            for element in current.list:
                if element != None:     
                    temp.push(element)
                    self.pop()
                    
            current = current.next


        current = other.linkedList

        if current.next != None:
            for element in current.list:
                self.push(element)
                other.pop()
            current = current.next

        while current != None:
            for element in current.list:
                if element != None:     
                    self.push(element)
                    other.pop()
            current = current.next

        current = temp.linkedList

        if current.next != None:
            for element in current.list:
                other.push(element)
                temp.pop()
            current = current.next

        while current != None:
            for element in current.list:
                if element != None:     
                    other.push(element)
                    temp.pop()
            current = current.next
        
        return


    # push the argument to the end of the queue and increment the size of the queue
    #############     TESTING COMMENTS    ##################
    # Tested on 7/4/2020 seems to be working properly, but not entirely sure as I am unable to
    # pop anything. -D Hatcher

    # Here is the process described from the instructions:
    # If the queue is empty, allocate memory for a new array with the required capacity, push the address of that array onto the linked list, set both indices to zero and place the new argument at that location. The size of the queue is now one.
    # If the back index already points to the last entry of the array, reset it to zero, allocate memory for a new array with the required capacity, push the address of that array onto the linked list, and insert the argument into the first location.
    # Otherwise, increment the back index and place the argument at that location.
    def push(self, element):
        if self.size == 0:  # if the list is empty
            self.linkedList = List_Node()  # create a new list node
            # place the element in the first position of the node's list
            self.linkedList.list[0] = element
            self.iback = 0  # set the position of the last element in the queue
            self.size += 1  # increments the size of the queue

        elif self.size > 0 and self.iback < 7:  # if the queue is not empty but not at the end of a node's list
            # a copy of the linked list's head to iterate through to find the end
            currentNode = self.linkedList

            while currentNode.next != None:  # iterating through the linked list to find the last node
                currentNode = currentNode.next

            # the element is added to the last index of the last node's list
            currentNode.list[self.iback+1] = element
            self.iback += 1  # increments the position of the last element in the queue
            self.size += 1  # increments the size of the queue

        elif self.iback == 7:  # if the queue is at the end of a node's list
            # a copy of the linked list's head to iterate through to find the end
            currentNode = self.linkedList

            while currentNode.next != None:  # iterating through the linked list to find the last node
                currentNode = currentNode.next

            currentNode.next = List_Node()  # adding a new node to the end of the list
            # the current node is set to the new node so that the element can be added to the node's list
            currentNode = currentNode.next
            # the element is placed in the node's list
            currentNode.list[0] = element

            self.iback = 0  # set the position of the last element in the queue
            self.size += 1  # increments the size of the queue

    # pops the front of the queue and decrements the size of the queue - not tested

    # Here is the process described from the instructions:
    # Pop the front of the queue and increment the ifront index.
    # If the front index equals the list capacity (8), reset it to zero and pop the front of the linked list while deallocating the memory allocated to that array.
    # If the queue is emptied, also pop the front of the linked list while deallocated the memory allocated to that array. This member function may throw a underflow exception.

    def pop(self):
        if self.size == 0:  # if the list size is 0, throw an underflow exception
            raise Exception("underflow")
        else:  # else remove the item from the front of the list
            # save a copy of the element at the front of the list
            popped = self.linkedList.list[self.ifront]
            # replace the first element with None
            self.linkedList.list[self.ifront] = None
            self.ifront += 1  # increment ifront
            self.size -= 1  # decrement size

            if self.ifront == 8:  # if the node list is empty, remove it and replace the first node pointer with the next node
                self.linkedList = self.linkedList.next
                self.ifront = 0  # set ifront back to 0

            return popped

    # prints the list, for testing purposes TODO: delete before project submission
    def printList(self):
        if self.size == 0:
            print("list is empty")
        else:
            currentNode = self.linkedList
            while currentNode != None:
                for element in currentNode.list:
                    # if element != None:
                    print(element)
                currentNode = currentNode.next
                if currentNode != None:
                    print()


# this is class for the nodes of the linked list, it hold the lists the hold the elements of the queue
class List_Node:
    def __init__(self):
        # 8 element list where the empty indexes use the placeholder None
        self.list = [None, None, None, None, None, None, None, None]
        self.next = None


# just some simple testing for the push function and front function
#############     TESTING COMMENTS    ##################
# Commented to start working on testing current implementations 7/4/2020 D.Hatcher
# myQueue = Linked_queue()

