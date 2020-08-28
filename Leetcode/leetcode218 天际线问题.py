# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-11 18:37:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-11 23:35:41


# 扫描线法
# 注意高度相同的两楼右边界跟左边界重合情况 即对于同一横坐标的左端点跟右端点
# 先处理左端点 (入栈) 后处理右端点 (出栈) 
class Solution:
	def getSkyline(self, buildings):

		import heapq as hq

		points = []
		for item in buildings:
			# 左端点 高度值变负数以区分
			points.append([item[0], -item[2]])
			# 右端点 
			points.append([item[1], item[2]])

		# 按左端点排序
		points.sort()

		# 记录当前所有有效高度的堆
		height = []
		# 保存上一个位置的横坐标以及高度
		last = [0, 0]
		# 记录已经被移除的高度 因为heapq堆不能移除指定元素
		remove = {}
		# 保存结果
		res = []
		
		for p in points:
			# 左端点 高度入栈
			if p[1] < 0:
				hq.heappush(height, p[1])
			# 右端点 高度应该出栈
			else:
				# 移除这个高度 先存在remove字典里
				remove[-p[1]] = remove.get(-p[1], 0) + 1

			# 栈顶元素即当前最大高度已经被移除 则需要弹出
			while height:
				if height[0] in remove and remove[height[0]] > 0:
					remove[height[0]] -= 1
					hq.heappop(height)
				else:
					break
			
			# 当前有效最大高度
			maxh = abs(height[0]) if height else 0

			# 当前最大高度如果不同于上一个转折点高度，说明这是一个转折点
			if last[1] != maxh:
				last[0] = p[0]
				last[1] = maxh
				res.append([p[0], maxh])

		return res

# print(Solution().getSkyline([[0,2,3],[2,5,3],[5,7,3]]))