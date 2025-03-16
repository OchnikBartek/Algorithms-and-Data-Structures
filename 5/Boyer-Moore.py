def BoyerMoore(text, pattern):
    n = len(text)
    m = len(pattern)
    i = m - 1
    index = []
    output = [" "] * n
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            j = j - 1
            i = i - 1
            if j == -1:
                index.append(i+1)
                output[i+1] = "^"
                i += m - min(j, 1 + in_last(text[i]))
                break
        else:
            i += m - min(j, 1 + in_last(text[i]))
    print("".join(output))
    print(f"Indeksy poczatkowe wzorcow: {index}")

def in_last(letter):
    for element in last.keys():
        if letter == element:
            return last[element]
    return -1


text = 'cbababdcab'
pattern = 'ab'
last = {letter: index for index, letter in enumerate(pattern)}
print(text)
BoyerMoore(text, pattern)
