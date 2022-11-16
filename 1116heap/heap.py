# 实现一个最大堆
class MaxHeap(object):
    def __init__(self):
        self.array = []

    # 堆化
    def heapify(self, array):
        for a in array:
            self.push(a)
        return self.array

    def get_size(self):
        return len(self.array)

    def _parent(self, index):
        if index == 0:
            raise Exception('Index 0 has no parent')
        return int((index - 1) / 2)

    # 返回左子
    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    # 遍历，实现父大子小
    def _shift_up(self, k):
        while k > 0 and self.array[self._parent(k)] < self.array[k]:
            # 交换节点与父节点的值
            self.array[self._parent(k)], self.array[k] = self.array[k], self.array[self._parent(k)]
            k = self._parent(k)

    def _shift_down(self, k):
        while self._left_child(k) < self.get_size():
            choose_index = self._left_child(k)  # 左孩子的索引
            # 先比较左右孩子的大小，选择较大的那个孩子再与父亲节点进行比较
            if choose_index + 1 < self.get_size() and self.array[choose_index + 1] > self.array[choose_index]:
                choose_index = self._right_child(k)
            if self.array[choose_index] <= self.array[k]:  # 如果最大的孩子比父亲节点小，退出循环
                break
            # 否则父亲节点和最大的子节点交换位置
            self.array[choose_index], self.array[k] = self.array[k], self.array[choose_index]
            k = choose_index  # 进行下次循环

    def push(self, value):
        self.array.append(value)
        self._shift_up(self.get_size() - 1)  # 相当于对堆进行重新堆化

    def pop(self):
        ret = self.find_max()
        self.array[0], self.array[self.get_size() - 1] = self.array[self.get_size() - 1], self.array[0]
        self.array.pop(-1)  # 删除最后一个元素
        self._shift_down(0)
        return ret

    def find_max(self):
        if self.array:
            return self.array[0]
        else:
            raise Exception('Empty heap has no value')


# test = [1,0,1,2,0]
test = [1,3,2,5,4]
max_heap = MaxHeap()
max_heap.heapify(test) # 对一个数组执行堆化
print(max_heap.pop()) # 弹出堆顶元素
print(max_heap.array) 


