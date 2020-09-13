# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-23 12:10:09
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-12 22:30:41


# 含重复元素
# 时间复杂度 O(N)
# 空间复杂度 O(N)
class Solution:
	def wiggleSort(self, nums):
		"""
		Do not return anything, modify nums in-place instead.
		"""

		def divide(arr, left, right):
			tmp = arr[left]
			while left != right:
				while left < right and arr[right] > tmp:
					right -= 1
				if left < right:
					arr[left] = arr[right]
					left += 1
				while left < right and arr[left] < tmp:
					left += 1
				if left < right:
					arr[right] = arr[left]
					right -= 1
			arr[left] = tmp
			return left

		# 找到中位上的那个数
		left, right = 0, len(nums) - 1
		# 中位数索引
		mid = (len(nums) - 1) // 2
		while True:
			tmp = divide(nums, left, right)
			if tmp == mid:
				break
			elif tmp > mid:
				right = tmp - 1
			else:
				left = tmp + 1

		# 3-way-partition 荷兰旗问题
		# 使与中位数相同的数在数组中间
		pivot = nums[mid]
		l, cur, r = 0, 0, len(nums) - 1
		while cur < r:
			if nums[cur] < pivot:
				nums[cur], nums[l] = nums[l], nums[cur]
				l += 1
				cur += 1
			elif nums[cur] > pivot:
				nums[cur], nums[r] = nums[r], nums[cur]
				r -= 1
			else:
				cur += 1

		# 现在的数组: [小于中位数的数, 中位数, 中位数, 中位数, 大于中位数的数]
		# 分成两半 分别逆序后交叉插入
		small, big, tmp_num = mid, len(nums)-1, nums[:]
		for i in range(len(nums)):
			if i % 2 == 0:
				nums[i] = tmp_num[small]
				small -= 1
			else:
				nums[i] = tmp_num[big]
				big -= 1

		# return nums

# print(Solution().wiggleSort([5, 3, 2, 2, 3, 1]))


# 不含重复元素
# 时间复杂度 O(N)
# 空间复杂度 O(1)
class Solution:
	def wiggleSort(self, nums):
		"""Perform Wiggle Sort."""
		for i in range(len(nums)):
			if (i%2 == 1) == (nums[i-1] > nums[i]):
				nums[i-1], nums[i] = nums[i], nums[i-1]

		return nums