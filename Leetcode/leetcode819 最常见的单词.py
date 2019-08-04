# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 16:28:23
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 16:47:27


class Solution:
	def mostCommonWord(self, paragraph, banned):
		start = 0
		dic = {}
		paragraph = paragraph.lower()
		def validchr(c):
			if 97 <= ord(c) <= 122:
				return True
			return False
		for i in range(len(paragraph)):
			if validchr(paragraph[i]):
				if i > 0 and not validchr(paragraph[i-1]):
					start = i
				if i == len(paragraph)-1:
					if paragraph[start:i+1] not in banned:
						dic[paragraph[start:i+1]] = dic.get(paragraph[start:i+1], 0) + 1
			else:
				if i > 0 and validchr(paragraph[i-1]):
					if paragraph[start:i] not in banned:
						dic[paragraph[start:i]] = dic.get(paragraph[start:i], 0) + 1

		word = ''
		count = 0
		for key,value in dic.items():
			if value > count:
				word = key
				count = value

		return word

		