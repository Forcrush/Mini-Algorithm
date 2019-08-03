# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-03 17:38:13
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-03 17:47:29


class Solution(object):
	def guessNumber(self, n):
		begin, end = 1, n
		while begin <= end:
			mid = begin + (end - begin) // 2
			if guess(mid) == 1:
				begin = mid + 1
			elif guess(mid) == -1:
				end = mid - 1
			else:
				return mid

				