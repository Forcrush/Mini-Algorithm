# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 16:01:23
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 17:05:49


class KthLargest:

	def __init__(self, k, nums):
		self.k = k
		self.pool = nums

		for hole in range(len(self.pool)//2-1, -1, -1):
			tmp = self.pool[hole]
			child = 2 * hole + 1
			while child <= len(self.pool)-1:
				if child < len(self.pool)-1 and self.pool[child] > self.pool[child+1]:
					child += 1
				if self.pool[child] < tmp:
					self.pool[hole] = self.pool[child]
					hole = child
					child = 2 * hole + 1
				else:
					break
			self.pool[hole] = tmp

		if self.k < len(self.pool):
			for _ in range(len(self.pool)-self.k):
				self.pool[0] = self.pool[-1]
				self.pool.pop()
				hole = 0
				tmp = self.pool[hole]
				child = 2 * hole + 1
				while child <= len(self.pool)-1:
					if child < len(self.pool)-1 and self.pool[child] > self.pool[child+1]:
						child += 1
					if self.pool[child] < tmp:
						self.pool[hole] = self.pool[child]
						hole = child
						child = 2 * hole + 1
					else:
						break
				self.pool[hole] = tmp


	def percolate(self, array, hole, end):
		tmp = array[hole]
		child = 2 * hole + 1
		while child <= end:
			if child < len(array)-1 and array[child] > array[child+1]:
				child += 1
			if array[child] < tmp:
				array[hole] = array[child]
				hole = child
				child = 2 * hole + 1
			else:
				break
		array[hole] = tmp


	def add(self, val):
		if len(self.pool) < self.k:
			self.pool.append(val)
			self.pool[0], self.pool[-1] = self.pool[0], self.pool[-1]
			self.percolate(self.pool, 0, len(self.pool)-1)
			return self.pool[0]
			
		else:
			if val > self.pool[0]:
				self.pool[0] = val
				self.percolate(self.pool, 0, len(self.pool)-1)
				return self.pool[0]
			else:
				return self.pool[0]

