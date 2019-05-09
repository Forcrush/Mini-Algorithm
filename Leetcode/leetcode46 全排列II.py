# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-09 12:07:51
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-09 15:00:57


'''
字典序法（可处理含重复数字的全排列）
从最小字典序到最大字典序

寻找序列的下一个字典序：
例如839647521是数字1～9的一个排列 从它生成下一个排列的步骤如下： 

自右至左找出排列中第一个比右边数字小的数字:4						8396475521
在该数字后的数字中找出比4大的数中最小的一个(若有多个取最后一个):5		8396475521
将5与4交换														8396575421
将75421倒转														8396512457

所以839647521的下一个排列是										8396512457

'''
class Solution:
	def permuteUnique(self, nums):
		if nums == []:
			return nums
		if len(nums) == 1:
			return [[nums[0]]]

		res = []

		# 桶排序找出最小序列
		minval = nums[0]
		maxval = nums[0]
		for i in nums:
			minval = min(minval, i)
			maxval = max(maxval, i)
		bucket = [0] * (maxval - minval + 1)
		for i in nums:
			bucket[i-minval] += 1
		nums = []
		for i in range(len(bucket)):
			nums += [i+minval] * bucket[i]

		while True:
			res.append(nums+[])

			# 寻找第一个非递增数 如没有则说明已到最大序列
			for i in range(len(nums)-2, -1, -1):
				if nums[i] < nums[i+1]:
					nonincrease = i
					break
				if i == 0:
					return res

			# 在[nonincrease+1, len(nums)-1]中寻找最小的大于nums[nonincrease]的数 若存在多个相同的此数则取序列中最后一个
			# 因为nums[nonincrease + 1] > nums[nonincrease]
			minpos = nonincrease + 1
			for i in range(nonincrease+1, len(nums)):
				if nums[i] > nums[nonincrease]:
					if nums[i] <= nums[minpos]:
						minpos = i
			nums[nonincrease], nums[minpos] = nums[minpos], nums[nonincrease]

			# 对num[nonincrease+1, len(nums)-1]逆序排列
			lb = nonincrease + 1
			rb = len(nums) - 1
			while lb < rb:
				nums[lb], nums[rb] = nums[rb], nums[lb]
				lb += 1
				rb -= 1

		return res

