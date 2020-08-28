# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 21:51:30
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 22:05:00


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def detectCycle(self, head):
		if not head or not head.next: return None

		slow, fast = head, head
		while True:
			if not fast or not fast.next:
				return None
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				break
		
		new = head
		while new != slow:
			new, slow = new.next, slow.next
		return new