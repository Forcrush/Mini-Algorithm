# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 21:08:07
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-12 14:45:57


# 小根堆法(维持一个大小为k的最小堆 最后的堆顶元素即第k大元素)
# Time Complexity: O(k+(n-k)logk) ~ O(nlogk)
class Min_Heap:
	def findKthLargest(self, nums, k):
		heap = [0] * k
		for i in range(k):
			heap[i] = nums[i]
		for i in range(len(heap)//2-1, -1, -1):
			self.percolate(heap, i, len(heap)-1)

		for j in range(k, len(nums)):
			if nums[j] > heap[0]:
				heap[0] = nums[j]
				self.percolate(heap, 0, len(heap)-1)

		return heap[0]


	def percolate(self, array, hole, end):
		tmp = array[hole]
		child = 2 * hole + 1
		while child <= end:
			if child < end and array[child] > array[child+1]:
				child += 1
			if array[child] < tmp:
				array[hole] = array[child]
				hole = child
				child = 2 * hole + 1
			else:
				break
		array[hole] = tmp


# 快速排序(随机选择)
# Time Complexity: O(n) -- 因为这个思想属于减治法 只需去解决一个分支
# 即期望的时间复杂度为 O(n) + O(n/2) + O(n/4) + O(n/8) + ... < 2*O(n) ~ O(n)
import random


class Random_Quicksort:
	def findKthLargest(self, nums, k):

		# ！！！
		# 存在分歧 即重复元素是否有效 若前k大元素中可以包含重复元素则不用去重 反之则需要
		# nums = list(set(nums))


		def random_divide(array, low, high):
			# 随机选取将要放置的数
			rand = random.randint(low, high)
			array[rand], array[low] = array[low], array[rand]

			tmp = array[low]
			while low != high:
				while low < high and array[high] > tmp:
					high -= 1
				if low < high:
					array[low] = array[high]
					low += 1
				while low < high and array[low] < tmp:
					low += 1
				if low < high:
					array[high] = array[low]
					high -= 1
			array[low] = tmp
			return low


		def quicksort(array, low, high):
			if low >= high:
				return 
			mid = random_divide(array, low, high)
			if mid == len(array) - k:
				return array[mid]
			elif mid > len(array) - k:
				return quicksort(array, low, mid-1)
			else:
				return quicksort(array, mid+1, high)

		quicksort(nums, 0, len(nums)-1)

		return nums[len(nums)-k]


# BFPRT算法
# 选取主元；
# 1. 将 n 个元素按顺序分为 n/5 个组，每组 5 个元素，若有剩余，舍去
# 2. 对于这 n/5 个组中的每一组使用插入排序找到它们各自的中位数
# 3. 对于 2 中找到的所有中位数，调用 BFPRT 算法求出它们的中位数，作为主元
# 4. 以 3 选取的主元为分界点，把小于主元的放在左边，大于主元的放在右边
# 5. 判断主元的位置与 k 的大小，有选择的对左边或右边递归

# Time Complexity: T(n) = T(n/5) + T(7n/10) + c*O(n) ==> T(n) = O(n)
# T(n/5) 来自 1，n 个元素 5 个一组，共有 n/5 个中位数；
# T(7n/10) 来自 BFPRT()，在 n/5 个中位数中，主元 x 大于其中 n/5 * 1/2 = n/10 个中位数，
# 而每个中位数在其本来的 5 个数的小组中又大于或等于其中的 3 个数，所以主元 x 至少大于所有数中的 3n/10 个
# 即划分之后，任意一边的长度至少为 3/10 ，在最坏情况下，每次选择都选到了 7/10 的那一部分。
# O(n) 来自其它操作，比如插入排序里所需的一些额外操作 (对每个数组最坏情况为O(5**2)，即O(n/5)*O(5**2) ~ O(n))

class BFPRT:
	def findKthLargest(self, nums, k):


		def insertsort(array, left, right):
			for i in range(left+1, right+1):
				tmp = array[i]
				j = i - 1
				while j >= left and array[j] > tmp:
					array[j+1] = array[j]
					j -= 1
				array[j+1] = tmp
			return left + ((right - left) >> 1)


		def GetPivotIndex(array, left, right):
			if right - left < 5:
				return insertsort(array, left, right)
			sub_right = left

			# 每五个作为一组，求出中位数，并把这些中位数全部依次移动到数组左边
			for i in range(left, right-3, 5):
				index = insertsort(array, i, i+4)
				array[index], array[sub_right] = array[sub_right], array[index]
				sub_right += 1

			# 利用 BFPRT 得到这些中位数的中位数下标 即主元下标
			return BFPRT(array, left, sub_right)


		def partition(array, left, right, pivot_index):
			# 把主元放置于末尾
			array[pivot_index], array[right] = array[right], array[pivot_index]
			# 跟踪划分的分界线
			partition_index = left
			for i in range(left, right):
				# 比主元小的都放在左侧
				if array[i] < array[right]:
					array[partition_index], array[i] = array[i], array[partition_index]
					partition_index += 1
			array[partition_index], array[right] = array[right], array[partition_index]
			return partition_index


		# 返回数组 array[left, right] 的第 k 大数的下标
		def BFPRT(array, left, right):
			# 得到中位数的中位数下标（即主元下标）
			pivot_index = GetPivotIndex(array, left, right)
			# 进行划分，返回划分边界
			partition_index = partition(array, left, right, pivot_index)

			if partition_index == len(array)-k:
				return partition_index
			elif partition_index > len(array)-k:
				return BFPRT(array, left, partition_index - 1)
			else:
				return BFPRT(array, partition_index + 1, right)
        
		return nums[BFPRT(nums, 0, len(nums)-1)]


'''
print(Min_Heap().findKthLargest([3, 2, 4, 6, 1, 5, 5, 8], 3))
print(Random_Quicksort().findKthLargest([3, 2, 4, 6, 1, 5, 5, 8], 3))
print(BFPRT().findKthLargest([3, 2, 4, 6, 1, 5, 5, 8], 3))
'''