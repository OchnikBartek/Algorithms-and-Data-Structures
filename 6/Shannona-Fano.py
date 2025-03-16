exp = "aaaccab"
lista = list(exp)

letter_count = {}
for word in lista:
    if word in letter_count:
        letter_count[word] += 1
    else:
        letter_count[word] = 1

posortowany = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
print("Posortowane symbole:", posortowany)


def kody(posortowany):
    if len(posortowany) == 1:
        return {posortowany[0][0]: ""}

    total = sum(count for _, count in posortowany)
    acc = 0
    split_index = 0
    for i, (symbol, count) in enumerate(posortowany):
        acc += count
        split_index = i
        if acc >= total / 2:
            break

    left = posortowany[:split_index + 1]
    right = posortowany[split_index + 1:]
    ciag = {}
    left_codes = kody(left)
    for symbol in left:
        ciag[symbol[0]] = "0" + left_codes[symbol[0]]
    right_codes = kody(right)
    for symbol in right:
        ciag[symbol[0]] = "1" + right_codes[symbol[0]]

    return ciag


kody_shanfan = kody(posortowany)
print("Kody Shannona-Fano:")
for symbol, code in kody_shanfan.items():
    print(f"{symbol}: {code}")
print(f"{exp}, zakodowane:")
for element in exp:
    kod = kody_shanfan[element]
    print(f"{kod}",end="")


