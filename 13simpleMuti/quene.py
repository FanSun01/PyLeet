import os

class Node(object):
    def __init__(self,val):
        self.next=None
        self.val=val

class Queue(object):
    def __init__(self):
        self.first=None
        self.last=None
        self.whole = []
        
    # 进
    def enter(self,n):
        n = Node(n)  
        if self.first==None:
            self.first=n
            self.last=self.first
        else:
            self.last.next=n   
            self.last=n 
  
    # 出
    def quit(self):
        if self.first==None:
            return None
        else:
            tmp=self.first.val
            self.first=self.first.next
        return tmp
    
    # 全弹出
    def allQuit(self):
        Lists=[]
        while self.first!=None:
            Lists.append(self.first.val)
            self.first=self.first.next
        return Lists


if __name__ == "__main__":
    quene=Queue()  
    quene.enter(1)
    quene.enter('猫猫球帅')
    quene.enter('!')
    quene.quit()
    print(quene.allQuit()) 