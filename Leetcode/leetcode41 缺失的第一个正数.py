# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-08 19:13:52
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-08 20:02:52


'''
检查 1 是否存在于数组中。如果没有，则已经完成，1 即为答案。
如果 nums = [1]，答案即为 2 。
将负数，零，和大于 n 的数替换为 1 。
遍历数组。当读到数字 a 时，替换第 a 个元素的符号。
注意重复元素：只能改变一次符号。由于没有下标 n ，使用下标 0 的元素保存是否存在数字 n。
再次遍历数组。返回第一个正数元素的下标。
如果 nums[0] > 0，则返回 n 。
如果之前的步骤中没有发现 nums 中有正数元素，则返回n + 1
'''
# Time Complexity: O(n) | Space Complexity O(1)
class Solution:
	def firstMissingPositive(self, nums):
		if 1 not in nums:
			return 1
		if nums == [1]:
			return 2
		for i in range(len(nums)):
			if nums[i] < 1 or nums[i] > len(nums):
				nums[i] = 1
		for i in range(len(nums)):
			tmp = abs(nums[i])
			if tmp == len(nums):
				nums[0] = -abs(nums[0])
			else:
				nums[tmp] = -abs(nums[tmp])
		for i in range(1, len(nums)):
			if nums[i] > 0:
				return i
		if nums[0] < 0:
			return len(nums) + 1
		else:
			return len(nums)

