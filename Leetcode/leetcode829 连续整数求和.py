'''
Author: Puffrora
Date: 2020-11-16 11:47:03
LastModifiedBy: Puffrora
LastEditTime: 2020-11-16 12:05:38
'''


"""
1个数时，必然有一个数可构成N
2个数若要构成N，第2个数与第1个数差为1，N减掉这个1能整除2则能由商与商+1构成N
3个数若要构成N，第2个数与第1个数差为1，第3个数与第1个数的差为2，N减掉1再减掉2能整除3则能由商、商+1与商+2构成N
依次内推，当商即第1个数小于等于0时结束

iteration: N - 1 - 2 - 3 - ... - k = 0
k(k+1)/2 = N
k = O(√N)
"""
# 时间复杂度 O(√N)
# 空间复杂度 O(1)
class Solution:
    def consecutiveNumbersSum(self, N):

        res, i = 0, 1
        while N > 0:
            res += (N % i == 0)
            N -= i
            i += 1
        
        return res
