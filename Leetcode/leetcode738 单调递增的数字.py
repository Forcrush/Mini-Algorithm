'''
Author: Puffrora
Date: 2020-10-12 14:34:56
LastModifiedBy: Puffrora
LastEditTime: 2020-10-12 14:59:41
'''


class Solution:
    def monotoneIncreasingDigits(self, N):
        if N < 10: return N

        s = list(str(N))

        for i in range(1, len(s)):
            if int(s[i]) < int(s[i-1]):
                j = i - 1
                tmp = s[j]
                while j > 0:
                    if s[j-1] == s[j]:
                        j -= 1
                    else:
                        break
                s[j] = str(int(s[j]) - 1)
                for k in range(j+1, len(s)):
                    s[k] = '9'
                
                return int(''.join(s))
                
        # 原数字本来就是递增的
        return N
        