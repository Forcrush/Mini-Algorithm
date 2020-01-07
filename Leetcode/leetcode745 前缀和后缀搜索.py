# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-17 16:56:11
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-19 14:06:13


# 对于单词 dog, 向字典树中插入 #dog g#dog og#dog dog#dog
# 对于 前缀d 后缀og 这样的查询 只需查找 og#d
class WordFilter:

	def __init__(self, words):
		self.root = {}
		self.weight = 'weight'
		for pos,word in enumerate(words):
			for i in range(len(word), -1, -1):
				node = self.root
				node[self.weight] = pos
				newword = word[i:len(word)] + '#' + word
				for c in newword:
					if c not in node:
						node[c] = {}
					node = node[c]
					node[self.weight] = pos
		
	def f(self, prefix, suffix):
		query = suffix + '#' + prefix
		node = self.root
		res = -1
		for char in query:
			if char in node:
				node = node[char]
				# 在插入时 pos 一直在覆盖 因此若能达到某一结点 此节点记录的一定是到达此的 pos 最大的单词
				res = node[self.weight]
			else:
				return -1
		return res


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)