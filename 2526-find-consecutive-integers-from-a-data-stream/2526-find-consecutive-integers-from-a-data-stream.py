class DataStream:

    def __init__(self, value: int, k: int):
        self.ans=0
        self.value=value
        self.k=k
        

    def consec(self, num: int) -> bool:
        
        if num==self.value:
            self.ans+=1
        elif self.ans>0 and num!=self.value:
            self.ans-=1

        if self.ans==self.k:
            self.ans-=1
            return True

        return False
        # self.stream.append(num)
        # l=0

        # if num!=self.value:
        #     return False
     

        # while len(self.stream)>=self.k and l<self.k:
        #     if self.stream:
        #        n= self.stream[len(self.stream)-1-l]
        #        if n!=self.value: return False
        #     l+=1
            

        # return  False if len(self.stream)<self.k else True
        # #count<k -- false
        # #k intigers are eqaul to value


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)