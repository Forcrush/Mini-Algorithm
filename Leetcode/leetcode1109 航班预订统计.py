'''
Author: Puffrora
Date: 2020-12-09 08:36:28
LastModifiedBy: Puffrora
LastEditTime: 2020-12-09 08:48:56
'''


"""
前缀和
一种思路就是在 i 的位置 + k， 然后利用前缀和的技巧给 i 到 n 的元素都加上 k。
但是题目需要加的是一个区间， j + 1 及其之后的元素会被多加一个 k。一个简单的
技巧就是给 j + 1 的元素减去 k，这样正负就可以抵消。
"""
class Solution:
    def corpFlightBookings(self, bookings, n):

        prefix_sum = [0] * (n + 1)
        for i, j, k in bookings:
            prefix_sum[i-1] += k
            if j < n: prefix_sum[j] -= k
        
        for i in range(n+1):
            prefix_sum[i] += prefix_sum[i-1]
        
        return prefix_sum[:-1]

