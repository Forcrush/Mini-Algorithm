'''
Author: Puffrora
Date: 2021-01-26 16:35:59
LastModifiedBy: Puffrora
LastEditTime: 2021-01-26 18:14:01
'''


"""
四种情况
1. [a, a, a, a, a] 全是同一个数字
2. [a, b, c, d, e] 全是不同数字 每种只出现一次
3. [a, a, b, b, c, c, d, d, d] 只有一种数字出现 n+1 次 其他数字都出现 n 次
4. [a, a, b, b, c, c, d] 只有一种数字出现 1 次 其他数字都出现 n 次
"""
class Solution:
    def maxEqualFreq(self, nums):

        # num[i] 记录数字 i 出现次数, i 代表数字
        # freq[i] 记录出现了 i 次的数字有多少个, i 代表频率
        num, freq = [0] * (max(nums) + 1), [0] * (len(nums) + 1)

        # 当前最大频率
        max_freq = 0
        res = 0

        for i, n in enumerate(nums):
            num[n] += 1
            freq[num[n]] += 1
            # 当某个频率出现一次以上 需要消去之前较低的频率记录 避免之后重复计数
            freq[num[n]-1] -= num[n] > 1
            max_freq = max(max_freq, num[n])
            if max_freq == i+1 or max_freq == 1 or max_freq+freq[max_freq-1]*(max_freq-1) == i+1 or freq[max_freq]*(max_freq)+1 == i+1:
                res = max(res, i+1)

        return res

