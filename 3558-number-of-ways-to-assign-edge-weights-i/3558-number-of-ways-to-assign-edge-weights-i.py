from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build the adjacency list for the tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: Use BFS to find the maximum depth (length of the longest path)
        # We start at node 1 with an initial path length (depth) of 0 edges.
        max_depth = 0
        queue = deque([(1, 0)]) # (node, current_edge_count)
        visited = {1}
        
        while queue:
            curr_node, current_depth = queue.popleft()
            max_depth = max(max_depth, current_depth)
            
            for neighbor in adj[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_depth + 1))
                    
        # Step 3: Calculate 2^(L-1) % MOD
        # Note: If max_depth is 0 (just a root node, though constraints say n >= 2), 
        # it would mean 0 edges. For n >= 2, max_depth will always be >= 1.
        return pow(2, max_depth - 1, MOD)