# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 12:06:25
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 12:36:25


class Solution(object):
	def minWindow(self, s, t):
		need, window = {}, {}
		for i in t:
			need[i] = need.get(i, 0) + 1
		left, right, match = 0, 0, 0
		goalstart, goalend = 0, len(s) + 1

		while right < len(s):
			if s[right] in need:
				window[s[right]] = window.get(s[right], 0) + 1
				if window[s[right]] == need[s[right]]:
					match += 1
			right += 1

			while match == len(need):
				if right - left < goalend - goalstart:
					goalstart, goalend = left, right
				if s[left] in need:
					window[s[left]] -= 1
					if window[s[left]] < need[s[left]]:
						match -= 1
				left += 1

		if goalend - goalstart == len(s) + 1:
			return ''
		return s[goalstart:goalend]

