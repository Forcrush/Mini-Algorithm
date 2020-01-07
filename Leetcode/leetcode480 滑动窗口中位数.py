# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-15 11:18:13
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-15 18:08:27


# 大小根堆
class Solution:
	def medianSlidingWindow(self, nums, k):

		import heapq

		# 第一个滑窗初始化
		# maxheap为小根堆 minheap为大根堆
		maxh, minh = [], []
		for i in range(k):
			heapq.heappush(maxh, -nums[i])
		# 若滑窗数组为奇数 则小根堆比大根堆多一个元素
		for _ in range(k//2):
			heapq.heappush(minh, -heapq.heappop(maxh))

		res = []
		# 储存离开滑窗的无效元素
		dic = {}
		# 此时从第k+1个元素开始
		pos = k
		while True:
			
			# 此时滑窗的中位数
			median = -maxh[0] if k % 2 == 1 else (-maxh[0] + minh[0]) / 2
			res.append(median)

			if pos == len(nums):
				break

			# 即将进入和离开滑窗的元素
			outnumber = nums[pos-k]
			innumber = nums[pos]

			# 平衡因子 判断两堆规模
			balance = 0

			# 处理离开元素
			balance += -1 if outnumber <= -maxh[0] else 1
			dic[outnumber] = dic.get(outnumber, 0) + 1

			# 处理进入元素
			if maxh and innumber <= -maxh[0]:
				balance += 1
				heapq.heappush(maxh, -innumber)
			else:
				balance -= 1
				heapq.heappush(minh, innumber)

			# 重平衡
			if balance < 0:
				heapq.heappush(maxh, -heapq.heappop(minh))
				# balance += 1
			if balance > 0:
				heapq.heappush(minh, -heapq.heappop(maxh))
				# balance -= 1

			# 删除之前离开滑窗的无效元素
			while maxh and dic.get(-maxh[0], None) != None:
				if dic[-maxh[0]] == 0:
					break
				else:
					dic[-maxh[0]] -= 1
					heapq.heappop(maxh)
			while minh and dic.get(minh[0], None) != None:
				if dic[minh[0]] == 0:
					break
				else:
					dic[minh[0]] -= 1
					heapq.heappop(minh)

			pos += 1
		
		return res


# 跟第一个解法一样用两个堆寻找中位数
# 但自己实现的大小根堆 push 操作效率远不如内置 heapq 
class Solution2:
	def medianSlidingWindow(self, nums, k):

		class maxheap():

			def __init__(self):
				self.heap = []

			def perlocate(self, heap, hole):
				tmp = heap[hole]
				child = hole * 2 + 1
				while child <= len(heap)-1:
					if child < len(heap)-1 and heap[child+1] > heap[child]:
						child += 1
					if heap[child] > tmp:
						heap[hole] = heap[child]
						hole = child
						child = 2 * hole + 1
					else:
						break
				heap[hole] = tmp

			def isempty(self):
				return False if self.heap else True

			def push(self, number):
				self.heap.append(number)
				for i in range(len(self.heap)//2-1, -1, -1):
					self.perlocate(self.heap, i)

			def top(self):
				return self.heap[0]

			def pop(self):
				if self.heap:
					tmp = self.heap[0]
					self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
					self.heap.pop()
					if self.heap:
						self.perlocate(self.heap, 0)
					return tmp

		class minheap():

			def __init__(self):
				self.heap = []

			def perlocate(self, heap, hole):
				tmp = heap[hole]
				child = hole * 2 + 1
				while child <= len(heap)-1:
					if child < len(heap)-1 and heap[child+1] < heap[child]:
						child += 1
					if heap[child] < tmp:
						heap[hole] = heap[child]
						hole = child
						child = 2 * hole + 1
					else:
						break
				heap[hole] = tmp

			def selforder(self):
				for i in range(len(self.heap)//2-1, -1, -1):
					self.perlocate(self.heap, i)

			def isempty(self):
				return False if self.heap else True

			def isempty(self):
				return False if self.heap else True

			def push(self, number):
				self.heap.append(number)
				for i in range(len(self.heap)//2-1, -1, -1):
					self.perlocate(self.heap, i)

			def top(self):
				return self.heap[0]

			def pop(self):
				if self.heap:
					tmp = self.heap[0]
					self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
					self.heap.pop()
					if self.heap:
						self.perlocate(self.heap, 0)
					return tmp

		# 第一个滑窗初始化
		# maxheap为小根堆 minheap为大根堆
		maxh, minh = maxheap(), minheap()
		for i in range(k):
			maxh.push(nums[i])
		# 若滑窗数组为奇数 则小根堆比大根堆多一个元素
		for _ in range(k//2):
			minh.push(maxh.pop())

		res = []
		# 储存离开滑窗的无效元素
		dic = {}
		# 此时从第k+1个元素开始
		pos = k
		while True:

			
			# 此时滑窗的中位数
			median = maxh.top() if k % 2 == 1 else (maxh.top() + minh.top()) / 2
			res.append(median)

			if pos == len(nums):
				break

			# 即将进入和离开滑窗的元素
			outnumber = nums[pos-k]
			innumber = nums[pos]

			# 平衡因子 判断两堆规模
			balance = 0

			# 处理离开元素
			balance += -1 if outnumber <= maxh.top() else 1
			dic[outnumber] = dic.get(outnumber, 0) + 1

			# 处理进入元素
			if not maxh.isempty() and innumber <= maxh.top():
				balance += 1
				maxh.push(innumber)
			else:
				balance -= 1
				minh.push(innumber)
			# 重平衡
			if balance < 0:
				maxh.push(minh.pop())
				# balance += 1
			if balance > 0:
				minh.push(maxh.pop())
				# balance -= 1
			# 删除之前离开滑窗的无效元素
			while not maxh.isempty() and dic.get(maxh.top(), None) != None:
				if dic[maxh.top()] == 0:
					break
				else:
					dic[maxh.top()] -= 1
					maxh.pop()
			while not minh.isempty() and dic.get(minh.top(), None) != None:
				if dic[minh.top()] == 0:
					break
				else:
					dic[minh.top()] -= 1
					minh.pop()

			pos += 1
		print(res)
		return res

