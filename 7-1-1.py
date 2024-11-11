def h(x):
    return hash(x)%10

def add(table,x):
    hash_value=h(x)
    if table[hash_value] == None:
        table[hash_value]=x
        

hash_table1=[None]*10
hash_table2=[None]*10


add(hash_table1,13)
add(hash_table1,14)
add(hash_table1,21)
add(hash_table1,46)
add(hash_table1,66)
add(hash_table1,67)
add(hash_table1,72)
add(hash_table1,77)
add(hash_table1,94)
add(hash_table1,95)


add(hash_table2,'Akabane')1
add(hash_table2,'Jujo')1
add(hash_table2,'Itabashi')1
add(hash_table2,'Ikebukuro')1
add(hash_table2,'Shinjuku')
add(hash_table2,'Shibuya')
add(hash_table2,'Ebisu')1
add(hash_table2,'Osaki')1

print(hash_table1)
print(hash_table2)