# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 15:15:43
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 15:35:45


class Solution:
	def isPalindrome(self, s):
		if len(s) == 0 or len(s) == 1:
			return True
		s = s.lower()
		begin, end = 0, len(s)-1

		def isvalidchr(c):
			if 48 <= ord(c) <= 57 or 97 <= ord(c) <= 122:
				return True
			return False

		while begin <= end:
			if not isvalidchr(s[begin]):
				begin += 1
			if not isvalidchr(s[end]):
				end -= 1
			if isvalidchr(s[begin]) and isvalidchr(s[end]):
				if s[begin] == s[end]:
					begin += 1
					end -= 1
				else:
					return False
		return True
			
			