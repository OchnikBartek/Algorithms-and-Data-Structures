import random


def AWCG(j, k, m, ran):
    c = 0
    Tab = []
    for i in range(k):
        Tab.append(int(random.randint(1, m-1)))
    for n in range(ran):
        rest = n % k
        x = (Tab[(k + rest - j) % k] + Tab[rest] + c) % m
        y = (Tab[(k + rest - j) % k] + Tab[rest] + c)
        if y < m:
            c = 0
        else:
            c = 1
        Tab[rest] = x
    return Tab


print(AWCG(50, 10, 10, 500))
