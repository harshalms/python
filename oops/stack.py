class Stack:
    def __init__(self, size=10):
        self.array = [None]*size
        self.top = -1
        self.size = size

    def __str__(self):
        return str((self.array, self.top, self.size))

    def push(self, val):
        if self.top==self.size-1:
            return "Stack is full!"
        self.top+=1
        self.array[self.top] = val

    def pop(self):
        if self.top == -1:
            print("Stack is empty...")
            return None
        self.top-=1
    
    def getElement(self):
        return self.array[:self.top+1]

s = Stack()
# print(s)
# s1 = Stack(5)
# print(s1)
s.push(3)
s.push(5)
s.push(8)
print(s.getElement())
s.pop()
print(s.getElement())
s.pop()
print(s.getElement())
s.pop()
print(s.getElement())
s.pop()
print(s.getElement())
s.pop()
print(s.getElement())

