class MyQueue:
    def placeOldestOnTopOfStackB(self):
        if self.B == []: # B is empty                
            while self.A:
                self.B.append(self.A.pop(-1))      


    def __init__(self):
        self.A, self.B = [], [] # A and B are stacks; 
                                    # the order in A: top of the stack is the newest element (of A and of the queue as a whole)
                                    # the order in B: top of the stack is the oldest element (of B and of the queue as a whole)
                                    # the newest (top) element in stack B is older than the oldest (bottom) element in stack A

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        self.placeOldestOnTopOfStackB()
        return self.B.pop(-1)  
        
    def peek(self) -> int:
        self.placeOldestOnTopOfStackB()
        return self.B[-1]        

    def empty(self) -> bool:
        return len(self.A) + len(self.B) == 0
