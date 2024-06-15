# https://leetcode.cn/problems/design-front-middle-back-queue/

from collections import deque 

class FrontMiddleBackQueue:

    def __init__(self):
        self.A = deque()
        self.B = deque()


    def pushFront(self, val: int) -> None:
        m = len(self.A)
        n = len(self.B)
        if m==n:
            self.A.appendleft(val)
            self.B.appendleft(self.A.pop())
        elif m<n:
            self.A.appendleft(val)
        


    def pushMiddle(self, val: int) -> None:
        m = len(self.A)
        n = len(self.B)
        if m==n:
            self.B.appendleft(val)
        elif m<n:
            self.A.append(val)
            


    def pushBack(self, val: int) -> None:
        m = len(self.A)
        n = len(self.B)
        
        if m==n:
            self.B.append(val)
        elif m<n:
            self.B.append(val)
            self.A.append(self.B.popleft())


    def popFront(self) -> int:
        m = len(self.A)
        n = len(self.B)
        if m==n:
            return self.A.popleft() if m!=0 else -1
        elif m<n:
            self.A.append(self.B.popleft())
            return self.A.popleft()
            
        

    def popMiddle(self) -> int:
        m = len(self.A)
        n = len(self.B)
        if m==n:
            if m==0:return -1
            return self.A.pop() if m!=0 else -1
        elif m<n:
            return self.B.popleft()
        


    def popBack(self) -> int:
        m = len(self.A)
        n = len(self.B)
        if m==n:
            if m==0:return -1
            self.B.appendleft(self.A.pop())
            return self.B.pop() if n!=0 else -1
        elif m<n:
            return self.B.pop() 



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()