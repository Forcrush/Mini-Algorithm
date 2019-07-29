# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-27 12:51:48
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-29 19:22:35


'''
n数之和 模板
'''
class Solution:
	def fourSum(self, nums, target):

		# nums 为有序数组
		def kSum(nums, target, start, k):
			res = []
			if start >= len(nums) or k > len(nums)-start:
				return res
			# 化简到两数之和问题 双指针方法
			if k == 2:
				left, right = start, len(nums)-1
				while left < right:
					if nums[left] + nums[right] == target:
						res.append([nums[left]]+[nums[right]])
						left += 1
						right -= 1

						while left < len(nums) and nums[left] == nums[left-1]:
							left += 1
						while right >= 0 and nums[right] == nums[right+1]:
							right -= 1
					elif nums[left] + nums[right] < target:
						left += 1
					else:
						right -= 1
				return res

			for i in range(start, len(nums)):
				if i > start and nums[i] == nums[i-1]:
					continue
				nextres = kSum(nums, target-nums[i], i+1, k-1)
				for item in nextres:
					res.append([nums[i]] + item)

			return res

		nums.sort()
		return kSum(nums, target, 0, 4)

