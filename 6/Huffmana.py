from collections import Counter

def probability(text):
    symbols = {}

    for letter in text:
        if letter in symbols:
            symbols[letter] += 1
        else:
            symbols[letter] = 1
    return symbols

def build_huffman_tree(freq):
    nodes = [[symbol, weight] for symbol, weight in freq.items()]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x[1])
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = [[left, right], left[1] + right[1]]
        nodes.append(new_node)

    return nodes[0]


def assign_codes(tree, add="", codes={}):
    if isinstance(tree[0], str):
        codes[tree[0]] = add
    else:
        assign_codes(tree[0][0], add + "0" , codes)
        assign_codes(tree[0][1], add + "1" , codes)
    return codes


def huffman_encoding(data):
    if not data:
        return {}, ""
    freq = probability(data)
    print(f"Prawdopodobienstwa liter: {freq}")
    huffman_tree = build_huffman_tree(freq)
    huffman_codes = assign_codes(huffman_tree)
    encoded_data = "".join(huffman_codes[symbol] for symbol in data)

    return huffman_codes, encoded_data


exp = "abaacca"
huffman_codes, encoded_data = huffman_encoding(exp)

print(f"Kody Huffmana dla ciągu '{exp}':")
for symbol, code in huffman_codes.items():
    print(f"{symbol}: {code}")
print(f"Zakodowany ciąg: {encoded_data}")
