
n=int(input())
s=input()
totalL=s.count("L")
totalO=s.count("O")

preL=0
preO=0

for k in range(1,n):
    if s[k-1]=="L":
        preL+=1
    else:
        preO+=1
    Fl=totalL-preL
    Fo=totalO-preO

    if preL!=Fl and preO!=Fo:
        print(k)
        exit(0)

print(-1)
