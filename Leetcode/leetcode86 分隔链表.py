# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-04 22:16:24
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-04 22:24:14


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
	def partition(self, head, x):
		
		smaller, bigger = ListNode(0), ListNode(0)
		s_cur, b_cur = smaller, bigger

		while head:
			if head.val < x:
				s_cur.next = head
				s_cur = s_cur.next
			else:
				b_cur.next = head
				b_cur = b_cur.next
			head = head.next

		s_cur.next = bigger.next
		b_cur.next = None

		return smaller.next
