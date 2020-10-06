# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-17 16:22:56
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-17 16:26:25


class RandomizedSet:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		import random

		self.dic = {}
		self.arr = []


	def insert(self, val):
		"""
		Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
		"""
		if val in self.dic: return False
		self.arr.append(val)
		self.dic[val] = len(self.arr) - 1


	def remove(self, val):
		"""
		Removes a value from the collection. Returns true if the collection contained the specified element.
		"""
		if val not in self.dic: return False
		remove_idx = self.dic[val]
		last_ele = self.arr[-1]
		self.arr[remove_idx], self.arr[-1] = last_ele, val
		self.dic[last_ele] = remove_idx
		del self.dic[val]

		self.arr.pop()
		return True


	def getRandom(self):
		"""
		Get a random element from the collection.
		"""
		return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()