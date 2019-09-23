# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-18 16:25:22
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-18 16:32:26


class Solution:
	def removeOuterParentheses(self, S):
		start, end = 0, len(S)-1
		point = 0
		stack_sum = 0
		res = ''
		while point <= end:
			if S[point] == '(':
				stack_sum += 1
			elif S[point] == ')':
				stack_sum -= 1
			if stack_sum == 0:
				res += S[start+1:point]
				start = point + 1
			point += 1
		return res

		