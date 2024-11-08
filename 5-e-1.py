from collections import deque

cashier=deque()

n=10
m=6

for i in  range(n):
    customer="customer-id{}".format(i)
    print(customer,"さんがレジに並びました。")
    cashier.append(customer)

for i in range(m):
    if len(cashier)!=0:
     castomer=cashier.popleft()
     print(castomer,"さんが会計を済ませました。")

print("レジに並んでいる人数",len(cashier))