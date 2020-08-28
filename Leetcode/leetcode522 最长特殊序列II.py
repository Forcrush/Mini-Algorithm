# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-02-17 13:46:24
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-02-17 14:24:01


class Solution:
	def findLUSlength(self, strs):
		# 按字符串长度从大到小排序
		strs.sort(key=lambda x:-len(x))
		res = -1

		# len(a) <= len(b)
		def isSubSeq(a, b):
			aPos = 0
			for i in b:
				if aPos == len(a):
					break
				aPos += 1 if i == a[aPos] else 0

			return True if aPos == len(a) else False

		for i in range(len(strs)):
			# 判断 i 是否唯一出现 即是否为特殊字符串
			flag = True
			for j in range(len(strs)):
				if i == j: continue
				if len(strs[j]) < len(strs[i]):
					break
				if isSubSeq(strs[i], strs[j]):
					flag = False
					break
			if flag:
				res = max(res, len(strs[i]))

		return res

