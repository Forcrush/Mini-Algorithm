# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-01 11:34:51
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-01 11:45:54


class Solution:
	def findSubstring(self, s, words):
		if s == "" or words == []: return []

		word_len = len(words[0])
		sent_len = len(words)*word_len

		word_dic = {}
		for i in words:
			word_dic[i] = word_dic.get(i, 0) + 1

		res = []
		pointer = 0
		while pointer <= len(s) - sent_len:

			tmp = {}
			for j in range(pointer, pointer+sent_len, word_len):
				tmp[s[j:j+word_len]] = tmp.get(s[j:j+word_len], 0) + 1

			if word_dic == tmp:
				res.append(pointer)

			pointer += 1
		
		return res

s = "r"
words = ['er']
print(Solution().findSubstring(s,words))