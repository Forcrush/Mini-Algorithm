# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 22:32:37
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 23:25:51


class Solution:
	def maxNumber(self, nums1, nums2, k):

		def get_k_comb(arr, k):
			to_delete = len(arr) - k
			mono_stack = []
			for i in arr:
				while to_delete and mono_stack and mono_stack[-1] < i:
					to_delete -= 1
					mono_stack.pop()
				mono_stack.append(i)
			print(mono_stack[:k])
			return mono_stack[:k]

		# 注意 按照一般交替方法合并 [6] [6, 7]
		# 会出现 [6, 6, 7] [6, 7, 6] 两种情况
		# 利用 python 数组大小比较来解决这个问题
		def merge(arr1, arr2):
			res = []
			while arr1 or arr2:
				bigger = arr1 if arr1 > arr2 else arr2
				res.append(bigger[0])
				bigger.pop(0)
			return res

		return max([merge(get_k_comb(nums1, i), get_k_comb(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2)])

'''
print(Solution().maxNumber([2,5,6,4,4,0],[7,3,8,0,6,5,7,6,2],15))
'''
