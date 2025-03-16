
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def forward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print(None)

    def backward(self):
        cuurrent_node = self.tail
        while cuurrent_node is not None:
            print(cuurrent_node.data, end="<-")
            cuurrent_node = cuurrent_node.prev
        print(None)

    def insert_index(self, new_data, index):
        new_node = Node(new_data)
        if index == 0:
            new_node = Node(new_data)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
            return
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        if current_node is None:
            print("Wyszedles poza zakres")
            return
        if current_node.next is None:
            new_node = Node(new_data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                current_node = self.head
                while current_node.next is not None:
                    current_node = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                self.tail = new_node
            return
        else:
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next = new_node

    def delete_index(self, index):
        if self.head is None:
            print("Lista pusta")
            return
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index:
            current_node = current_node.next
            current_index += 1
        if current_node is None:
            print("Wyszedles poza zakres")
            return
        if current_node.next is None:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            if current_node.prev is not None:
                current_node.prev.next = None
                self.tail = current_node.prev
            return
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        return

    def search(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return print(f"Wezel {key} zawiera sie w liscie.")
            current_node = current_node.next
        return print(f"Wezel {key} nie zawiera sie w liscie.")

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="<->")
            current_node = current_node.next
        print(None)


lista = DoublyLinkedList()
lista.insert_index(2, 0)
lista.insert_index(3, 0)
lista.insert_index(12, 2)
lista.insert_index(20, 3)
lista.insert_index(8, 4)
lista.insert_index(11, 10)
lista.insert_index(57, 5)
lista.print_list()
print("wyswietlanie od przodu")
lista.forward()
print("wyswietlanie od tylu")
lista.backward()
lista.print_list()
lista.delete_index(3)
lista.print_list()
lista.delete_index(0)
lista.print_list()
lista.delete_index(15)
lista.print_list()
lista.delete_index(1)
lista.print_list()
lista.delete_index(2)
lista.print_list()
lista.search(3)
lista.search(100)
