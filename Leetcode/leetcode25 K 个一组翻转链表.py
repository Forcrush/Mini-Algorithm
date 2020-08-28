# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-06-23 20:28:56
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-08 18:21:56


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
	def reverseKGroup(self, head, k):

		temp = head
		for _ in range(k-1):
			if temp != None:
				temp = temp.next

		# 不够凑成K个
		if temp == None:
			return head

		nexthead = temp.next
		temp.next = None

		# 把当前组逆序
		newhead = self.reverseSingle(head)

		head.next = self.reverseKGroup(nexthead, k)

		return newhead


	# recursion version
	def reverseSingle(self, head):
		if head == None or head.next == None:
			return head
		newlist = self.reverseSingle(head.next)
		head.next.next = head
		head.next = None

		return newlist

	# iteration version
	'''
	def reverseSingle(self, head):
		pre = None
		nex = None
		while head:
			nex = head.next
			head.next = pre
			pre = head
			head = nex

		return pre
	'''