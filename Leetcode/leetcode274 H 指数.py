# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 17:59:59
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 18:19:24


# 时间复杂度 O(n)
# 空间复杂度 O(n)
class Solution:
	def hIndex(self, citations):
		if not citations: return 0

		for i in range(len(citations)):
			if citations[i] > len(citations):
				citations[i] = len(citations)

		# 计数排序思想
		suffix_sum = [0] * (len(citations) + 1)
		for i in citations:
			suffix_sum[i] += 1

		for i in range(len(suffix_sum)-2, -1, -1):
			suffix_sum[i] += suffix_sum[i+1]

		for i in range(len(suffix_sum)):
			if suffix_sum[i] < i:
				return i - 1

		return len(citations)

