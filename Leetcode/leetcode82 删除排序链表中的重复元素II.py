# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-04 23:14:44
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-04 23:44:51


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def deleteDuplicates(self, head):

		if not head: return head

		def filter_dup(h):
			if h == None or h.next == None:
				return h
			if h.val != h.next.val:
				h.next = filter_dup(h.next)
				return h
			while True:
				if h.next == None:
					return None
				if h.val == h.next.val:
					h = h.next
				else:
					return filter_dup(h.next)

		return filter_dup(head)