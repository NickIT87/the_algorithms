class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=' -> ')
            curr = curr.next
        print("None")

    def delete(self, val):
        curr = self.head
        prev = None
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def find(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def length(self):
        return len(self)

    def insert(self, index, val):
        size = len(self)
        if index < 0:
            index = size + index
        if index < 0 or index > size:
            print("Индекс вне диапазона")
            return

        new_node = ListNode(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        prev = None
        curr_index = 0
        while curr and curr_index < index:
            prev = curr
            curr = curr.next
            curr_index += 1

        prev.next = new_node
        new_node.next = curr

    # ✅ len(obj)
    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # ✅ obj[i]
    def __getitem__(self, index):
        size = len(self)
        if index < 0:
            index += size
        if index < 0 or index >= size:
            raise IndexError("Index out of range")

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    # ✅ obj[i] = value
    def __setitem__(self, index, value):
        size = len(self)
        if index < 0:
            index += size
        if index < 0 or index >= size:
            raise IndexError("Index out of range")

        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.val = value


ll = LinkedList()
for i in [1, 2, 3, 4]:
    ll.append(i)
ll.print_list()  # 1 -> 2 -> 3 -> 4 -> None

ll.insert(-1, 99)  # Вставка перед последним элементом
ll.print_list()    # 1 -> 2 -> 3 -> 99 -> 4 -> None

ll.insert(-3, 77)  # Перед 3
ll.print_list()    # 1 -> 2 -> 77 -> 3 -> 99 -> 4 -> None


ll = LinkedList()
for x in [10, 20, 30, 40]:
    ll.append(x)

print(len(ll))       # 4
print(ll[0])         # 10
print(ll[-1])        # 40
ll[1] = 99
ll.print_list()      # 10 -> 99 -> 30 -> 40 -> None
