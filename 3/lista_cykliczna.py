class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_index(self, new_data, index):
        new_node = Node(new_data)
        if index > self.length or index < 0:
            print("Wyszedles poza zakres")
            return
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.length += 1
            return
        current_node = self.head
        if index == 0:
            new_node.next = self.head
            current_node = self.head
            while current_node.next is not self.head:
                current_node = current_node.next
            current_node.next = new_node
            self.head = new_node
            self.length += 1
            return

        elif index == self.length:
            while current_node.next is not self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
            self.length += 1
            return
        else:
            current_index = 0
            while current_index < index - 1:
                current_node = current_node.next
                current_index += 1
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            return

    def delete_index(self, index):
        if self.head is None:
            print("Lista pusta")
            return
        if index > self.length or index < 0:
            print("Wyszedles poza zakres")
            return
        current_node = self.head
        if index == 0:
            if self.length == 1:
                self.head = None
            else:
                while current_node.next is not self.head:
                    current_node = current_node.next
                current_node.next = self.head.next
                self.head = self.head.next
            self.length -= 1
            return
        if index == self.length:
            current_index = 0
            while current_index < index - 1:
                current_node = current_node.next
                current_index += 1
            current_node.next = self.head
            self.length -= 1
            return
        else:
            current_index = 0
            while current_index < index - 1:
                current_node = current_node.next
                current_index += 1
            current_node.next = current_node.next.next
            self.length -= 1
            return

    def display(self):
        if self.head is None:
            print("Lista jest pusta")
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("(Powrót do głowy)")

    def search(self, key):
        if self.head is None:
            print(f"Wezel {key} nie zawiera sie w liscie.")
            return
        current_node = self.head
        while True:
            if current_node.data == key:
                print(f"Wezel {key} zawiera sie w liscie.")
                return
            current_node = current_node.next
            if current_node == self.head:
                break
        print(f"Wezel {key} nie zawiera sie w liscie.")


lista = CircularList()
lista.insert_index(6, 0)
lista.insert_index(10, 0)
lista.insert_index(13,5)
lista.insert_index(26,2)
lista.insert_index(33,1)
lista.insert_index(61, 2)
lista.display()
lista.delete_index(0)
lista.display()
lista.delete_index(3)
lista.display()
lista.delete_index(1)
lista.display()
lista.delete_index(10)
lista.search(33)
lista.search(10)

