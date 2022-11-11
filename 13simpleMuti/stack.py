class Node:
    def __init__(self, data, _next = None):
        self.data = data
        self.next = _next

class Stack:
    def __init__(self):
        self.__top = None
        self._size = 0

    # 压入
    def push(self, item):
        self.__top = Node(item, self.__top)
        self._size += 1
    
    # 弹出
    def pop(self):
        if self._size == 0:
            raise ValueError("empty stack")
        value =  self.__top.data
        self.__top = self.__top.next
        self._size -= 1
        return value
    
    # 输出栈顶
    def top(self):
        if self._size == 0:
            raise ValueError("empty stack")
        return self.__top.data
              
    # 判空
    def is_empty(self):
        return self._size == 0

if __name__ == '__main__':
        stack = Stack()
        stack.push(1)        
        stack.push('猫猫球帅')
        stack.push(5)
        stack.pop()
        print(stack.top())
    
