# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-10 23:09:49
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-10 23:15:18


class Solution(object):
	def isAnagram(self, s, t):
		def insertdic(string):
			res = {}
			for i in string:
				res[i] = res.get(i, 0) + 1
			return res
		sdic, tdic = insertdic(s), insertdic(t)
		if sdic == tdic:
			return True
		return False

