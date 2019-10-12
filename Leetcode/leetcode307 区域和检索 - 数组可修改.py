# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-12 08:42:00
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-12 11:41:39


# Method 1
# Segment Tree (线段树)

class NumArray():

	def __init__(self, nums):
		if len(nums) > 0:

			self.seg_tree = [0] * (2 * len(nums))

			for i in range(len(nums)):
				self.seg_tree[i+len(nums)] = nums[i]
			for j in range(len(nums)-1, -1, -1):
				self.seg_tree[j] = self.seg_tree[2*j] + self.seg_tree[2*j+1]

	def update(self, i, val):
		# 更新叶节点
		pos = i + len(self.seg_tree) // 2
		self.seg_tree[pos] = val

		# 回溯到根节点更新
		while pos > 0:
			left, right = pos, pos
			# 为左叶节点
			if pos % 2 == 0:
				right += 1
			# 为右叶节点
			else:
				left -= 1
			self.seg_tree[pos//2] = self.seg_tree[left] + self.seg_tree[right]
			pos //= 2

	def sumRange(self, i, j):

		left = i + len(self.seg_tree) // 2
		right = j + len(self.seg_tree) // 2
		res = 0

		while left <= right:
			if left % 2 == 1:
				res += self.seg_tree[left]
				left += 1
			if right % 2 == 0:
				res += self.seg_tree[right]
				right -= 1

			left //= 2
			right //= 2

		return res


# Method 2
# Binary Indexed Tree (树状数组 / Fenwick Tree)

class NumArray2():

	def __init__(self, nums):
		self.nums = nums
		self.c = [0] * (len(nums) + 1)
		for i in range(len(nums)):
			j = i + 1
			while j <= len(nums):
				self.c[j] += nums[i]
				# 加上self.lowbit(j)后为j的父节点
				j += self.lowbit(j)				

	def lowbit(self, x):
		return x & (-x)

	def update(self, i, val):
		diff = val - self.nums[i]
		self.nums[i] = val
		k = i + 1
		while k <= len(self.nums):
			self.c[k] += diff
			# 加上self.lowbit(k)后为k的父节点
			k += self.lowbit(k)

	# 得到前i个数的和
	def getSum(self, i):
		res = 0
		k = i
		while k > 0:
			res += self.c[k]
			# 减去self.lowbit(k)后为k的上层兄弟节点
			k -= self.lowbit(k)
			
		return res

	def sumRange(self, i, j):
		return self.getSum(j+1) - self.getSum(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
