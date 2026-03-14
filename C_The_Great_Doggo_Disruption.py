from collections import Counter
# 
input()
s=input().strip()

if len(s)==1:
    print("Yes")
    exit(0)

if len(set(s))<len(s):
    print("Yes")
else:
    print("No")
