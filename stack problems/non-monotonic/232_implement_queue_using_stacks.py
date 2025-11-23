class MyQueue:
    def __init__(self):
        self.inqueue = [] 
        self.outqueue =[]

    def push(self, x: int) -> None:
        self.inqueue.append(x)
        

    def pop(self) -> int:
        if self.outqueue:
            return self.outqueue.pop()
        while self.inqueue:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue.pop()
        

    def peek(self) -> int:
        if self.outqueue:
            return self.outqueue[-1]
        while self.inqueue:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue[-1]


    def empty(self) -> bool:
        return (len(self.inqueue) + len(self.outqueue)) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(5)
print(obj.pop())
print(obj.peek())
print(obj.empty())