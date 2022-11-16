class Node: 
    def __init__(self, value=None):
        self.value = value  # 节点值
        self.prev = None   # 指向上一个节点
        self.next = None   # 指向下一个节点
 
    def insert(self, prev, next):
        self.prev = prev
        self.next = next
        prev.next = self
        next.prev = self
 
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self
 
 
class LinkedList:

    def __init__(self):
        self.__head = Node()
        self.__tail = Node()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
 
    def isEmpty(self):
        return self.__head.next == self.__tail
 
    def __len__(self):
        count = 0
        cursor = self.__head
        while cursor.next != self.__tail:
            count += 1
            cursor = cursor.next
        return count
 
    def __str__(self):
        value_list = []
        cursor = self.__head
        while cursor.next != self.__tail:
            value_list.append(cursor.next.value)
            cursor = cursor.next
        return str(value_list)
 
    def pushBack(self, value):
        new_node = Node(value)
        new_node.insert(self.__tail.prev, self.__tail)
 
    def popBack(self):
        if not self.isEmpty():
            pop_node = self.__tail.prev.remove()
            return pop_node.value
        return None
 
    def pushFront(self, value):
        new_node = Node(value)
        new_node.insert(self.__head, self.__head.next)
 
    def popFront(self):
        if not self.isEmpty():
            pop_node = self.__head.next.remove()
            return pop_node.value
        return None
 
    def find(self, value):
        find_pos = None
        count = 0
        cursor = self.__head
        while cursor.next != self.__tail:
            if cursor.next.value == value:
                find_pos = count
                break
            count += 1
            cursor = cursor.next
        return find_pos
 
    # 没写异常处理
    def insert(self, pos, value):
        length = len(self)
        if pos >= 0 and pos <= length:
            cursor = self.__head
            count = 0
            while count < pos:
                count += 1
                cursor = cursor.next
            new_node = Node(value)
            new_node.insert(cursor, cursor.next)
            return True
        return False
 
    def remove(self, pos):
        length = len(self)
        if pos >= 0 and pos < length:
            cursor = self.__head.next
            count = 0
            while count < pos:
                count += 1
                cursor = cursor.next
            cursor.remove()
            return True
        return False
 
    def reverse(self):

        if (self.__head.next == self.__tail or
                self.__head.next.next == self.__tail):
            return
        cursor = self.__head
        while cursor != None:
            cursor.prev, cursor.next = cursor.next, cursor.prev
            cursor = cursor.prev
        self.__head, self.__tail = self.__tail, self.__head
 
    def sort(self):
        outer = self.__head.next
        while outer != self.__tail and outer != self.__tail.prev:
            inner = outer
            while inner != self.__tail and inner != self.__tail.prev:
                if inner.value > inner.next.value:
                    inner.value, inner.next.value = inner.next.value, inner.value
                inner = inner.next
            outer = outer.next
 
 
if __name__ == "__main__":
    mylist = LinkedList()
 
    # 尾
    mylist.pushBack(1)
    mylist.pushBack(2)
    print(mylist.popBack())
 
    # 头
    mylist.pushFront(1)
    mylist.pushFront(2)
 
    # 任意位置
    mylist.insert(1, "猫猫球帅")

    print(str(mylist))