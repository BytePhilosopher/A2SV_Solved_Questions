n=int(input())
levels=list(map(int,input().split()))



count = [0] * (n + 1)
for num in levels:
    count[num] += 1

for index, value in enumerate(count):
    if value==0 and index!=0:
        print(index)
        break
