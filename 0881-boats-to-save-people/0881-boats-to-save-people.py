class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
    #   [3,3,4,5]
        people.sort()
        left,right=0,len(people)-1
        ans=0

        while right>=left:
            if people[right]+ people[left]<=limit:
                left+=1
            ans+=1
            right-=1
  
        return ans