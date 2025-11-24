class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
            self.stack.append(value)
            if not self.min_stack or value <= self.min_stack[-1]:
                self.min_stack.append(value)

    def pop(self) -> None:
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
            return self.stack[-1]

        
    def getMin(self) -> int:
            return self.min_stack[-1]

            

if __name__ == "__main__":
    print("--- MinStack Implementation Test ---")
    
    # 1. Instantiate the object
    obj = MinStack()
    
    # List of operations and expected outputs for comparison
    operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    values = [[], [-2], [0], [-3], [], [], [], []]
    
    # The first element is the constructor call, so we skip it for the loop
    results = [None] # Start with 'null' for the constructor
    
    # 2. Execute the sequence of operations
    for op, val_list in zip(operations[1:], values[1:]):
        val = val_list[0] if val_list else None # Get the value, if one exists
        
        if op == "push":
            print(f"Calling push({val})")
            obj.push(val)
            results.append(None) # push returns nothing
            
        elif op == "pop":
            print("Calling pop()")
            obj.pop()
            results.append(None) # pop returns nothing
            
        elif op == "top":
            result = obj.top()
            print(f"Calling top() -> {result}")
            results.append(result)
            
        elif op == "getMin":
            result = obj.getMin()
            print(f"Calling getMin() -> {result}")
            results.append(result)
            
        else:
            print(f"Unknown operation: {op}")

    print("\n--- Final Results ---")
    print(f"Expected Output: [null, null, null, null, -3, null, 0, -2]")
    print(f"Actual Output:   {results}")