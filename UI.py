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
        add_value = input("Enter an item to be added to the queue: ")
        if(add_value.strip() != ''):
            queue.push(add_value)
            print("")
        else:
