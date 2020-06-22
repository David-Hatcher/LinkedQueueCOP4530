class Linked_queue:
    def __init__(self):
        self.queue = []
        self.ifront = 0
        self.iback = None
        self.count = 0
        self.next = self
        self.head = self
        self.tail = self
    
    def push(self,val):
        self.count += 1
        self.queue.append(val)
        if(self.iback == None):
            self.iback = 0
        else:
            self.iback += 1
    
    def pop(self):
        try:
            popVal = self.queue[self.ifront]
            self.queue[self.ifront] = None
            self.ifront += 1
            self.count -= 1
        except:
            return None
        return popVal
    
    def size(self):
        return self.count
