'''
Author: Puffrora
Date: 2020-12-09 17:30:40
LastModifiedBy: Puffrora
LastEditTime: 2020-12-21 16:18:37
'''


class Solution:
    def findTheLongestSubstring(self, s):

        status_dic = {}

        status, res = 0, 0
        status_dic[status] = 0

        for i, c in enumerate(s):
            if c == 'a':
                status ^= 1 << 4
            elif c == 'e':
                status ^= 1 << 3
            elif c == 'i':
                status ^= 1 << 2
            elif c == 'o':
                status ^= 1 << 1
            elif c == 'u':
                status ^= 1 << 0

            if status in status_dic:
                res = max(res, i+1-status_dic[status])
            else:
                status_dic[status] = i+1
        return res


