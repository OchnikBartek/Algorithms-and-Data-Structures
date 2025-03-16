def Naiwny(text,pattern):
    n = len(text)
    m = len(pattern)
    i = 0
    output = [" "] * n
    index = []
    while i <= n-m:
        if text[i:i+m] == pattern:
            output[i] = "^"
            index.append(i)
        i += 1
    print("".join(output))
    print(f"Indeksy poczatkowe wzorcow: {index}")


text = 'abbcbaababcab'
pattern = 'ab'
print(text)
Naiwny(text,pattern)



