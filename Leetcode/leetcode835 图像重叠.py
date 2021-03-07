'''
Author: Puffrora
Date: 2021-03-06 17:03:17
LastModifiedBy: Puffrora
LastEditTime: 2021-03-06 17:25:24
'''


from scipy.signal import correlate2d
import numpy as np
from typing import List


# 枚举偏移量
# 时间复杂度 O(N^4)
# 空间复杂度 O(N^2)
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        from collections import defaultdict

        bias_set = defaultdict(int)

        for r1, row1 in enumerate(img1):
            for c1, v1 in enumerate(row1):
                if v1:
                    for r2, row2 in enumerate(img2):
                        for c2, v2 in enumerate(row2):
                            if v2:
                                bias = (r2-r1, c2-c1)
                                bias_set[bias] += 1

        return max(bias_set.values()) if bias_set else 0


# FFT 卷积
# 时间复杂度 O(N*N*logN)
class Solution1:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        N2 = 1 << (N.bit_length() + 1)
        img1_fft = np.fft.fft2(np.array(img1), (N2, N2))
        img2_fft = np.fft.fft2(np.array(img2)[::-1, ::-1], (N2, N2))
        img1_fft *= img2_fft
        conv = np.fft.ifft2(img1_fft)
        return int(np.round(np.max(conv)))


# 卷积
class Solution2:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        return correlate2d(A, B).max()

