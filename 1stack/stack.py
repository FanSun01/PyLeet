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
        if self._size == 0:
            raise ValueError("empty stack")
        value =  self.__top.data
        self.__top = self.__top.next
        self._size -= 1
        return value
    
    def top(self):
        if self._size == 0:
            raise ValueError("empty stack")
        return self.__top.data
              
    def is_empty(self,input):
        return self.size(input) == 0

    def size(self,input):
        return len(input)
    
    def handleIpt(self,input):
        opt = []
        if self.is_empty(input):
            return
        if self.size(input) == 1:
            return input[0]
        for i in input:
            if '+' in i:
                self.push(i.split('+'))
            if '-' in i:
                opt.append(self.top())
                self.pop()            
            else:
                self.push(i)
        return opt
    
if __name__ == '__main__':
    ipt=[]
    opt=[]
    
    with open('1stack/input.txt','r',encoding='utf-8') as a:
        for line in a:
            ipt.append(list(line.strip('\n').split(',')))

    stack = Stack()
    opt = stack.handleIpt(ipt)
    
    with open('1stack/output.txt','w',encoding='utf-8') as f:
        for line in opt:      
            f.write(str(line).replace('+','').replace('[','').replace(']','').replace("'",'')+'\n')
        f.close()
    