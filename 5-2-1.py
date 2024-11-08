

def cal(text):
    result=[]
    value=[]
    all=0
    for i in text:
        if i not in result:
            result.append(i)
            value.append(1)
        else:
            value[result.index(i)]+=1
    for n in value:
        all+=n
        i=0
    for n in value:
        print(n/all)
        
    return [value,result]

percent=cal("SUMOMOMO_MOMO_MOMOMO_MOMO")[0]
letters=cal("SUMOMOMO_MOMO_MOMOMO_MOMO")[1]
class Node:
    def __init__(self,value,left=None,right=None) :
        self.value=value
        self.left=left
        self.right=right
    
    def __str__(self) -> str:
        return self.value
    