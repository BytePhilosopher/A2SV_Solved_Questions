class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=[0]
        for num in nums:
            self.add(num)
    def push(self,val):
        self.nums.append(val)
        i=len(self.nums)-1 

        while i>1 and self.nums[i//2]>self.nums[i]:
            self.nums[i//2],self.nums[i]=self.nums[i],self.nums[i//2]
            i=i//2
    def pop(self):
        if len(self.nums)==1:
            return
        if len(self.nums)==2:
            self.nums.pop()
            return

        self.nums[1]=self.nums.pop()
        i=1
        while (2*i)<len(self.nums):
            if  (2*i+1)<len(self.nums) and self.nums[2*i +1]< self.nums[2*i] and self.nums[i]>self.nums[2*i+1]:
                self.nums[2*i+1],self.nums[i]=self.nums[i], self.nums[2*i+1]
                i=2*i+1
            elif self.nums[i]>self.nums[2*i]:
                self.nums[2*i],self.nums[i]=self.nums[i], self.nums[2*i]
                i=2*i
            else:
                break

    def add(self, val: int) -> int:
        self.push(val)
        while len(self.nums)-1>self.k:
            self.pop()
        return self.nums[1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)