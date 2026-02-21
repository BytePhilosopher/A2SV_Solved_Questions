
n = int(input())

towers = []
all_blocks = []

for _ in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    blocks = data[1:]
    towers.append(blocks)
    all_blocks.extend(blocks)


sorted_blocks = sorted(all_blocks)


position = {value: i for i, value in enumerate(sorted_blocks)}


segments = 0

for blocks in towers:

    mapped = [position[x] for x in blocks]
    
    
    segments += 1  
    
    for i in range(len(mapped) - 1):
        if mapped[i] + 1 != mapped[i + 1]:
            segments += 1


splits = segments - n
combines = segments - 1

print(splits,combines )