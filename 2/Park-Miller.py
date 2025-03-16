import random

def ParkMiller(a, m, ran):
    Tab = []
    Tab.append(int(random.randint(1, m - 1)))
    for i in range(1, ran):
        Tab.append((a * Tab[i - 1]) % m)
    return Tab


print(ParkMiller(16807, (2 ** 31) - 1, 10))
