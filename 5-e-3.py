from collections import deque

class Visitor:
    def __init__(self,name,lst):
        self.name=name
        self.attr=deque(lst)

a=Visitor("A",[0,1,2])
b=Visitor("B",[0,1,2])
c=Visitor("C",[0,1,2])

print(a.name,"さんのアトラクション訪問順序",a.attr)
print(b.name,"さんのアトラクション訪問順序",b.attr)
print(c.name,"さんのアトラクション訪問順序",c.attr)
print("")

attractions=[deque(),deque(),deque()]
next_pool=deque()
goal=deque()


num_of_visitors=3


next_pool.append(a)
next_pool.append(b)
next_pool.append(c)

def next_action(visitor):
    if len(visitor.attr)>0:    
        i=visitor.attr.popleft()
        print(visitor.name,"さんがアトラクション",i,"に並びました。")
        attractions[i].append(visitor)
    else:
        print(visitor.name,"さんがアトラクションを回り終えました。")
        goal.append(visitor)


for t in range(100):
    print("t=",t)

    for i in range(len(attractions)):
        if len(attractions[i])>0:
            v=attractions[i].popleft()
            next_pool.append(v)

    while len(next_pool)>0:
        v=next_pool.popleft()
        next_action(v)

    print("")
    if len(goal) >= num_of_visitors:
        print("終了時間",t)
        break

              