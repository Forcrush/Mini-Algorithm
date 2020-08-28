# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-24 09:31:15
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-24 09:59:27

'''
Fisher-Yates Shuffle算法

最早提出这个洗牌方法的是 Ronald A. Fisher 和 Frank Yates，即 Fisher–Yates Shuffle，
其基本思想就是从原始数组中随机取一个之前没取过的数字到新的数组中，具体如下：

1 初始化原始数组和新数组，原始数组长度为n(已知)；

2 从还没处理的数组（假如还剩k个）中，随机产生一个[0, k)之间的数字p（假设数组从0开始）；

3 从剩下的k个数中把第p个数取出；

4 重复步骤2和3直到数字全部取完；

5 从步骤3取出的数字序列便是一个打乱了的数列


Knuth-Durstenfeld Shuffle算法

Knuth 和 Durstenfeld 在Fisher 等人的基础上对算法进行了改进，在原始数组上对数字进行交互，
省去了额外O(n)的空间。 该算法的基本思想和 Fisher 类似，每次从未处理的数据中随机取出一个数字，
然后把该数字放在数组的尾部，即数组尾部存放的是已经处理过的数字。

'''
class Solution:

	def __init__(self, nums):
		self.array = nums
		self.original = nums[:]

	def reset(self):
		"""
		Resets the array to its original configuration and return it.
		"""
		self.array = self.original[:]
		return self.array


	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		"""
		import random
		for i in range(len(self.array)-1, 0, -1):
			index = random.randrange(0, i+1)
			self.array[i], self.array[index] = self.array[index], self.array[i]

		return self.array



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()