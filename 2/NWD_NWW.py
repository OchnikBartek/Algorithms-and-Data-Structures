def nwd(a, b):
    while a != b:
        if a < b:
            b = b - a
        elif a > b:
            a = a - b
    return a

def nww(x,y):
    Nww = (x*y)/nwd(x,y)
    return Nww


print(nwd(24, 136))
print(nww(56, 100))