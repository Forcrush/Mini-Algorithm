# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-13 10:45:16
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-13 11:07:51


class Solution:
	def duplicateZeros(self, arr):
		"""
		Do not return anything, modify arr in-place instead.
		"""
		slow, fast = 0, 0
		# 当fast到数组末尾时 slow记录的是能复制到的位置
		while fast < len(arr):
			if arr[slow] == 0:
				fast += 1
			slow += 1
			fast += 1
		# 在loop中多加了一次 需要复原
		slow -= 1
		fast -= 1
		while slow >= 0:
			# 但fast仍可能等于len(arr) 例如输入 [0]
			if fast < len(arr):
				arr[fast] = arr[slow]
			if arr[slow] == 0:
				fast -= 1
				arr[fast] = arr[slow]
			fast -= 1
			slow -= 1

