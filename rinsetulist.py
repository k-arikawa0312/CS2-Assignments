graph2=[
    [1,2,3],
    [0],
    [5],
    [4],
    [1,3],
    [4]
]

def adjacent_list(lst,i,j):
    return j in lst[i]

print(adjacent_list(graph2,0,2))