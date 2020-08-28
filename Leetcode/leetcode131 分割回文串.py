# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 19:28:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 19:40:06


class Solution:
	def partition(self, s):
		
		def isPalin(candidate):
			l, r = 0, len(candidate) - 1
			while l <= r:
				if candidate[l] != candidate[r]:
					return False
				l += 1
				r -= 1
			return True

		def find_all(start, end):
			res = []
			if start > end:
				return [[]]

			for i in range(start, end+1):
				if isPalin(s[start:i+1]):
					if i+1 in memo:
						sub_item = memo[i+1]
					else:
						sub_item = find_all(i+1, end)
					for item in sub_item:
						res.append([s[start:i+1]] + item)

			memo[start] = res
			return res

		memo = {}
		return find_all(0, len(s)-1)

