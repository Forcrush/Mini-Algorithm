# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-26 14:46:05
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-26 14:52:30


class Solution:
	def reverseVowels(self, s):
		s = list(s)
		vowels = ['a', 'A', 'o', 'O', 'u', 'U', 'e', 'E', 'i', 'I']
		start, end = 0, len(s) - 1
		while start <= end:
			if s[start] in vowels and s[end] in vowels:
				s[start], s[end] = s[end], s[start]
				start += 1 
				end -= 1
			elif s[start] not in vowels:
				start += 1
			elif s[end] not in vowels:
				end -= 1
		
		return ''.join(s)

