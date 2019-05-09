# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-06 17:26:49
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-06 19:47:35


# 采用递归方式，添加左括号的条件是左括号数量小于n，添加右括号的条件是右括号数小于左括号数
class Solution:
	def generateParenthesis(self, n):

		res = []

		def findbracket(s, leftbra, rightbra):
			if rightbra == n:
				res.append(s)
			if leftbra < n:
				findbracket(s+'(', leftbra+1, rightbra)
			if rightbra < leftbra:
				findbracket(s+')', leftbra, rightbra+1)

		findbracket('', 0, 0)

		return res

print(Solution().generateParenthesis(4))