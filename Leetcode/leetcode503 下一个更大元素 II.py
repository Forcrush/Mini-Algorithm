'''
Author: Puffrora
Date: 2020-10-08 22:57:51
LastModifiedBy: Puffrora
LastEditTime: 2020-10-08 23:18:11
'''


# 单调栈 同leetcode496
# 循环数组相当于遍历两次
class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []

        # (val, pos)
        mono_stack = [(nums[0], 0)]
        dic = {}
        for i in range(1, 2*len(nums)):
            if mono_stack[-1][0] >= nums[i % len(nums)]:
                mono_stack.append((nums[i % len(nums)], i % len(nums)))
            else:
                while mono_stack and mono_stack[-1][0] < nums[i % len(nums)]:
                    dic[mono_stack.pop()[1]] = nums[i % len(nums)]
                mono_stack.append((nums[i % len(nums)], i % len(nums)))

        while mono_stack:
            tmp = mono_stack.pop()[1]
            if tmp not in dic:
                dic[tmp] = -1 

        res = []
        for i in range(len(nums)):
            res.append(dic[i])

        return res


print(Solution().nextGreaterElements(
    [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]))
