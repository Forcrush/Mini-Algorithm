# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 15:40:16
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 16:28:08


class Solution:
	def validPalindrome(self, s):
		begin, end = 0, len(s)-1
		def completePalindrome(sen):
			if len(sen) == 1:
				return True
			b, e = 0, len(sen)-1
			while b <= e:
				if sen[b] == sen[e]:
					b += 1
					e -= 1
				else:
					return False
			return True

		while begin <= end:
			if s[begin] != s[end]:
				if completePalindrome(s[begin+1:end+1]) or completePalindrome(s[begin:end]):
					return True
				return False
			else:
				begin += 1
				end -= 1
		return True

		