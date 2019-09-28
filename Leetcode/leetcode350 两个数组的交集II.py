# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-26 14:09:52
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-26 14:27:07


class Solution:
	def intersect(self, nums1, nums2):
		if len(nums1) < len(nums2):
			shorter = nums1
			longer = nums2
		else:
			shorter = nums2
			longer = nums1

		dic1, dic2 = {}, {}
		for i in shorter:
			dic1[i] = dic1.get(i, 0) + 1
		for j in longer:
			dic2[j] = dic2.get(j, 0) + 1

		dic_res = {}
		for key,value in dic1.items():
			if dic2.get(key, None) != None:
				dic_res[key] = min(value, dic2[key])

		res = []
		for key,value in dic_res.items():
			res.extend([key]*value)

		return res

		