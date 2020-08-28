# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-18 17:16:48
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-18 20:30:47


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#  递归
# 时间复杂度 O(N^2)
# 空间复杂度 O(N)
class Solution:
	def reorderList(self, head):
		"""
		Do not return anything, modify head in-place instead.
		"""

		def alter_reverse(head, flag):
			if not head or not head.next:
				return head
			# 奇数位 不需交换
			if flag:
				head.next = alter_reverse(head.next, not flag)
				return head

			# 偶数维 需交换
			else:
				first = head
				while head.next.next:
					head = head.next
				newhead = head.next
				head.next = None
				newhead.next = first
				newhead.next = alter_reverse(newhead.next, not flag)
				return newhead

		alter_reverse(head, True)


# 时间复杂度 O(N)
# 空间复杂度 O(1)
class Solution:
	def reorderList(self, head):
		"""
		Do not return anything, modify head in-place instead.
		"""
		if not head or not head.next or not head.next.next: return

		origin_head = head
		slow, fast = head, head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next

		# 此时 slow 为中间节点
		newhead = slow.next
		slow.next = None

		# 翻转后半部分的链表
		pre, cur = None, newhead
		while cur:
			nex = cur.next
			cur.next = pre
			pre = cur
			cur = nex

		# 交替合并两链表 分别以 origin_head, pre 作为头
		cur1, cur2 = origin_head, pre
		while cur2:
			tmp1 = cur1.next
			tmp2 = cur2.next
			cur1.next = cur2
			cur2.next = tmp1
			cur1 = tmp1
			cur2 = tmp2
			
