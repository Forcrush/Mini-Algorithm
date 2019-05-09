# 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights == []:
            return 0
        stack = []
        maxarea = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack != [] and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                if stack == []:
                    maxarea = max(maxarea, heights[top]*i)
                else:
                    maxarea = max(maxarea, heights[top]*(i-stack[-1]-1))
            stack.append(i)
        return maxarea