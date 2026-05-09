r1,c1,r2,c2=map(int, input().split())

rook=1 if r1==r2 or c1==c2 else 2

if (c1+c2)%2 !=(r1+r2)%2:
    bishop=0
elif abs(r1-r2)==abs(c1-c2):
    bishop=1
else:
    bishop=2

king=max(abs(r1-r2),abs(c1-c2))

print(rook, bishop, king)