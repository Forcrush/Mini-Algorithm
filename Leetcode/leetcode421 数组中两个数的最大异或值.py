# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-02-17 12:00:37
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-02-17 13:36:51


class Solution:
	def findMaximumXOR(self, nums):

		class Trie(object):
			"""docstring for Trie"""
			def __init__(self):
				self.root = {}

			def insert(self, nums):
				root = self.root
				for i in nums:
					if i not in root:
						root[i] = {}
					root = root[i]

				root['#'] = '#'

			def getEORValue(self, candidate):
				root = self.root
				val = ""
				for c in candidate:
					if c == "0":
						# 先去找跟此位不一样的位 实现 0 1 异或
						if "1" in root:
							root = root["1"]
							val += "1"
						elif "0" in root:
							root = root["0"]
							val += "0"
						else:
							return int(val, 2)
					elif c == "1":
						if "0" in root:
							root = root["0"]
							val += "1"
						elif "1" in root:
							root = root["1"]
							val += "0"
						else:
							return int(val, 2)
				return int(val, 2)

		trie = Trie()
		for i in nums:
			binNum = bin(i)[2:]
			trie.insert('0'*(32-len(binNum)) + binNum)
		finalVal = 0
		for i in nums:
			binNum = bin(i)[2:]
			val = trie.getEORValue('0'*(32-len(binNum)) + binNum)
			if val > finalVal:
				finalVal = val

		return finalVal

