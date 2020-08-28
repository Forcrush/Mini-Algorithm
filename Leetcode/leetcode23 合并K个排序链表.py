# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-08 00:07:06
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-08 00:32:54


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
时间复杂度：考虑递归「向上回升」的过程
第一轮合并 k/2 组链表 每一组的时间代价是 O(2n)
第一轮合并 k/4 组链表 每一组的时间代价是 O(4n)
第一轮合并 k/8 组链表 每一组的时间代价是 O(8n)

故渐进时间复杂度为 ∑ ((k/2**i) * (2**i * n)) = O(kn*logk)
空间复杂度：递归会使用到 O(logk) 空间代价的栈空间
'''
class Solution:
	def mergeKLists(self, lists):

		# 合并两个有序链表
		def mergeTwoList(l1, l2):
			p1, p2 = l1, l2

			# 虚拟头指针 任意值都可
			pointer = ListNode(0)
			head = pointer

			while p1 and p2:
				if p1.val < p2.val:
					pointer.next = p1
					p1 = p1.next
				else:
					pointer.next = p2
					p2 = p2.next
				pointer = pointer.next

			pointer.next = p1 if p1 else p2

			# 因为head是虚拟的任意指针 可以忽略直接指向下一个
			return head.next

		def merge(lists, l, r):
			if l > r:
				return
			if l == r:
				return lists[l]
			mid = (l + r) // 2
			return mergeTwoList(merge(lists, l, mid), merge(lists, mid+1, r))

		return merge(lists, 0, len(lists)-1)