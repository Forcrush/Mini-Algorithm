'''
Author: Puffrora
Date: 2020-10-08 00:26:00
LastModifiedBy: Puffrora
LastEditTime: 2020-10-08 12:35:40
'''


# @ 主席树/可持久化线段树/函数式线段树
# $ 静态版本

import copy
import bisect


class TreeNode():
    def __init__(self):
        self.left_node = None
        self.right_node = None
        # l, r 表示区间index
        self.l = -1
        self.r = -1
        # 表示区间权值
        self.num = 0


class ChairmanTree():
    def __init__(self, arr):
        self.arr = arr
        self.arr_s = sorted(arr)
        self.node_arr = self.initialization()
    
    # 建树
    def build(self, l, r):
        node = TreeNode()
        node.l, node.r = l, r
        
        # 叶子节点
        if l == r:
            return node
        else:
            mid = (l + r) // 2
            node.left_node = self.build(l, mid)
            node.right_node = self.build(mid+1, r)
            return node

    # 插入新值 表示一颗新根节点加入
    def insert(self, x, node):
        node.num += 1
        
        # 叶子节点
        if node.l == node.r:
            return
        
        mid = (node.l + node.r) // 2
        if mid >= x:
            # ! 节点复用 需要浅拷贝
            left_tmp = copy.copy(node.left_node)
            node.left_node = left_tmp
            self.insert(x, node.left_node)
        else:
            # ! 节点复用 需要浅拷贝
            right_tmp = copy.copy(node.right_node)
            node.right_node = right_tmp
            self.insert(x, node.right_node)

    # 返回主席树的节点数组
    def initialization(self):
        # ! 离散化 bisect巧用
        z = list(map(lambda x: bisect.bisect(self.arr_s, x), self.arr))
        # arr = [25957, 6405, 15770, 26287, 26465, 6405, 6405, 26465]
        # z = [5, 3, 4, 6, 8, 3, 3, 8]
        # 允许重复元素 所以 25957是第5小 6405是第3小
        # print(arr, z)

        initial_node = self.build(1, len(z))
        node_arr = [initial_node]
        for x in z:
            # ! 节点复用 需要浅拷贝
            new_node = copy.copy(node_arr[-1])
            self.insert(x, new_node)
            node_arr.append(new_node)

        return node_arr

    # 此处找到的是离散化数组的元素
    def find_k(self, nl, nr, k):
        if nr.l == nr.r:
            return nr.l
        left_num_diff = nr.left_node.num - nl.left_node.num
        if k <= left_num_diff:
            return self.find_k(nl.left_node, nr.left_node, k)
        else:
            return self.find_k(nl.right_node, nr.right_node, k-left_num_diff)

    # find the kth small number in [l-1, r-1]
    # 此处 l r 代表数组的第几个元素 对应的下标需要减1
    def find_kth_small(self, l, r, k):
        res = self.find_k(self.node_arr[l-1], self.node_arr[r], k)
        return self.arr_s[res-1]


# @ demo
def demo():
    arr = [25957, 6405, 15770, 26287, 26465, 6405, 6405, 26465]
    chairman_tree = ChairmanTree(arr)
    for i in range(1, len(arr)+1):
        for j in range(i, len(arr)+1):
            for k in range(1, max(1, abs(j-i+1))+1):
                print(i, j, k)
                print(chairman_tree.find_kth_small(i, j, k))


demo()