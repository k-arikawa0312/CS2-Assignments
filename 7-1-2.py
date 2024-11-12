class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value 
        self.next = None

def make_hash_table(n):
    table = [None]*n
    return table

def h(x):   
    return hash(x)%10

def put(table,key,value):
    hash_value = h(key)
    node = table[hash_value]
    while node != None:
        if node.key == key:
            node.value = value
            return
        node = node.next
    
    first_node=table[hash_value]
    new_node = Node(key,value)
    new_node.next = first_node
    table[hash_value] = new_node

def get(table,key):
    hash_value = h(key)
    node = table[hash_value]
    while node != None:
        if node.key == key:
            return node.value
        node = node.next
    return None


def make_dict(n):
    result = [None]*n
    keys=random.sample(range(1000000),n)
    