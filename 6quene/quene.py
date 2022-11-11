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
        
    def enter(self,n):
        n = Node(n)  
        if self.first==None:
            self.first=n
            self.last=self.first
        else:
            self.last.next=n   
            self.last=n 
  

    def quit(self):
        if self.first==None:
            return None
        else:
            tmp=self.first.val
            self.first=self.first.next
        return tmp
    
    def allQuit(self):
        Lists=[]
        while self.first!=None:
            Lists.append(self.first.val)
            self.first=self.first.next
        return Lists


if __name__ == "__main__":
    ipt=[]
    opt=[]
    seq=[]
    quene=Queue()  
    with open('6quene/input.txt','r',encoding='utf-8') as a:
        for line in a:
            ipt.append(list(line.strip('\n').split(',')))   
            
    for x in ipt:
        if '+' in str(x):
            quene.enter(int(str(x).replace("'", "").replace('+', '').strip('[]')))
            seq.append(int(str(x).replace("'", "").replace('+', '').strip('[]')))
        if '-' in str(x):
            seq.remove(quene.first.val)
            quene.quit()
        if '?' in str(x):
            c = seq[0]
            b = seq[::-1]
            while b:
                i = b.pop()
                if i < c:
                    c = i
            opt.append(c)
            
    
    with open('6quene/output.txt','w',encoding='utf-8') as f:
        for line in opt:      
            f.write(str(line)+'\n')
        f.close()