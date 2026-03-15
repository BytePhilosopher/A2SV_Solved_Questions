import sys
input=sys.stdin.readline

h,w=map(int,input().split())

grid=[[0]*w for _ in range(h)]

for i in range(h):
    row=input().strip()
    for j in range(w):
        grid[i][j]=1 if row[j]=="." else 0



hor=[[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w-1):
        if grid[i][j] and grid[i][j+1]:
            hor[i][j]=1



ver=[[0]*w for _ in range(h)]

for i in range(h-1):
    for j in range(w):
        if grid[i][j] and grid[i+1][j]:
            ver[i][j]=1



ph=[[0]*(w+1) for _ in range(h+1)]
pv=[[0]*(w+1) for _ in range(h+1)]

for i in range(h):
    for j in range(w):
        ph[i+1][j+1]=hor[i][j]+ph[i][j+1]+ph[i+1][j]-ph[i][j]
        pv[i+1][j+1]=ver[i][j]+pv[i][j+1]+pv[i+1][j]-pv[i][j]


q=int(input())

for _ in range(q):

    r1,c1,r2,c2=map(int,input().split())

    r1-=1
    c1-=1
    r2-=1
    c2-=1



    horizontal = ph[r2+1][c2] - ph[r1][c2] - ph[r2+1][c1] + ph[r1][c1]

    # vertical dominoes
    vertical = pv[r2][c2+1] - pv[r1][c2+1] - pv[r2][c1] + pv[r1][c1]

    print(horizontal+vertical)