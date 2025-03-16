def insertion_sort(table):
    m = int(len(table))
    for i in range(1, m):
        key = table[i]
        j = i - 1
        while j >= 0 and table[j] > key:
            table[j + 1] = table[j]
            j -= 1
        table[j + 1] = key
    return table

def bubble_sort(table):
    n = int(len(table))
    for i in range(n - 1):
        for j in range(n - 1):
            if table[j] > table[j + 1]:
                table[j], table[j + 1] = table[j + 1], table[j]
    return table

def quick_sort(table):
    if len(table) <= 1:
        return table
    left = []
    right = []
    middle = []
    pivot = table[int(len(table)) // 2]
    for element in table:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        elif element > pivot:
            right.append(element)
    return quick_sort(left) + middle + quick_sort(right)

def heapify(table, n , i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and table[left] > table[largest]:
        largest = left
    if right < n and table[right] > table[largest]:
        largest = right
    if largest != i:
        table[i], table[largest] = table[largest], table[i]
        heapify(table, n, largest)

def heap_sort(table):
    n = len(table)
    for i in range(n//2 - 1, -1, -1):
        heapify(table, n, i)
    for i in range(n-1, 0, -1):
        table[i], table[0] = table[0], table[i]
        heapify(table, i,0)


def merge_sort(table):
    if len(table) <= 1:
        return table
    mid = len(table) // 2
    left = table[:mid]
    right = table[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result






