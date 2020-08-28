# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-16 17:46:47
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-16 18:04:22


# 时间复杂度：O(nklogk) 其中 n 是所有列表的平均长度，k 是列表数量
# 空间复杂度：O(k)
class Solution:
	def smallestRange(self, nums):

		import heapq as hq

		min_heap = []
		max_val = nums[0][0]
		range_l, range_r = float("-inf"), float("inf")
		for i in range(len(nums)):
			min_heap.append((nums[i][0], i, 0))
			max_val = max(max_val, nums[i][0])
		hq.heapify(min_heap)
		while True:
			min_val, arr_index, index = hq.heappop(min_heap)
			if max_val - min_val < range_r - range_l:
				range_l, range_r = min_val, max_val

			# 某一个数组到达最后一个元素 可退出 因为后面能找到的区间必不包含此数组元素
			if index == len(nums[arr_index]) - 1:
				break

			max_val = max(max_val, nums[arr_index][index+1])
			hq.heappush(min_heap, (nums[arr_index][index+1], arr_index, index+1))

		return [range_l, range_r]
