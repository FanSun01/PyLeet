import os

class Node:
    def __init__(self, data, _next = None):
        self.data = data 
        self.next = _next 

class Stack:
    def __init__(self):

        self.__top = None
        self._size = 0

    def push(self, item):
        self.__top = Node(item, self.__top)
        self._size += 1

    def pop(self):
        if self.is__empty():
            raise ValueError("empty stack")
        value =  self.__top.data
        self.__top = self.__top.next
        self._size -= 1
        return value

    def top(self):
        if self.is__empty():
            raise ValueError("empty stack")
        return self.__top.data

    def is__empty(self):
        return self._size == 0

    def size(self):
        return len(self._size)
    def seq(self, string):
        if len(string) %2 :
            return False
        dict = {
            '(':')',
            '[':']'
        }
        for char in string:
            if char in '([':
                self.push(dict[char])
            else:
                if self.is__empty() or self.pop() != char:
                    return False
        return self.is__empty()

if __name__ == '__main__':
    ipt=[]
    opt=[]
    
    with open('3seq/input.txt','r',encoding='utf-8') as a:
        for line in a:
            if '(' in line or ')' in line or '[' in line or ']' in line :
                 ipt.append(list(line.strip('\n').split(',')))            
            
    stack = Stack()
    for x in ipt:
        opt.append(stack.seq(str(x).replace("'", "").strip('[]')))
    
    with open('3seq/output.txt','w',encoding='utf-8') as f:
        for line in opt:      
            f.write(str(line)+'\n')
        f.close()
    
