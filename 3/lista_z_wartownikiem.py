class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SentinelList():
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.head = self.sentinel
        self.length = 0
    def insert_index(self,new_data,index):
        new_node = Node(new_data)
        if index > self.length or index < 0:
            print("Wyszedles poza zakres")
            return
        current_node = self.sentinel
        if index == 0:
            new_node.next = self.sentinel.next
            self.sentinel.next = new_node
            self.length += 1
            return
        elif index == self.length:
            while current_node.next is not self.sentinel:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.sentinel
            self.length += 1
            return
        else:
            current_index = 0
            while current_index < index:
                current_node = current_node.next
                current_index += 1
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            return
    def delete_index(self,index):
        if self.sentinel.next is self.sentinel:
            print("Lista pusta")
            return
        if index > self.length or index < 0:
            print("Wyszedles poza zakres")
            return
        current_node = self.head
        if index == 0:
            to_delete = self.sentinel.next
            self.sentinel.next = to_delete.next
            self.length -= 1
            return
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1

        to_delete = current_node.next
        current_node.next = to_delete.next
        self.length -= 1

    def search(self, key):
        current_node = self.sentinel.next
        index = 0
        while current_node != self.sentinel:
            if current_node.data == key:
                print(f"Element występuje w liście na indeksie {index}")
                return
            current_node = current_node.next
            index += 1

        print("Element nie występuje w liście")

    def display(self):
        current_node = self.sentinel.next
        while current_node != self.sentinel:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

lista = SentinelList()

lista.insert_index(5,0)
lista.insert_index(10,1)
lista.insert_index(84,0)
lista.insert_index(76,1)
lista.insert_index(98,3)
lista.insert_index(1,6)
lista.display()
lista.delete_index(0)
lista.display()
lista.delete_index(2)
lista.display()
lista.delete_index(2)
lista.display()
lista.delete_index(10)
lista.search(100)
lista.search(5)
