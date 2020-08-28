# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 21:40:01
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 21:59:21


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def hasCycle(self, head):
		if not head or not head.next: return False

		slow, fast = head, head
		while True:
			if not fast or not fast.next:
				return False
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		