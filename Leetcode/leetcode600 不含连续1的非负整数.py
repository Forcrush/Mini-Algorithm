'''
Author: Puffrora
Date: 2020-10-11 20:24:39
LastModifiedBy: Puffrora
LastEditTime: 2020-10-11 22:16:45
'''


# 时间复杂度 O(x) x是返回的结果 即算法会遍历 x 这么多个数
# 空间复杂度 O(log(MAX_INT)) = O(32)
class Solution:
    def findIntegers(self, num):
        if num == 0: return 1
        if num == 1: return 2
        
        def generate(n):
            nonlocal cnt
            if n > num: return
            
            cnt += 1
            # 二进制最后一位是1 只能加0
            if n % 2 == 1:
                generate(n << 1)
            # 二进制最后一位是0 可以加0或1
            else:
                generate(n << 1)
                generate((n << 1) + 1)

        cnt = 0
        generate(1)

        # 0 没有被算进去
        return cnt + 1


# 时间复杂度 O(log(MAX_INT)) = O(32)
# 空间复杂度 O(1)
# https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/solution/xiang-xi-jie-shuo-jian-dan-ming-liao-jie-fa-by-sup/
class Solution:
    def findIntegers(self, num):
        num += 1  # 找比num+1小的符合条件的所有数字，这样包含了num
        prev, curr = 1, 1  # curr = f(0)，每次循环变为f(1), f(2)...
        res = 0
        while num:
            if num & 3 == 3:  # 如果是0b11结尾，清除之前结果
                res = 0
            if num & 1:  # 如果是0b1结尾，加上f()
                res += curr
            num >>= 1  # 右移一位
            prev, curr = curr, prev + curr  # 斐波那契额数列计算
        return res
