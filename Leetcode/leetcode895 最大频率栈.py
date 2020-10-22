'''
Author: Puffrora
Date: 2020-10-22 17:46:56
LastModifiedBy: Puffrora
LastEditTime: 2020-10-22 18:03:42
'''


class FreqStack:

    def __init__(self):
        from collections import defaultdict
        # 记录每个数字的频率
        self.freq = defaultdict(int)
        # 记录每个频率下的数字
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        self.freq[x] += 1
        self.max_freq = max(self.max_freq, self.freq[x])
        self.group[self.freq[x]].append(x)

    def pop(self):
        top = self.group[self.max_freq].pop()
        self.freq[top] -= 1

        # 如果原最大频率下没有其他数字
        if not self.group[self.max_freq]:
            self.max_freq -= 1
            
        return top


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
