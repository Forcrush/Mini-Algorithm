# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-14 23:00:18
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-14 23:21:44


class Solution:
	def reverseStr(self, s, k):
		def sub_reverse(array, start, end):
			while start <= end:
				array[start], array[end] = array[end], array[start]
				start += 1
				end -= 1

		s = list(s)
		remain = len(s) % (2 * k)
		if remain <= k:
			for i in range(0, len(s)-remain, 2*k):
				sub_reverse(s, i, i+k-1)
			sub_reverse(s, len(s)-remain, len(s)-1)
		else:
			for i in range(0, len(s), 2*k):
				sub_reverse(s, i, i+k-1)
		res = ''
		for i in s:
			res += i
		return res

		