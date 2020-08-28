# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-11 22:41:00
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-10 21:22:25


# 详细解法 https://charlesliuyx.github.io

"""
令楼高为 h, 剩下 m 个鸡蛋时的最少尝试步数 f(h, m)
在第 k 层扔下1个鸡蛋碎了后的最少尝试步数 f(k-1, m-1)
在第 k 层扔下1个鸡蛋没碎后的最少尝试步数 f(h-k, m)

f(h, m) =  min  (max(f(k-1, m-1), f(h-k, m)) + 1)
		 1<=k<=h
"""


# K 鸡蛋数
# N 楼层数


# 基础版本
# 时间复杂度 O(K*N*N)
# 空间复杂度 O(K*N)
class Solution1:
	def superEggDrop(self, K, N):

		dp = [[i for i in range(N+1)] for j in range(K+1)]

		# i=1 的情况就是 [i for i in range(N+1)]
		for i in range(2, K+1):
			for j in range(1, N+1):
				for c in range(1, j):
					dp[i][j] = min(dp[i][j], max(dp[i-1][c-1], dp[i][j-c]) + 1)

		return dp[K][N]


# 空间优化版本
# 时间复杂度 O(K*N*N)
# 空间复杂度 O(N)
class Solution2:
	def superEggDrop(self, K, N):

		dp_pre = [i for i in range(N+1)]
		dp_cur = [i for i in range(N+1)]

		# i=1 的情况就是 [i for i in range(N+1)]
		for i in range(2, K+1):
			for j in range(1, N+1):
				for c in range(1, j):
					dp_cur[j] = min(dp_cur[j], max(dp_pre[c-1], dp_cur[j-c]) + 1)
			dp_pre = dp_cur[:]
		return dp_cur[N]


# 下界优化版本
# 时间复杂度 O(K*N*log(N))
# 空间复杂度 O(N)
class Solution3:
	def superEggDrop(self, K, N):
		import math
		dp_pre = [i for i in range(N+1)]
		dp_cur = [i for i in range(N+1)]

		# i=1 的情况就是 [i for i in range(N+1)]
		for i in range(2, K+1):
			for j in range(1, N+1):
				t = math.ceil(math.log2(j+1))
				if i >= t:
					dp_cur[j] = t
				else:
					for c in range(1, j):
						dp_cur[j] = min(dp_cur[j], max(dp_pre[c-1], dp_cur[j-c]) + 1)
			dp_pre = dp_cur[:]
		return dp_cur[N]


# 决策单调性 二分查找 版本
# 时间复杂度 O(K*N*log(N))
# 空间复杂度 O(N)
class Solution4:
	def superEggDrop(self, K, N):
		import math
		t = math.floor(math.log2(N)) + 1
		if K >= t: return t
		else:
			dp_cur = [i for i in range(N+1)]
			dp_pre = [i for i in range(N+1)]

			for i in range(2, K+1):
				dp_cur[0] = 0
				for j in range(1, N+1):
					dp_cur[j] = 1000000
					start, stop = 1, j
					# 二分查找
					while start <= stop:
						mid = (start + stop) // 2
						if dp_pre[mid - 1] > dp_cur[j - mid]:
							if dp_pre[mid - 1] + 1 < dp_cur[j]:
								dp_cur[j] = dp_pre[mid - 1] + 1
							stop = mid - 1
						elif dp_pre[mid - 1] < dp_cur[ j - mid]:
							if dp_cur[j - mid] + 1 < dp_cur[j]:
								dp_cur[j] = dp_cur[j - mid] + 1
							start = mid + 1
						else:
							dp_cur[j] = dp_cur[j - mid] + 1
							break
				dp_pre = dp_cur[:]
			return dp_cur[N]


# 决策单调性优化版本
# 时间复杂度 O(K*N)
# 空间复杂度 O(N)
class Solution5:
	def superEggDrop(self, K, N):
		import math
		t = math.floor(math.log2(N)) + 1
		if K >= t: return t
		else:
			dp_cur = [i for i in range(N+1)]
			dp_pre = [i for i in range(N+1)]

			for i in range(2, K+1):
				x = 1
				for j in range(1, N+1):
					while x < j and max(dp_pre[x-1], dp_cur[j-x]) >= max(dp_pre[x], dp_cur[j-x-1]):
						x += 1
					dp_cur[j] = max(dp_pre[x-1], dp_cur[j-x]) + 1

				dp_pre = dp_cur[:]

			return dp_cur[N]


# 改变对问题的状态描述方法，用 h(i,j) 表示用 j 个鸡蛋尝试 i 次在最坏情况下能找到的最小尝试次数的楼高
# 状态转移方程 h(i, j) = h(i-1, j) + h(i-1, i-1) + 1
# nm就离谱优化 https://www.zhihu.com/question/19690210
# 时间复杂度 O(N^0.5)
# 空间复杂度 O(K)
class Solution6:
	def superEggDrop(self, K, N):
		import math
		if K < 1 and N < 1: return 0
		if K == 1: return N
		t = math.floor(math.log2(N)) + 1
		if K >= N:
			return t
		else:
			g = [1 for _ in range(K+1)]
			g[0] = 0
			if g[K] >= N: return 1
			elif N == 1: return N
			else:
				for i in range(2, N+1):
					for j in range(K, -1, -1):
						g[j] = g[j-1] + g[j] + 1
						if j == K and g[j] >= N:
							return i
					g[1] = i
					if K == 1 and g[1] >= N:
						return i	
k = 2
m = 200
print(Solution1().superEggDrop(k,m))
print(Solution2().superEggDrop(k,m))
print(Solution3().superEggDrop(k,m))
print(Solution4().superEggDrop(k,m))
print(Solution5().superEggDrop(k,m))
print(Solution6().superEggDrop(k,m))