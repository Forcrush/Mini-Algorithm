# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 10:35:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 12:32:14


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def sortList(self, head):

		def merge_sort(h):
			if not h or not h.next:
				return h

			slow, fast = h, h
			while fast.next and fast.next.next:
				slow = slow.next
				fast = fast.next.next

			new_head = slow.next
			slow.next = None

			return merge(merge_sort(h), merge_sort(new_head))

		def merge(h1, h2):
			sentry = ListNode(0)
			cur = sentry
			while h1 and h2:
				if h1.val < h2.val:
					cur.next = h1
					h1 = h1.next
					cur = cur.next
				else:
					cur.next = h2
					h2 = h2.next
					cur = cur.next
			if h1:
				cur.next = h1
			if h2:
				cur.next = h2

			return sentry.next

		return merge_sort(head)