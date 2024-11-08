from collections import deque

result=deque()
n=1

while len(result)<10:
    if n%5==0:
        result.pop()
    elif n%3==0:
        result.popleft()
    elif n%2==0:
        result.append(n)
    else:
        result.appendleft(n)
    n+=1

print(result)