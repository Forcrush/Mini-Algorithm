# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-28 21:37:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-28 21:53:15


class Solution:
	def addStrings(self, num1, num2):
		res = ''
		i, j = len(num1)-1, len(num2)-1
		carry = 0
		while i >= 0 and j >= 0:
			tmp = int(num1[i]) + int(num2[j]) + carry
			carry = tmp // 10
			res = str(tmp % 10) + res
			i -= 1
			j -= 1

		while i >= 0:
			tmp = int(num1[i]) + carry
			carry = tmp // 10
			res = str(tmp % 10) + res
			i -= 1

		while j >= 0:
			tmp = int(num2[j]) + carry
			carry = tmp // 10
			res = str(tmp % 10) + res
			j -= 1

		if carry > 0:
			return str(carry) + res
		return res

