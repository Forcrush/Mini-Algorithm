# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-27 17:50:52
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-27 17:55:47


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
	def removeElements(self, head, val):
		ori = ListNode(0)
		ori.next = head

		pre, cur = ori, head
		while cur:
			nex = cur.next
			if cur.val == val:
				pre.next = nex
			else:
				pre = cur
			cur = nex

		return ori.next