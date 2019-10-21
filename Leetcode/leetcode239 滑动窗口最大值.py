# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-16 12:48:41
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-16 14:38:08


# 双端队列
# 队首元素为窗口最大元素下标 依次为递减元素的下标
# 时间复杂度 O(n)
# 空间复杂度 O(n)
class Solution:
	def maxSlidingWindow(self, nums, K):
		deque = []
		if len(nums) * K == 0:
			return []
			
		def update_deque(pos):
			if deque and deque[0] == pos-K:
				deque.pop(0)
			while deque and nums[deque[-1]] < nums[pos]:
				deque.pop()
			deque.append(i)

		maxpos = 0
		res = []
		for i in range(K):
			update_deque(i)
			if nums[i] > nums[maxpos]:
				maxpos = i
		res.append(nums[maxpos])

		for i in range(K, len(nums)):
			update_deque(i)
			res.append(nums[deque[0]])

		return res


# DP
# 将输入数组分割成有 K 个元素的块
# 时间复杂度 O(n)
# 空间复杂度 O(n)
class Solution2:
	def maxSlidingWindow(self, nums, K):
		if len(nums) * K == 0:
			return []
		left, right = [0]*len(nums), [0]*len(nums)
		left[0], right[-1] = nums[0], nums[-1]

		for i in range(1, len(nums)):
			# 每个块的开头
			if i % K == 0:
				left[i] = nums[i]
			else:
				left[i] = max(left[i-1], nums[i])

		for j in range(len(nums)-2, -1, -1):
			# 每个块的结尾
			if (j+1) % K == 0:
				right[j] = nums[j]
			else:
				right[j] = max(right[j+1], nums[j])

		res = []
		for i in range(len(nums)-K+1):
			res.append(max(right[i], left[i+K-1]))
		return res

