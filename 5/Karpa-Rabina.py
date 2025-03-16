def KarpaRabina(text,pattern):
    n = len(text)
    m = len(pattern)
    d = 256
    p = 101
    hash_pattern = 0
    hash_text = 0
    for i in range(m):
        hash_pattern = (hash_pattern * d + ord(pattern[i])) % p
    for i in range(m):
        hash_text = (hash_text * d + ord(text[i])) % p
    index = []
    output = [" "] * n
    for i in range(n-m + 1):
        if hash_text == hash_pattern:
            if text[i:i+m] == pattern:
                index.append(i)
                output[i] = "^"
        if i < n - m:
            hash_text = (d * (hash_text - ord(text[i]) * pow(d, m - 1, p)) + ord(text[i + m])) % p
            if hash_text < 0:
                hash_text += p
    print("".join(output))
    print(f"Indeksy poczatkowe wzorcow: {index}")



text = 'cbababcbabcbab'
pattern = 'ab'
print(text)
KarpaRabina(text,pattern)
