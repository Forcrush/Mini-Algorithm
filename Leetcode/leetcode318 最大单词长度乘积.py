# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-23 11:05:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-23 11:14:43


class Solution:
	def maxProduct(self, words):

		dic = {}
		for w in words:
			bit_ID = 0
			for c in w:
				bit_ID |= 1 << (ord(c)-ord('a'))
			dic[w] = bit_ID

		res = 0
		for i in range(len(words)):
			for j in range(i, len(words)):
				if dic[words[i]] & dic[words[j]] == 0:
					res = max(res, len(words[i]) * len(words[j]))

		return res


