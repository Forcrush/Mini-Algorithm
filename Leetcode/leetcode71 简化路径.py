# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-31 12:48:14
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-31 13:11:44


class Solution:
	def simplifyPath(self, path):
		refined = [x for x in path.split('/') if x]
		stack = []
		for i in refined:
			if i == '..':
				if not stack:
					continue
				else:
					stack.pop()
			elif i != '.':
				stack.append(i)
		if not stack: return '/'
		res = ""
		for i in stack:
			res = res + '/' + i
		return res

