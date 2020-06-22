from Linked_queue import Linked_queue

newQueue = Linked_queue()
passedString = "Test Passed."
failedString = "Test Failed."

def testPushAndPop(push_val):
    queue = Linked_queue()
    queue.push(push_val)
    test_val = queue.pop()
    print("Test Push and Pop - Expected: ",push_val,"Recieved: ",test_val)
    if(test_val == push_val):
        print(passedString)
        return True
    else:
        print(failedString)
        return False

def testCount(itemsToPush):
    queue = Linked_queue()
    for item in itemsToPush:
        queue.push(item)
    queue_size = queue.size()
    list_size = len(itemsToPush)
    print("Test Count - Expected: ",list_size,"Recieved: ",queue_size)
    if(queue_size == list_size):
        print(passedString)
        return True
    else:
        print(failedString)
        return False

def testPop(length):
    queue = Linked_queue()
    for i in range(0,length):
        queue.push(0)
    for i in range(0,length):
        queue.pop()
    print("Test Pop to clear - Expected: 0 Recieved: ",queue.size())
    if (queue.size() == 0):
        print(passedString)
        return True
    else:
        print(failedString)
        return False

def testMultiPopandPush(itemsToPush):
    queue = Linked_queue()
    for item in itemsToPush:
        queue.push(item)
    poppedList = []
    testPassed = True
    while(queue.size() != 0):
        poppedList.append(queue.pop())
    for i in range(0,len(itemsToPush)):
        if(len(poppedList) != len(itemsToPush)):
            testPassed = False
            break
        if (itemsToPush[i] != poppedList[i]):
            testPassed = False
            break
    print("Test Multi Pop and Push - Expected: ",itemsToPush,"Recieved: ",poppedList)
    if(testPassed):
        print(passedString)
        return True
    else:
        print(failedString)
        return False
    
def testIBackValue(listOfItems):
    queue = Linked_queue()
    for item in listOfItems:
        queue.push(item)
    print("Expected: ",len(listOfItems) - 1,"Recieved: ",queue.iback)
    if(queue.iback == len(listOfItems) - 1):
        print(passedString)
        return True
    else:
        print(failedString)
        return False

    

def testSuite():
    testPushAndPop(1)
    testPushAndPop(13)
    testCount([1,2,3])
    testPop(3)
    testMultiPopandPush([1,2,3])
    testPop(3)
    testIBackValue([1,2,3])


testSuite()