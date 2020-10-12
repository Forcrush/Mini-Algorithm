'''
Author: Puffrora
Date: 2020-10-08 22:45:09
LastModifiedBy: Puffrora
LastEditTime: 2020-10-08 22:57:41
'''


# 单调栈
class Solution:
    def nextGreaterElement(self, nums1, nums2):

        if not nums2: return []
        
        mono_stack = [nums2[0]]
        dic = {}
        for i in range(1, len(nums2)):
            if mono_stack[-1] > nums2[i]:
                mono_stack.append(nums2[i])
            else:
                while mono_stack and mono_stack[-1] < nums2[i]:
                    dic[mono_stack.pop()] = nums2[i]
                mono_stack.append(nums2[i])
        while mono_stack:
            dic[mono_stack.pop()] = -1
        
        res = []
        for i in nums1:
            res.append(dic[i])

        return res