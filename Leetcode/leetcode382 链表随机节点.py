# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-17 11:20:26
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-17 11:43:54


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 蓄水池抽样
class Solution:

	def __init__(self, head):
		"""
		@param head The linked list's head.
		Note that the head is guaranteed to be not null, so it contains at least one node.
		"""
		self.head = head

	def getRandom(self):
		"""
		Returns a random node's value.
		"""
		import random

		cur = self.head
		visited = 1
		pool = cur.val
		cur = cur.next

		while cur:
			visited += 1
			if random.randint(0, visited-1) == 0:
				pool = cur.val
			cur = cur.next

		return pool

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()