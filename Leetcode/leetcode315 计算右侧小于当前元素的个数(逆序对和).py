# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-19 13:43:58
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-22 10:57:54


# 归并排序 + 索引数组
class Solution:
	def countSmaller(self, nums):

		if not nums: return []

		# bind index and element
		arr =[(nums[i], i) for i in range(len(nums))]
		res = [0] * len(nums)

		def merge(arr, left, mid, right):
			tmp = [0] * (right - left + 1)
			i, j = left, mid
			k = 0
			while i < mid and j <= right:
				if arr[i][0] <= arr[j][0]:
					tmp[k] = arr[i]
					res[arr[i][1]] += j - mid
					k += 1
					i += 1
				else:
					tmp[k] = arr[j]
					k += 1
					j += 1
			while i < mid:
				tmp[k] = arr[i]
				res[arr[i][1]] += j - mid
				k += 1
				i += 1
			while j <= right:
				tmp[k] = arr[j]
				k += 1
				j += 1
			for n in range(left, right+1):
				arr[n] = tmp[n-left]


		def mergesort(arr, left, right):
			if left == right:
				return
			mid = (right + left) // 2
			mergesort(arr, left, mid)
			mergesort(arr, mid+1, right)
			merge(arr, left, mid+1, right)

		mergesort(arr, 0, len(nums)-1)
		return res


# 树状数组 + 离散化
class Solution1:
	def countSmaller(self, nums):
		if not nums: return []
		class FenwickTree():
			"""docstring for FenwickTree"""
			def __init__(self, n):
				self.c = [0] * (n+1)

			def lowbit(self, num):
				return num & (-num)

			def update(self, index, delta):
				while index <= len(self.c)-1:
					self.c[index] += delta
					index += self.lowbit(index)

			def getSum(self, index):
				res = 0
				while index > 0:
					res += self.c[index]
					index -= self.lowbit(index)
				return res
				
		# 离散化数组 即按大小排名将原数组元素换成 (1, len(nums)) 之间的元素
		# 不必去重 因为内置sort是稳定排序 离散后的数组逆序对数不变
		# [5,3,6,3,2] -> [4,2,5,3,1]
		tmp = [(nums[i], i) for i in range(len(nums))]
		tmp.sort(key=lambda x:x[0])
		# 将原数组中元素替换成各自的离散值
		for i in range(len(tmp)):
			nums[tmp[i][1]] = i + 1

		# 倒序添加离散数组到树状数组
		# 每次添加时查询树状数组中小于当前元素的个数 即此元素对应的逆序对数
		Ftree = FenwickTree(len(nums))
		res = [0] * len(nums)
		for i in range(len(nums)-1, -1, -1):
			res[i] = Ftree.getSum(nums[i])
			Ftree.update(nums[i], 1)

		return res

