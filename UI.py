from Linked_queue import Linked_queue

queue = Linked_queue()

def printTitle():
    print('\t\tWelcome To The Queue',end = '\n\n')

def printCommands():
    print("Commands:")
    print("\t\tEnter 'a' to add an item to the queue.")
    print("\t\tEnter 'p' to print the item in the front of the queue.")
    print("\t\tEnter 'd' to pop the front item from the queue.")
    print("\t\tEnter 's' to print the size of the queue.")
    print("\t\tEnter 'e' to exit the queue")

def processCommand(command):
    global queue
    if(command == 'a'):
        addItem()
    else:
        pass


def addItem():
    global queue
    add_value = input("Enter an item to be added to the queue: ")
    if(add_value.strip() != ''):
        queue.push(add_value)
        print(add_value,"has been added to the queue!")
    else:
        print("ERROR: No item in input!")

def printFirstItem():
    global queue
    if(queue.size() > 0):
        first = queue.front()
        print("The item in the front of the queue is",first)
    else:
        print("ERROR: The queue is empty!")

def deleteFirst():
    global queue
    if(queue.size > 0):
        delete = queue.pop()
        print(delete,"has been deleted from the queue!")
    else:
        print("ERROR: The queue is empty!")


def printSize():
    global queue
    print("There are",queue.size(),"items in the queue")