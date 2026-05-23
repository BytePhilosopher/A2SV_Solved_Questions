class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        minheap=[y for x in matrix for y in x]
        heapq.heapify(minheap)
        for _ in range(k-1):
            heapq.heappop(minheap)
        return heapq.heappop(minheap)