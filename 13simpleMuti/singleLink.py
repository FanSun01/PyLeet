class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def insert_head(self, node):
        self.head, node.next = node, self.head
        self.length += 1

    def lookup(self):
        head = self.head
        while head is not None:
            current, head = head, head.next
            yield current

    def append_node(self, node):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        self.length += 1

    def pop_first(self):
        head = self.head
        if self.head is not None:
            self.head = self.head.next
        self.length -= 1
        return head

    def pop_last(self):
        current = self.head
        while current.next.next is not None:
            current = current.next
        node, current.next = current.next, None
        self.length -= 1
        return node

    def insert(self, index, new_node):
        if self.head is None or index < 1:
            self.head, new_node.next = new_node, self.head
        else:
            current = self.head
            while index > 1 and current.next is not None:
                current = current.next
                index -= 1
            current.next, new_node.next = new_node, current.next
            self.length += 1

    def remove(self, index):

        if self.head is None or index < 0:
            return None
        else:
            current = self.head
            while index > 1 and current.next is not None:
                current = current.next
                index -= 1
            current.next = current.next.next
            self.length -= 1

if __name__ == "__main__":
     # 创建
    linkedlist = LinkedList()
    for i in range(10):
        node = Node(i)
        linkedlist.insert_head(node)
    print(len(linkedlist))

    # 从第index处插入节点
    index = 3
    new_node = Node("new_index")
    linkedlist.insert(index, new_node)
    print(len(linkedlist))

    # 删除index处节点
    index = 4
    linkedlist.remove(index)
    print(len(linkedlist))

    while(linkedlist.head != None):  
        print(linkedlist.head.data)  
        linkedlist.head = linkedlist.head.next