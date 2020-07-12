from Linked_queue import Linked_queue
import random
import math
testPassedString = "\033[0;32m Test Passed \033[0;37m"
testFailedString = "\033[0;31m Test Failed \033[0;37m"


# Generates random numbers for creation of arrays to create random queues 
def randomNumber():
    return int(random.random() * 1000)

# Generates random characters for creation of arrays to create random queues
def randomCharacter():
    chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()_+[];':<>,.?"
    return chars[randomNumber() % len(chars)]

# Generations random strings for creation of arrays to create random queues
def randomString(length):
    string = ''
    for i in range(0,length):
        string += randomCharacter()
    return string

# Determines the outcome of a test
def testResults(testTitle,received,expected):
    print(testTitle)
    print("Expected: ",expected,"Received: ",received)
    if(received == expected):
        print(testPassedString)
        return True
    else:
        print(testFailedString)
        return False

def testResultsArrays(testTitle,received,expected):
    print(testTitle)
    print("Length of Expected: ",len(expected),"Length of Received: ",len(received))
    same = True
    if(len(received) == len(expected)):
        for i in range(0,len(expected)):
            if(received[i] != expected[i]):
                same = False
                break
    else:
        same = False
    if(same == True):
        print(testPassedString)
        return True
    else:
        print(testFailedString)
        return False

# Tests the front functionality of the Linked_queue class
def testFront(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    received = queue.front()
    expected = array[0]
    return testResults("Front Test",received,expected)

# Tests the size function of the Linked_queue class
def testSize(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    received = queue.getSize()
    expected = len(array)
    return testResults("Size Test: ",received,expected)

# Tests the empty function of the Linked_queue
def testEmpty(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    if(len(array) != 0):
        expected = False
    else:
        expected = True
    received = queue.empty()
    return testResults("Empty Test",received,expected)

# Tests the list_size function of the Linked_queue this must take a second variable for the
# expected number of nodes
def testListSize(array,expected):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    received = queue.list_size()
    return testResults("List Size",received,expected)

def testPop(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    testArray = []
    fail = False
    while(fail == False):
        try:
            testArray.append(queue.pop())
        except:
            fail = True
    return testResultsArrays("Pop Test",testArray,array)

def testPopEmpty(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    expected = False
    try:
        queue.pop()
        received = True
    except:
        received = False
    return testResults("Empty Pop Test",received,expected)

def testCopy(array):
    queueA = Linked_queue()
    for value in array:
        queueA.push(value)
    queue_copy = queueA.copy()
    testArray = []
    fail = False
    while(fail == False):
        try:
            testArray.append(queue_copy.pop())
        except:
            fail = True
    return testResultsArrays("Copy Test",testArray,array)
    
def testDecon(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    del queue
    expected = False
    try:
        print(queue)
        received = True
    except:
        received = False
    testResults("Deconstructor Test",received,expected)

def testPushAndPop(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    rand = random.randint(0,len(array)-1)
    expected = len(array) - rand
    for _ in range(0,rand):
        queue.pop()
    received = queue.getSize()
    testResults("Push and Pop test",received,expected)

def testPopAndPushOrdered():
    queue = Linked_queue()
    arr = []
    queue.push(1)
    queue.push(2)
    arr.append(queue.pop())
    queue.push(4)
    arr.append(queue.pop())
    arr.append(queue.pop())
    return testResultsArrays("Ordered Push and Pop Test",arr,[1,2,4])

#Ints [1,1000] size 5
testArray_A = [random.randint(1,1000) for _ in range(5)]

#Ints [1,1000] size 10000
testArray_B = [random.randint(1,1000) for _ in range(10000)]

#Unicode Characters range 15
testArray_C = [randomCharacter() for _ in range(15)]

#Unicode Characters range 10000
testArray_D = [randomCharacter() for _ in range(10000)]

#Unicode Strings range 15
testArray_E = [randomString(5) for _ in range(15)]

#Unicode Strings range 10000
testArray_F = [randomString(5) for _ in range(10000)]

#Empty array to be added
testArray_G = []

testFront(testArray_A)
testFront(testArray_B)
testFront(testArray_C)
testFront(testArray_D)
testFront(testArray_E)
testFront(testArray_F)
testSize(testArray_A)
testSize(testArray_B)
testSize(testArray_C)
testSize(testArray_D)
testSize(testArray_E)
testSize(testArray_F)
testSize(testArray_G)
testEmpty(testArray_F)
testEmpty(testArray_G)
testListSize(testArray_A,math.ceil(len(testArray_A)/8))
testListSize(testArray_C,math.ceil(len(testArray_C)/8))
testListSize(testArray_B,math.ceil(len(testArray_B)/8))
testPop(testArray_A)
testPop(testArray_B)
testPop(testArray_C)
testPopEmpty(testArray_G)
testDecon(testArray_A)
testDecon(testArray_B)
testDecon(testArray_C)
testDecon(testArray_G)
testPushAndPop(testArray_C)
testPushAndPop(testArray_B)
testPushAndPop(testArray_A)
testCopy(testArray_A)
testCopy(testArray_B)
testCopy(testArray_C)
testPopAndPushOrdered()