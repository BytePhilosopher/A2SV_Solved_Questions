from collections import deque
class RecentCounter:

    def __init__(self):
        self.req=deque()
        

    def ping(self, t: int) -> int:
        self.req.append(t)
        left=t-3000
        count=0
        while self.req and (left>self.req[0] or self.req[0]>t):
            self.req.popleft()
        return len(self.req)
        

                

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)