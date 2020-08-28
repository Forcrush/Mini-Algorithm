# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-04 23:00:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-04 23:08:13


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
	def deleteDuplicates(self, head):
		
		if not head: return head

		sentry = ListNode(head.val-1)
		cur = sentry
		while head:
			if head.val != cur.val:
				cur.next = head
				cur = cur.next
			head = head.next

		cur.next = None
		return sentry.next