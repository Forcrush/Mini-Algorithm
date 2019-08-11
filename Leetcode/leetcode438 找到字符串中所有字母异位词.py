# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 11:11:01
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 12:06:09


class Solution(object):
	def findAnagrams(self, s, p):
		window, need = {}, {}
		for i in p:
			need[i] = need.get(i, 0) + 1
		left, right, match = 0, 0, 0
		res = []
		while right < len(s):
			if s[right] in need:
				window[s[right]] = window.get(s[right], 0) + 1
				if window[s[right]] == need[s[right]]:
					match += 1
			right += 1

			while match == len(need):
				if right - left == len(p):
					res.append(left)
				if s[left] in need:
					window[s[left]] -= 1
					if window[s[left]] < need[s[left]]:
						match -= 1
				left += 1

		return res