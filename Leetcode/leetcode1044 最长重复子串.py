'''
Author: Puffrora
Date: 2020-10-26 09:11:03
LastModifiedBy: Puffrora
LastEditTime: 2020-10-26 12:51:07
'''


class Solution:
    def longestDupSubstring(self, S):

        import functools
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1
        n = len(S)

        # s1s2s3...sn will be encoded as a^(n-1)*s1 + a^(n-2)*s2 + ... + a^0*sn
        # 用来检测 S 中是否有长度为 length 的重复串
        def Rabin_Karp(l):
            p = pow(26, l, mod)
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:l])
            appeared = {cur}
            for index in range(l, n):
                cur = (cur * 26 + A[index] - A[index-l] * p) % mod
                if cur in appeared: return index - l + 1
                appeared.add(cur)

            return -1

        left, right = 0, n
        res = 0
        while left < right:
            mid = (left + right + 1) // 2
            pos = Rabin_Karp(mid)
            if pos != -1:
                left = mid
                res = pos
            else:
                right = mid - 1

        return S[res:res+left]



