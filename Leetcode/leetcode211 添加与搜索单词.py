# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-17 14:58:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-17 15:55:23


class WordDictionary:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = {}
		self.flag = False

	def addWord(self, word):
		"""
		Adds a word into the data structure.
		"""
		node = self.root
		for char in word:
			if char not in node:
				node[char] = {}
			node = node[char]

		node['#'] = '#'

	def search(self, word):
		"""
		Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
		"""
		
		def subsearch(word, node):
			i = word[0]
			# 已经到单词结尾 终止匹配
			if len(node) == 1 and '#' in node:
				return
			if i != '.' and i in node:
				if len(word) > 1:
					subsearch(word[1:], node[i])
				elif len(word) == 1 and '#' in node[i]:
					self.flag = True
					return
			if i == '.':
				if len(word) == 1 and len(node) > 0:
					for key,val in node.items():
						if '#' in node[key]:
							self.flag = True
							return
				elif len(word) > 1:
					for key,val in node.items():
						subsearch(word[1:], node[key])

		subsearch(word, self.root)
		flag = self.flag
		self.flag = False
		return flag


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
