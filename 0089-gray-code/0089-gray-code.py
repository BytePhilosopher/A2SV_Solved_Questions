class Solution:
    def grayCode(self, n: int) -> List[int]:
        # total= 2**n

        # path=[0]
        # visited={0}

        # def onebit(a,b):
        #     x= a ^ b

        #     return x and (x & (x - 1)) == 0


        # def dfs():
        #     if len(path)== total:
        #         return onebit(path[0],path[-1])

        #     for num in range(total):
        #         if num not in visited and onebit(path[-1],num):
        #             visited.add(num)
        #             path.append(num)

        #             if dfs():
        #                 return True

        #             path.pop()
        #             visited.remove(num)

        #     return False
        
        # dfs()
        # return path
        
        return [i ^ (i>>1) for i in range(1<<n)]