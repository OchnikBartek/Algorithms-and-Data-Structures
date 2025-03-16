class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OneWayList:
    def __init__(self):
        self.head = None

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        if current_node is None:
            print("Indeks poza zakresem listy")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, index):
        current_node = self.head
        if current_node is None:
            return

        if index == 0:
            self.head = current_node.next
            print(f"Usunięto węzeł o indeksie {index}.")
            current_node = None
            return

        current_position = 0
        prev_node = None

        while current_node is not None and current_position != index:
            prev_node = current_node
            current_node = current_node.next
            current_position += 1

        if current_node is None:
            print(f"Nie znaleziono węzła o indeksie {index} do usunięcia.")
            return

        prev_node.next = current_node.next
        print(f"Usunięto węzeł o indeksie {index}.")
        current_node = None
    def search(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return print(f"Wezel {key} zawiera sie w liscie.")
            current_node = current_node.next
        return print(f"Wezel {key} nie zawiera sie w liscie.")

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


lista = OneWayList()
lista.insert(0, 3)
lista.insert(1, 6)
lista.display()
lista.insert(4, 8)
lista.insert(1, 10)
lista.display()
lista.delete(0)
lista.delete(10)
lista.display()
lista.search(3)
lista.search(9)
