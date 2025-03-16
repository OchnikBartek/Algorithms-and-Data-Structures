def fibonacci(n):
    output = [0]
    a, b, m = 0, 1, 10
    for i in range(1, n):
        a, b = b, (a + b) % m
        output.append(a)
    return output


print(fibonacci(20))
