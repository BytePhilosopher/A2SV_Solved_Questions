class Solution:
    def grayCode(self, n: int) -> List[int]:

        result =[]
        seen = set()
        def backtrack(current):

            if current in seen:
                
                return
            result.append(current)
            seen.add(current)
            
            for i in range(n):
               current = current ^ (1 << i)
               
               backtrack(current)
            
               current = current ^ (1 <<i )
                  
               
        backtrack(0)
        # for i in range(n):
        #     print(i^(i>>n))
        return result

