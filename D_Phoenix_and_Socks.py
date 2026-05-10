
t = int(input())


for _ in range(t):
    n,l_count ,r_count = map(int, input().split())
    socks = list(map(int, input().split()))
    left_socks = socks[:l_count]
    right_socks = socks[l_count:]
    
    # Count frequency of colors on both sides
    left_freq = {}
    for c in left_socks:
        left_freq[c] = left_freq.get(c, 0) + 1
        
    right_freq = {}
    for c in right_socks:
        right_freq[c] = right_freq.get(c, 0) + 1
        
    # Remove already matched pairs
    for color in left_freq:
        if color in right_freq:
            match = min(left_freq[color], right_freq[color])
            left_freq[color] -= match
            right_freq[color] -= match
    
    # Recalculate remaining totals
    l_rem = sum(left_freq.values())
    r_rem = sum(right_freq.values())
    
    # Ensure we always treat the side with more socks as the 'majority'
    if l_rem >= r_rem:
        majority_freq = left_freq
        maj_total = l_rem
        min_total = r_rem
    else:
        majority_freq = right_freq
        maj_total = r_rem
        min_total = l_rem
        
    # We need to move 'diff' socks from majority to minority
    diff = (maj_total - min_total) // 2
    
    # Find how many pairs exist within the majority side
    pairs_available = 0
    for count in majority_freq.values():
        pairs_available += count // 2
        
    # Optimal cost formula
    # Cost = (Moves to balance) + (Cost to match remaining after balancing)
    cost = maj_total - min(diff, pairs_available)

    print(cost)
