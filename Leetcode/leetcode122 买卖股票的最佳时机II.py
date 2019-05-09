# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-08 00:08:00
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-08 00:16:45


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        profits = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profits += prices[i] - prices[i-1]
        return profits

        