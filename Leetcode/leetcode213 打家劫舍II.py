# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-09 10:03:04
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-09 10:46:27


'''
打家劫舍 的升级版，加入了一个限制条件：
第一间屋子和最后一间屋子不能同时被抢。即，要么抢第一间，要么抢最后一间。

因此，可以把问题拆分为两个基础版的 打家劫舍：

去掉第一间，打劫一次
去掉最后一间，打劫一次
取两次打劫能获得的最大值
'''
class Solution(object):
	def rob(self, nums):
		if nums == []:
			return 0
		if len(nums) == 1:
			return nums[0]
		def basicrob(array):
			dp = [0] * (len(array) + 1)
			dp[1] = array[0]
			for i in range(2, len(array)+1):
				dp[i] = max(array[i-1] + dp[i-2], dp[i-1])
			return dp[-1]

		return max(basicrob(nums[1:]), basicrob(nums[:-1]))