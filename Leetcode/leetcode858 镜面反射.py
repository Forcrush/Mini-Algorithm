'''
Author: Puffrora
Date: 2020-10-16 21:18:35
LastModifiedBy: Puffrora
LastEditTime: 2020-10-17 01:11:53
'''


"""
我们需要找到最小的 k 使得 kq 是 p 的倍数
并且根据 k 的奇偶性可以得知光线到达了左侧还是右侧
根据 kq / p 的奇偶性可以得知光线到达了上方还是下方，从而得知光线到达的接收器的编号

显然，设 g = gcd(p, q) 为 p 和 q 的最大公约数，那么 s = pq / gcd(p, q) 是最小的同时整除 p 和 q 的数，
即 p 和 q 的最小公倍数。因此 k 的值为 s / q = p / gcd(p, q)

"""
class Solution:
    def mirrorReflection(self, p, q):
        
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)

        k = p / gcd(p, q)

        lr = k % 2
        ud = (k * q / p) % 2

        if lr == 1 and ud == 1:
            return 1
        elif lr == 0 and ud == 1:
            return 2
        elif lr == 1 and ud == 0:
            return 0