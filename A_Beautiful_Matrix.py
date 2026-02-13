matrix=[[0]*5 for _ in range(5)]
for r in range(5):
    matrix[r]=list(map(int, input().split()))

index_row=2
index_col=2

for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            index_row=i
            index_col=j


print(abs(index_row-2)+abs(index_col-2))
