# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 12:08:07
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 12:22:55


class Solution(object):
	def checkInclusion(self, s1, s2):
		need, window = {}, {}
		for i in s1:
			need[i] = need.get(i, 0) + 1
		left, right, match = 0, 0, 0

		while right < len(s2):
			if s2[right] in need:
				window[s2[right]] = window.get(s2[right], 0) + 1
				if window[s2[right]] == need[s2[right]]:
					match += 1
			right += 1
			while match == len(need):
				if right - left == len(s1):
					return True
				if s2[left] in need:
					window[s2[left]] -= 1
					if window[s2[left]] < need[s2[left]]:
						match -= 1
				left += 1
		return False
