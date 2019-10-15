# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-14 11:01:24
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-14 19:08:06


# 双指针left right 窗口移动
# 当 A[right] = 1 时 left 不变 right 继续移动
# 当 A[right] = 0 时，
# 	0 的数量在 K 的范围内 left 不变 right 继续移动
# 	0 的数量 > K
# 		当 A[left] == 0 时 即 left 指向了一个零 只需要 left 右移一格 就可以减少一个零
# 		当 A[left] == 1 时 即此时窗口内包了 K 个零 需要先移动至下个零再右移一格才能减少一个零

class Solution:
	def longestOnes(self, A, K):
		left, right = 0, 0
		res = 0
		while right < len(A):
			if A[right] == 0:
				if K == 0:
					while A[left] == 1:
						left += 1
					left += 1
				else:
					K -= 1
			res = max(res, right-left+1)
			right += 1
			
		return res
