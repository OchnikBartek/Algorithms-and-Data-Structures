def weight(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


expresion = input("Podaj wyrazenie, ktore chcesz przekszalcic z postaic infiksowej na postfiksowa: ")
operators = []
output = []
for char in expresion:
    if char.isdigit():
        output.append(char)
    elif char == "(":
        operators.append(char)
    elif char == ")":
        while operators and operators[-1] != '(':
            output.append(operators.pop())
        operators.pop()
    elif char in "+-*/":
        while (operators and operators[-1] != '(' and weight(operators[-1]) >= weight(char)):
            output.append(operators.pop())
        operators.append(char)
    else:
        print("W twoim wyrazeniu znajduje sie zly znak")
        output = []
        break

while operators:
    output.append(operators.pop())

print(" ".join(output))

expresion2 = input("Podaj wyrazenie, ktore chcesz przekszalcic z postaic postfiksowej na infiskowa: ")
output2 = []
for char in expresion2:
    if char.isdigit():
        output2.append(char)
    elif char in "+-*/":
        b = output2.pop()
        a = output2.pop()
        if char in "*/":
            result = f"{a} {char} {b}"
        else:
            result = f"({a} {char} {b})"
        output2.append(result)
    else:
        print("W twoim wyrazeniu znajduje sie zly znak")
        output2 = []
        break

print(" ".join(output2))
