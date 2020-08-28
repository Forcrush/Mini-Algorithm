# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-16 14:27:01
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-16 14:27:22


# 大根堆
class max_heap():
    def __init__(self):
        self.heap = []

    # pop 用下滤函数
    def pop(self):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

            pop = self.heap.pop()
            self.perlocate_down(0, len(self.heap)-1)
            return pop
        else:
            return None

    def perlocate_down(self, hole, end):
        if end < hole: return
        tmp = self.heap[hole]
        child = 2 * hole + 1
        while child <= end:
            if child < end and self.heap[child+1] > self.heap[child]:
                child += 1
            if self.heap[child] > tmp:
                self.heap[hole] = self.heap[child]
                hole = child
                child = 2 * hole + 1
            else:
                break
        self.heap[hole] = tmp

    # insert 用上滤函数
    def insert(self, x):
        self.heap.append(x)
        self.perlocate_up(len(self.heap)-1)

    def perlocate_up(self, end):
        hole = end
        tmp = self.heap[hole]
        parent = (hole-1) // 2
        while parent >= 0:
            if self.heap[parent] < tmp:
                self.heap[hole] = self.heap[parent]
                hole = parent
                parent = (hole-1) // 2
            else:
                break
        self.heap[hole] = tmp
'''
a = max_heap()
arr = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1, 0, -19, 8, -5, 551]

for i in arr:
    a.insert(i)
for i in arr:
    print(a.pop())
'''