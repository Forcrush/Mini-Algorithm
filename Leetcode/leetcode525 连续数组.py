'''
Author: Puffrora
Date: 2020-10-08 16:50:27
LastModifiedBy: Puffrora
LastEditTime: 2020-10-08 18:06:04
'''


# 时间复杂度 O(N)
# 空间复杂度 O(N)
class Solution:
    def findMaxLength(self, nums):
        dic = {0: -1}
        cur_val = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_val -= 1
            else:
                cur_val += 1
            if cur_val in dic:
                res = max(res, i - dic[cur_val])
            else:
                dic[cur_val] = i

        return res
