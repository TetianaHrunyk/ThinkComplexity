class CirularBuffer:
    
    def __init__(self, size = 10, position = 0):
        self.items = [False for i in range(size)]
        self.size = size
        self.start = position
        self.end = position
        
    def add(self, value):
        
        try:
            self.items[self.end] = value
        except IndexError:
            self.end = 0
            self.items[self.end] = value
            
        self.end += 1
        
        if self.end == self.start:
            self.start += 1
            
    def pop(self):
        if len(self.items) == 0:
            print("There are no items in the buffer")
            return
        
        self.items[self.start] == False
        self.start += 1
        
    def show(self):
        for item in self.items:
            print(item, end = ' ')
        print()
            
        