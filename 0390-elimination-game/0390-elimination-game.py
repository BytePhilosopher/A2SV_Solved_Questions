class Solution:
    def lastRemaining(self, n: int) -> int:
        head=1
        rem=n
        step=1

        l=True
        while rem>1:
            if rem%2==1 or l:
                head+=step

            rem//=2
            step*=2
            l=not l

        return head