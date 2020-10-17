'''
Author: Puffrora
Date: 2020-10-14 16:43:22
LastModifiedBy: Puffrora
LastEditTime: 2020-10-14 17:05:42
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        total_len = 0
        pos = root
        while pos:
            total_len += 1
            pos = pos.next
        
        res = []

        # 全部分割成单个节点
        if k >= total_len:
            cur = root
            for _ in range(k):
                if cur:
                    new_head = cur.next
                    cur.next = None
                    res.append(cur)
                    cur = new_head
                else:
                    res.append(None)
        # 存在长度大于 1 的链表
        else:
            remainder = total_len % k
            block_len = total_len // k
            cur = root
            for _ in range(k):
                if remainder > 0:
                    cur_len = block_len + 1
                    remainder -= 1
                else:
                    cur_len = block_len

                tmp = cur
                for _ in range(cur_len-1):
                    cur = cur.next
                new_head = cur.next
                cur.next = None
                res.append(tmp)
                cur = new_head
        
        return res
