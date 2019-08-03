# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-01 10:33:13
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-01 10:33:25


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1, l2):
		temp = ListNode(0)
		temcop = temp
		carry = 0
		while l1 or l2:
			a = l1.val if l1 else 0
			b = l2.val if l2 else 0
			total = a + b + carry
			carry = total // 10
			temcop.next = ListNode(total%10)
			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next 
			temcop = temcop.next
		if carry:
			temcop.next = ListNode(1)

		return temp.next

		