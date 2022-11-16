class BinaryTree:
    def __init__(self,rootObj):
        self.val = rootObj
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    #前序遍历
    def PreOrder(self, node):
        if node:
            print(node.val)
            self.PreOrder(node.left)
            self.PreOrder(node.right)
            
    #中序遍历
    def InOrder(self, node):
        if node:
            self.InOrder(node.left)
            print(node.val)
            self.InOrder(node.right)
            
    #后续遍历. 这边都选的递归方法， 循环方式下面下个例子
    def PostOrder(self, node):
        if node:
            self.PostOrder(node.left)
            self.PostOrder(node.right)
            print(node.val)
            
    #后续遍历，循环方式
    def PostOrderLoop(self, node):
        if node == None:
            return
        stack =[]
        stack.append(node)
        pre = None
        while stack!=[]:
            node = stack[-1]
            if ((node.left==None and node.right==None) or
                    (pre and (pre == node.left or pre ==node.right))):
                print(node.val)
                pre = node
                stack.pop()
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                    

    # 计算深度
    def getTreeDepth(self, root):
        if root == None:
            return 0
        left = self.getTreeDepth(root.left) + 1
        right = self.getTreeDepth(root.right) + 1
        return left if left>right else right

    #计算节点数
    def CountNode(self, root):
        if root == None:
            return 0
        return self.CountNode(root.left) + self.CountNode(root.right) + 1

    #计算叶子数
    def countLeaves(self, root):
        if root == None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.countLeaves(root.left)+self.countLeaves(root.right)

   # 计算K层节点数
    def getKLevel(self, root, K):
        if root == None: return 0
        if K == 1: return 1
        return self.getKLevel(root.left, K-1)+self.getKLevel(root.right, K-1)

    # 找最近的公共祖先
    def findLCA(self, root, node1, node2):
        if root == None: return
        if root == node1 or root == node2: return root
        left = self.findLCA(root.left, node1, node2)
        right = self.findLCA(root.right, node1, node2)
        if left and right:
            return root
        return left if left else right

    # 找一个节点所有的父节点
    def findAllAncestor(self, root, target):
        if root == None: return False
        if root == target: return True
        if self.findAllAncestor(root.left, target) or self.findAllAncestor(root.right, target):
            print(root.val)
            return True
        return False

    # 计算两个节点的距离
    def getDist(self, root, node1, node2):
        lca = self.findLCA(root, node1, node2)
        level1 = self.FindLevel(lca, node1) 
        level2 = self.FindLevel(lca, node2)
        return level1+level2
    def FindLevel(self, node, target):
        if node == None: return -1
        if node == target: return 0
        level = self.FindLevel(node.left, target)
        if level == -1: level = self.FindLevel(node.right, target)
        if level != -1: return level + 1
        return -1

    # 判断两颗二叉树是否一样
    def StrucCmp(self, root1, root2):
        if root1 == None and root2 == None: return True
        elif root1 ==None or root2 == None: return False
        return self.StrucCmp(root1.left, root2.left) and self.StrucCmp(root1.right, root2.right)




# test
#create a BinaryTree [18,7,11,3,4,5,6,#,#,#,#,1,3,2,4]
#  18
# 7  11
#3 4 5 6
#   1 3 2 4
# 你第二题题目就是算深度，其他没看懂，树的算法无非就这些，看着抄就行
# 测试例子自己改 空就不用赋

root = BinaryTree(18)
root.left = BinaryTree(7)
root.right = BinaryTree(11)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(4)
root.right.left = BinaryTree(5)
root.right.right = BinaryTree(6)
root.right.left.left = BinaryTree(1)
root.right.left.right = BinaryTree(3)
root.right.right.left = BinaryTree(2)
root.right.right.right = BinaryTree(4)
print(root.getTreeDepth(root))
