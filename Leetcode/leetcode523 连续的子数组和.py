'''
Author: Puffrora
Date: 2020-10-08 18:26:44
LastModifiedBy: Puffrora
LastEditTime: 2020-10-08 18:41:57
'''


# 时间复杂度 O(N)
# 空间复杂度 O(min(N, k))
# 利用哈希取模加速
class Solution:
    def checkSubarraySum(self, nums, k):

        cur_sum = 0
        dic = {0: -1}
        for i, n in enumerate(nums):
            cur_sum += n

            if k != 0:
                cur_sum %= k
            
            if cur_sum in dic:
                if i - dic[cur_sum] > 1:
                    return True
            else:
                dic[cur_sum] = i
        
        return False


