class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxAria =0
        stack =[]

        for i,h in enumerate(heights):
            start =i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                maxAria = max(maxAria, height*(i-index))
                start = index
            stack.append((start,h))

        for i,h in stack:
            maxAria = max(maxAria, h*(len(heights)-i))
        return maxAria


        