# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-24 09:57:52
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-24 11:15:12


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 迭代
# 时间复杂度 O(n)
# 空间复杂度 O(1)
class Solution1:
	def reverseList(self, head):
		prev, tmp = None, None
		cur = head
		while cur:
			tmp = cur.next
			cur.next = prev
			prev = cur
			cur = tmp
		return prev


# 递归
# 时间复杂度 O(n)
# 空间复杂度 O(n) 由于使用递归 将会使用隐式栈空间 递归深度可能会达到 n 层
class Solution2:
	def reverseList(self, head):
		def reverse(head):
			if head == None or head.next == None:
				return head
			p = reverse(head.next)
			head.next.next = head
			head.next = None
			return p
		return reverse(head)

		