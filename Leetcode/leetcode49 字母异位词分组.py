# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-17 07:31:03
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-17 07:37:37


class Solution:
	def groupAnagrams(self, strs):
		dic = {}
		for word in strs:
			arr = [0] * 26
			for i in word:
				arr[ord(i)-97] += 1
			key = ''
			for i in arr:
				key += str(i)
			dic[key] = dic.get(key, []) + [word]

		res = []
		for key,val in dic.items():
			res.append(val)
		return res

