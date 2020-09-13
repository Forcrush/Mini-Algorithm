# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-14 00:04:08
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-14 00:49:48


class Solution:
	def palindromePairs(self, words):

		def isPanlindrome(s):
			return s == s[::-1]

		dic = {}
		for i,w in enumerate(words):
			dic[w] = i

		res = []
		for w in words:
			# 这里+1是因为，列表切片是前闭后开区间
			# w[:j] 前缀   w[j:] 后缀
			for j in range(len(w)+1):
				# 前缀是回文串 判断后缀的逆序是否在单词列表中
				# 因为是后缀，所以至少要从word的第二位算起，所以j>0
				if j > 0 and isPanlindrome(w[:j]) and w != w[j:][::-1] and w[j:][::-1] in dic:
					res.append([dic[w[j:][::-1]], dic[w]])
				# 后缀是回文串 判断前缀的逆序是否在单词列表中
				if isPanlindrome(w[j:]) and w != w[:j][::-1] and w[:j][::-1] in dic:
					res.append([dic[w], dic[w[:j][::-1]]])
		return res

# print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))