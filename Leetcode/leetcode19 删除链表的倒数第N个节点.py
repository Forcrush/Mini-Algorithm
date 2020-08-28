# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-06-23 21:27:53
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-06-23 21:44:04


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def removeNthFromEnd(self, head, n):

		newhead = self.reverseList(head)

		if n == 1:
			return self.reverseList(newhead.next)

		pos = newhead
		for _ in range(n-2):
			if pos != None:
				pos = pos.next

		# 此时 pos.next 为待删除结点
		if pos.next != None:
			pos.next = pos.next.next

		return self.reverseList(newhead)

	def reverseList(self, head):
		if head == None or head.next == None:
			return head

		newlist = self.reverseList(head.next)
		head.next.next = head
		head.next = None

		return newlist