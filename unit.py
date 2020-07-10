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
def testResults(testTitle,recieved,expected):
    print(testTitle)
    print("Expected: ",expected,"Recieved: ",recieved)
    if(recieved == expected):
        print(testPassedString)
        return True
    else:
        print(testFailedString)
        return False

def testResultsArrays(testTitle,recieved,expected):
    print(testTitle)
    print("Length of Expected: ",len(expected),"Length of Recieved: ",len(recieved))
    same = True
    if(len(recieved) == len(expected)):
        for i in range(0,len(recieved)):
            if(recieved[i] != expected[i]):
                same = False
                break
    else:
        same = False
    if(same):
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
    recieved = queue.front()
    expected = array[0]
    return testResults("Front Test",recieved,expected)

# Tests the size function of the Linked_queue class
def testSize(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    recieved = queue.getSize()
    expected = len(array)
    return testResults("Size Test: ",recieved,expected)

# Tests the empty function of the Linked_queue
def testEmpty(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    if(len(array) != 0):
        expected = False
    else:
        expected = True
    recieved = queue.empty()
    return testResults("Empty Test",recieved,expected)

# Tests the list_size function of the Linked_queue this must take a second variable for the
# expected number of nodes
def testListSize(array,expected):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    recieved = queue.list_size()
    return testResults("List Size",recieved,expected)

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
        recieved = True
    except:
        recieved = False
    return testResults("Empty Pop Test",recieved,expected)

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
        recieved = True
    except:
        recieved = False
    testResults("Deconstructor Test",recieved,expected)

def pushAndPop(array):
    queue = Linked_queue()
    for value in array:
        queue.push(value)
    rand = random.randint(0,len(array)-1)
    expected = len(array) - rand
    for _ in range(0,rand):
        queue.pop()
    recieved = queue.getSize()
    testResults("Push and Pop test",recieved,expected)

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
pushAndPop(testArray_C)
pushAndPop(testArray_B)
pushAndPop(testArray_A)
testCopy(testArray_A)
testCopy(testArray_B)
testCopy(testArray_C)