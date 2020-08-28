# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-24 21:08:14
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-24 21:59:36


# DFS
# TC O(xy) 状态数最多有(x+1)(y+1)种 x,y 分别为水壶容量
# SC O(xy) 哈希集最多储存状态数(x+1)(y+1)
class Solution:
	def canMeasureWater(self, x, y, z):
		if z > x + y: return False
		stack = [(0, 0)]
		visited = set()
		while stack:
			x_remain, y_remain = stack.pop()
			if x_remain == z or y_remain == z or x_remain + y_remain == z:
				return True
			if (x_remain, y_remain) in visited:
				continue

			visited.add((x_remain, y_remain))

			# 每种状态下有如下6种操作
			# 将 x 水壶灌满
			stack.append((x, y_remain))
			# 将 y 水壶灌满
			stack.append((x_remain, y))
			# 将 x 水壶倒空
			stack.append((0, y_remain))
			# 将 y 水壶倒空
			stack.append((x_remain, 0))
			# 将 y 水壶全部倒入 x 水壶直到倒空或灌满
			stack.append((min(x, x_remain+y_remain), max(0, y_remain-(x-x_remain))))
			# 将 x 水壶全部倒入 y 水壶直到倒空或灌满
			stack.append((max(0, x_remain-(y-y_remain)), min(y, x_remain+y_remain)))
		return False
		

'''
贝祖定理(裴蜀定理)
我们认为，每次操作只会让桶里的水总量增加 x，增加 y，减少 x，或者减少 y

首先要清楚，在题目所给的操作下，两个桶不可能同时有水且不满。因为观察所有题目中的操作，
操作的结果都至少有一个桶是空的或者满的；其次，对一个不满的桶加水是没有意义的。因为如
果另一个桶是空的，那么这个操作的结果等价于直接从初始状态给这个桶加满水；而如果另一个
桶是满的，那么这个操作的结果等价于从初始状态分别给两个桶加满；再次，把一个不满的桶里
面的水倒掉是没有意义的。因为如果另一个桶是空的，那么这个操作的结果等价于回到初始状态；
而如果另一个桶是满的，那么这个操作的结果等价于从初始状态直接给另一个桶倒满。因此，我
们可以认为每次操作只会给水的总量带来 x 或者 y 的变化量。

因此我们的目标可以改写成：找到一对整数 a, b，使得 ax + by = z

而只要满足 z <= x+y，且这样的 a, b 存在，那么我们的目标就是可以达成的。这是因为：

若 a ≥ 0,b ≥ 0，那么显然可以达成目标。

若 a < 0，那么可以进行以下操作：
往 y 壶倒水；
把 y 壶的水倒入 x 壶；
如果 y 壶不为空，那么 x 壶肯定是满的，把 x 壶倒空，然后再把 y 壶的水倒入 x 壶。
重复以上操作直至某一步时 x 壶进行了 a 次倒空操作，y 壶进行了 b 次倒水操作。

若 b < 0，方法同上，x 与 y 互换。

贝祖定理告诉我们，ax + by = z 有解当且仅当 z 是 x, y 的最大公约数的倍数
因此我们只需要找到 x, y 的最大公约数并判断 z 是否是它的倍数即可

TC O(log(min(x,y))) 取决于计算最大公约数所使用的辗转相除法
SC O(1)
'''
class Solution1:
	def canMeasureWater(self, x, y, z):
		if z > x+y: return False
		if x == 0 or y == 0: return z == 0 or z == x+y

		def gcd(a, b):
			if b == 0:
				return a
			return gcd(b, a%b)

		return z % gcd(x, y) == 0