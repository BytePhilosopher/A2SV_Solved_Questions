class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans={}
        for cp in cpdomains:
            visit=cp.split(" ")
            if visit[1] in ans:
                ans[visit[1]]=int(ans.get(visit[1],0))+ int(visit[0])
            else:
                ans[visit[1]]=(visit[0])

            domain=visit[1].split(".")
            if len(domain)==3:
                newdom=domain[1]+"."+domain[2]
                ans[newdom]=int(ans.get(newdom,0))+int(visit[0])
                nnewdom=domain[2]
                ans[nnewdom]=int(ans.get(nnewdom,0))+int(visit[0])
            elif len(domain)==2:
                nnewdom=domain[1]
                ans[nnewdom]=int(ans.get(nnewdom,0))+int(visit[0])
            
        return [str(val) + " " + key for key,val in ans.items()]
            

        