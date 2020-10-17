'''
Author: Puffrora
Date: 2020-10-13 18:24:20
LastModifiedBy: Puffrora
LastEditTime: 2020-10-13 20:23:48
'''


"""
黑名单映射
注意题目假设 黑名单长度 << 白名单长度
基本思想是：设总名单长度为N，黑名单长度为blen，则白名单长度为 N-blen。黑名单分散在总名单的各个位置，有的分布在[0,N-blen)，有的则分布在[N-blen,N)。
首先我们生成[0,N-blen)中的随机数，那么：

对于分布在[N-blen,N)中的黑名单成员，不用管它们，因为生成的随机数达不到这个范围。
对于分布在[0,N-blen)中的黑名单成员，完全有可能碰撞到它们。为他们建立一一映射，映射到[N-blen,N)范围内的白名单成员中去，一旦发生碰撞则映射一次。

"""
class Solution:

    import random

    def __init__(self, N, blacklist):
        mapping_pos = N - len(blacklist)
        threshold = mapping_pos
        mapping_dict = {}

        # 先将大于阈值的黑名单数映射到自身
        for b in blacklist:
            if b >= threshold:
                mapping_dict[b] = b
        # 再将小于阈值的黑名单数映射到大于阈值的白名单数
        for b in blacklist:
            if b < threshold:
                while mapping_pos in mapping_dict:
                    mapping_pos += 1
                mapping_dict[b] = mapping_pos
                mapping_pos += 1
        self.threshold = threshold
        self.mapping_dict = mapping_dict

    def pick(self):
        randnum = random.randint(0, self.threshold-1)
        if randnum in self.mapping_dict:
            return self.mapping_dict[randnum]
        else:
            return randnum
            
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(N, blacklist)
    # param_1 = obj.pick()
