# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-24 18:06:16
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-24 18:21:14


class Solution:
	def findRepeatedDnaSequences(self, s):
		if len(s) < 10:
			return []
		seqset = set()
		res = set()
		for i in range(len(s)-9):
			if s[i:i+10] in seqset:
				print(i, 'yes')
				res.add(s[i:i+10])
			else:
				seqset.add(s[i:i+10])
		return list(res)

