import random

def LFG(j, k, znak): ###0<j<k
    m = 2 ** 31
    TabIn = []
    TabOut = []
    for i in range(k):
        TabIn.append(int(random.randint(0, m-1)))
    for n in range(0,k):
        if znak == "+":
            xn = (TabIn[(k + n - j)%k] + TabIn[n%k]) % m
        if znak == "-":
            xn = (TabIn[k+ n - j] - TabIn[n]) % m
        if znak == "*":
             xn = (TabIn[k + n - j] * TabIn[n]) % m
        if znak == "/":
            xn = (TabIn[k + n - j] / TabIn[n]) % m


        TabOut.append(xn)
    return TabOut


print(LFG(7, 10, '+'))
