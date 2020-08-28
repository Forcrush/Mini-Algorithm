# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-24 19:04:51
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-24 20:13:11


class Solution:
	def maxSumSubmatrix(self, matrix, k):

		# 给定一个长度为n的数组，求数组的最大子序和，这个子序和要求不能超过k
		'''
		求 sum[0, j] - sum[0, i] <= k 同时保持最大
		把这个式子变换一下就会是sum[0, j] - k <= sum[0, i]
		我们注意到sum[0, i]会先计算出来，然后后面才计算出sun[0, j]
		'''
		import bisect

		def max_subarray_sum(nums, k):
			arr = [0]
			cur_sum = 0
			res = float("-inf")
			for n in nums:
				cur_sum += n
				# 在 arr 里面找比 cur_sum - k 大但最接近的数
				loc = bisect.bisect_left(arr, cur_sum-k)
				# loc > len(arr) 则说明 arr 中所有数都小于 cur_sum-k
				if loc < len(arr):
					# 目前对于每次遍历 cum - array[loc] 都会是比 k 小的
					# 但是我们不仅要比 k 小还要最接近 k 因此在这些数里面找最大
					res = max(res, cur_sum-arr[loc])
				# 加入cur_sum 并且还要维护排序
				bisect.insort(arr, cur_sum)

			return res

		res = float("-inf")
		for l in range(len(matrix[0])):
			pre_sum = [0] * len(matrix)
			for r in range(l, len(matrix[0])):
				for i in range(len(matrix)):
					pre_sum[i] += matrix[i][r]

				res = max(res, max_subarray_sum(pre_sum, k))
				if res == k:
					return res
		return res

		