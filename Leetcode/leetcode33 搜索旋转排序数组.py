# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-23 09:18:23
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-23 10:11:03


class Solution:
	def search(self, nums, target):
		if nums == []:
			return -1
		rotate = -1
		if len(nums) == 1:
			rotate = 0
		# 特殊情况 旋转点为第一个或最后一个
		elif len(nums) > 1:
			if nums[0] < nums[-1]:
				rotate = 0
			if nums[-1] < nums[-2]:
				rotate = len(nums)-1

		if rotate == -1:
			start, end = 0, len(nums)-1
			while start < end:
				mid = start + (end - start) // 2
				if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
					rotate = mid
					break
				if nums[mid] < nums[start]:
					end = mid
				elif nums[mid] > nums[end]:
					start = mid
		
		# return rotate

		def bi_find(start, end, tar):
			while start <= end:
				mid = start + (end - start) // 2
				if nums[mid] == tar:
					return mid
				elif nums[mid] < tar:
					start = mid + 1
				elif nums[mid] > tar:
					end = mid - 1

		if nums[rotate] == target:
			return rotate
		r1 = bi_find(0, rotate-1, target)
		r2 = bi_find(rotate+1, len(nums)-1, target)
		if r1 != None:
			return r1
		if r2 != None:
			return r2
		return -1


a = [3,1]
print(Solution().search(a,3))

