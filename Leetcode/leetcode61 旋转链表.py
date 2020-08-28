# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-31 00:31:05
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-31 01:16:44


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def rotateRight(self, head, k):
	
		def reverse(head):
			pre, cur = None, head
			while cur:
				nex = cur.next
				cur.next = pre
				pre = cur
				cur = nex
			return pre

		if not head:
			return head
			
		length = 0
		tmp = head
		while tmp:
			tmp = tmp.next
			length += 1

		# 输入: 1->2->3->4->5->NULL, k = 2
		# 输出: 4->5->1->2->3->NULL
		# 此时 cut_pos 为 3
		cut_pos = length - (k % length)
		if cut_pos == length:
			return head

		cnt = 1
		cur = head
		while cur:
			if cnt == cut_pos:
				newhead = cur.next
				cur.next = None
				re_newhead = reverse(newhead)
				newhead = reverse(re_newhead)
				re_newhead.next = head
				return newhead

			cur = cur.next
			cnt += 1
		