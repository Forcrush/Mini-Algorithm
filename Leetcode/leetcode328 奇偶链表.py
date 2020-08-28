# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-24 14:57:36
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-24 15:04:14


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def oddEvenList(self, head):

		odd, even = ListNode(0), ListNode(0)
		odd_cur, even_cur = odd, even
		cur = head
		flag = True
		while cur:
			if flag:
				odd_cur.next = cur
				odd_cur = cur
				cur = cur.next
				flag = not flag
			else:
				even_cur.next = cur
				even_cur = cur
				cur = cur.next
				flag = not flag

		even_cur.next = None
		odd_cur.next = even.next
		
		return odd.next