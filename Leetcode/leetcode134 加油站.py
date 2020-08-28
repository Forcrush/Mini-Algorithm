# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 13:51:09
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 17:47:27


class Solution:
	def canCompleteCircuit(self, gas, cost):

		total_tank, cur_tank = 0, 0
		start = 0
		for i in range(len(gas)):
			total_tank += gas[i] - cost[i]
			cur_tank += gas[i] - cost[i]
			if cur_tank < 0:
				cur_tank = 0
				start = i + 1

		return start if total_tank >= 0 else -1