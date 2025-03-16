import random
def lcg(a,c,ran):
    Tab = []
    m = 2**32
    Tab.append(int(random.randint(1, 100)))
    for i in range(ran):
        xn = (a * Tab[i] + c) % m
        Tab.append(xn)
    return Tab

print(lcg(1664525,1013904223,30))