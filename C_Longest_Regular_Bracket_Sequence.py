s=input()
max_length = 0
current_length = 0
stack = [-1]
p=0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            current_length = i - stack[-1] 
            if current_length > max_length:
                max_length = current_length
                p=1
            elif current_length == max_length:
                p+=1
if max_length == 0:
    p=1
print(max_length,p)