# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 22:16:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 22:28:34


# 单调栈
class Solution:
	def removeKdigits(self, num, k):

		monotone_stack = []

		for i in num:

			while k and monotone_stack and monotone_stack[-1] > i:
				monotone_stack.pop()
				k -= 1
			monotone_stack.append(i)

		res_stack = monotone_stack[:-k] if k else monotone_stack

		return ''.join(res_stack).lstrip('0') or '0'

