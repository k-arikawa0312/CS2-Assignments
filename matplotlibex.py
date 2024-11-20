import matplotlib.pyplot as plt

xs = [0]
ys = [100000]
ys2 = [100000]

for x in range(1,51):
    y = ys[x-1] + ys2[0] * 0.02 
    y2 = ys2[x-1] * 1.02
    xs.append(x)
    ys.append(y)
    ys2.append(y2)

plt.plot(xs, ys, label='Simple interest')
plt.plot(xs, ys2, label='Compound interest')

plt.title('Simple and Compound Interest')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()

plt.show()