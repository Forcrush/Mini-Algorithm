'''
Author: Puffrora
Date: 2020-10-16 20:42:38
LastModifiedBy: Puffrora
LastEditTime: 2020-10-16 20:50:02
'''


# ! 当 K == 1 时， 只能循环移动每个元素，无法改变相对位置。因此只需要获取循环移动过程中字典序最小的序列
# ! 当 K > 1 时， 可以生成当前字符串的任意序列。因此将原字符串排序生成字典序最小的序列
class Solution:
    def orderlyQueue(self, S, K):
        if K == 1:
            return min(S[i:]+S[:i] for i in range(len(S)))
        return "".join(sorted(list(S)))
