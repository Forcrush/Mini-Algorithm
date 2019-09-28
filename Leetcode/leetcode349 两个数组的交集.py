# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-26 14:03:33
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-26 14:09:18


class Solution:
	def intersection(self, nums1, nums2):
		s1 = set(nums1)
		s2 = set(nums2)
		res = set()
		for i in s1:
			if i in s2:
				res.add(i)
		return list(res)

		