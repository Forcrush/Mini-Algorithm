# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-08 17:55:42
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-08 18:23:39


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def reverseBetween(self, head, m, n):

		def reverseSingle(root):
			pre, nex = None, None
			while root:
				nex = root.next
				root.next = pre
				pre = root
				root = nex
			return pre

		cnt = 1
		tmp = head

		if m == 1:
			while head:
				if cnt == n:
					npos = head
					break
				head = head.next
				cnt += 1

			nnext = npos.next
			npos.next = None
			newhead = reverseSingle(tmp)
			tmp.next = nnext

			return newhead
		else:
			while head:
				if cnt == m-1:
					prempos = head
				if cnt == n:
					npos = head
					break
				head = head.next
				cnt += 1

			mpos = prempos.next
			nnext = npos.next
			npos.next = None

			newhead = reverseSingle(mpos)
			prempos.next = newhead
			mpos.next = nnext

			return tmp
