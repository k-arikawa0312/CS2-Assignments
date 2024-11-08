def one(n):
    if n>0:
     return one(n-1)+1
    else:
     return 0
    
def power(x,n):
    if n>0:
     return power(x,n-1)*x
    else:
     return 1
    
def comb(n,k):
    if k==0 or k==n:
     return 1
    else:
     return comb(n-1,k-1)+comb(n-1,k)

def hanoi(n,a,b,c):
    if n==1:
      print("move",a,"to",c)
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)

hanoi(4,1,2,3)

print(one(0))
print(power(0,1))
print(comb(5,2))

