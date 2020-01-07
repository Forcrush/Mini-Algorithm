# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-16 17:09:25
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-16 17:24:41


class Trie:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = {}

	def insert(self, word):
		"""
		Inserts a word into the trie.
		"""
		root = self.root
		for char in word:
			if char not in root:
				root[char] = {}
			root = root[char]
			
		# flag of end
		root['#'] = '#'

	def search(self, word):
		"""
		Returns if the word is in the trie.
		"""
		root = self.root
		for char in word:
			if char not in root:
				return False
			root = root[char]

		if '#' not in root:
			return False

		return True


	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		root = self.root
		for char in prefix:
			if char not in root:
				return False
			root = root[char]

		return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)