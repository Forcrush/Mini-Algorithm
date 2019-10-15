# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-13 14:50:12
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-14 09:00:55


# Boyer-Moore 投票算法
# 超过n/3数量的元素最多只能有两个

class Solution:
	def majorityElement(self, nums):
		if nums == []:
			return []
		countA, countB = 0, 0
		candidateA, candidateB = nums[0], nums[0]
		for num in nums:
			if num == candidateA:
				countA += 1
				continue
			if num == candidateB:
				countB += 1
				continue

			if countA == 0:
				candidateA = num
				countA += 1
				continue
			if countB == 0:
				candidateB = num
				countB += 1
				continue

			countA -= 1
			countB -= 1
		res = []

		# 需要再次遍历数组看candidateA, candidateB是否超过n/3
		countA, countB = 0, 0
		for num in nums:
			if num == candidateA:
				countA += 1
			if num == candidateB:
				countB += 1
		if countA > len(nums)//3:
			res.append(candidateA)
		if countB > len(nums)//3:
			res.append(candidateB)

		return list(set(res))

		