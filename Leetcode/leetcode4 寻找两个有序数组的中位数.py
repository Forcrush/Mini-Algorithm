# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-12 16:35:08
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-12 19:25:37


# 时间复杂度 O(log(min(len(nums1), len(nums2))))
# 空间复杂度 O(1)
class Solution:
	def findMedianSortedArrays(self, nums1, nums2):

		# 保证在较短的数组切分
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

		imin, imax = 0, len(nums1)
		while imin <= imax:
			# i j 为在两个数组的切分位置
			# 满足如下关系:
			# 1. i + j = len(nums1) - i + len(nums2) - j + (1) 
			# 2. median = (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) // 2 
			# 可用 i 去确定 j
			i = (imin + imax) // 2
			# +1 是因为可能两数组合并后为奇数个元素数组 假设切分后左边比右边多一个元素
			j = (len(nums1) + len(nums2) + 1) // 2 - i

			# i 需要增加
			if j != 0 and i != len(nums1) and nums2[j-1] > nums1[i]:
				imin = i + 1

			# i 需要减少
			elif i != 0 and j != len(nums2) and nums1[i-1] > nums2[j]:
				imax = i - 1

			# 满足第二个关系 但需要考虑边界
			else:
				maxleft = 0
				if i == 0:
					maxleft = nums2[j-1]
				elif j == 0:
					maxleft = nums1[i-1]
				else:
					maxleft = max(nums1[i-1], nums2[j-1])
				# 奇数情况 不需要考虑右边
				if (len(nums1) + len(nums2)) % 2 == 1:
					return maxleft

				minright = 0
				if i == len(nums1):
					minright = nums2[j]
				elif j == len(nums2):
					minright = nums1[i]
				else:
					minright = min(nums1[i], nums2[j])

				return (maxleft + minright) / 2



# 时间复杂度 O(log(len(nums1) + len(nums2)))
# 空间复杂度 O(1)
# 可看成在两个有序数组中找第 (len(nums1) + len(nums2)) // 2 大的数
class Solution2:
	def findMedianSortedArrays(self, nums1, nums2):
		m, n = len(nums1), len(nums2)
		left, right = (m + n + 1) // 2, (m + n + 2) // 2

		def getKth(nums1, start1, end1, nums2, start2, end2, k):
			len1, len2 = end1 - start1 + 1, end2 - start2 + 1
			# 让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1 
			if len1 > len2:
				return getKth(nums2, start2, end2, nums1, start1, end1, k)
			if len1 == 0:
				return nums2[start2+k-1]

			if k == 1:
				return min(nums1[start1], nums2[start2])

			i = start1 + min(len1, k//2) - 1
			j = start2 + min(len2, k//2) - 1
			if nums1[i] > nums2[j]:
				return getKth(nums1, start1, end1, nums2, j+1, end2, k-(j-start2+1))
			else:
				return getKth(nums1, i+1, end1, nums2, start2, end2, k-(i-start1+1))

		# 将偶数和奇数的情况合并 如果是奇数 会求两次同样的 k
		return (getKth(nums1, 0, m-1, nums2, 0, n-1, left) + getKth(nums1, 0, m-1, nums2, 0, n-1, right)) / 2

