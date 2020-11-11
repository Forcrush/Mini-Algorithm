'''
Author: Puffrora
Date: 2020-11-11 22:14:57
LastModifiedBy: Puffrora
LastEditTime: 2020-11-11 22:30:44
'''

"""
假设我们在数组 B 中放了 K 个数，数组 C 中放了 N - K 个数，它们的平均值相等，
即 sum(B) / K = sum(C) / (N - K)，那么有
sum(B) * (N - K) = sum(C) * K
== > sum(B) * N = (sum(B) + sum(C)) * K
== > sum(B) / K = (sum(B) + sum(C)) / N
== > sum(B) / K = sum(A) / N
即 B 的平均值与 A 的平均值相等。因此我们可以将 A 中的每个元素减去它们的平均值，
这样 A 的平均值变为 0。 此时我们的问题变成：找出若干个元素组成集合 B，这些元素的和为 0。

一个容易想到的思路是，N 个元素中取出若干个有 2 ^ N 种方法（即每个元素取或不取），
我们依次判断每种方法选出的元素之和是否为 0。但题目中的 N 可以达到 30，2 ^ N 会非常大。
因此我们考虑将数组平均分成两部分 A0 和 A1，它们均含有 N/2 个元素（不失一般性，这里假设 N 为偶数。
如果 N 为奇数，在 A0 中多放一个元素即可），此时这两个数组分别有 2 ^ (N/2) 种选择的方法。
设 A0 中所有选择的方法得到的元素之和的集合为 left，A1 中所有选择的方法得到的元素之和的集合为 right，
那么我们只需要在 left 中找出一个 x，使得 right 中包含 - x，那么就找到了一种和为 0 的方法。
需要注意的是，我们不能同时选择 A0 和 A1 中的所有元素，这样 C 就为空了。

此外，“将 A 中每个元素减去它们的平均值” 这一步会引入浮点数，可能会导致判断的时候出现误差。
一种解决方案是使用分数代替浮点数，但这样代码编写起来较为麻烦。更好的解决方案是先将 A 中的
每个元素乘以 A 的长度，这样它们的平均值一定为整数。
"""
# 折半搜索
# 时间复杂度：O(2^(N/2))，其中 N 是数组 A 的长度
# 空间复杂度：O(2^(N/2))
class Solution:
    def splitArraySameAverage(self, A):
        from fractions import Fraction
        N, S = len(A), sum(A)
        A = [z - Fraction(S, N) for z in A]

        if N == 1: return False

        # ! 计算左半部分所有可能的和
        left = {A[0]}
        for i in range(1, N//2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left:
            return True
        
        # ! 计算右半部分所有可能的和
        right = {A[-1]}
        for i in range(N//2, N-1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right:
            return True

        sleft = sum(A[i] for i in range(N//2))
        sright = sum(A[i] for i in range(N//2, N))

        return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)


# dfs
class Solution2:
   def splitArraySameAverage(self, A):

       # 有序数组 A 中是否存在从 begin 开始的 n 个数其和为 target 
       def dfs(A, begin, n, target):
           if n == 0:
               return target == 0
           if target < n * A[begin]:
               return False
           for i in range(begin, len(A) - n + 1):
               if i > begin and A[i] == A[i-1]:
                   continue
               if dfs(A, i+1, n-1, target-A[i]):
                   return True
           return False

       A.sort()
       n, s = len(A), sum(A)
       # ! i 代表 B/C 数组中元素个数
       for i in range(1, n//2+1):
           if s * i % n == 0 and dfs(A, 0, i, s * i // n):
               return True
       return False
