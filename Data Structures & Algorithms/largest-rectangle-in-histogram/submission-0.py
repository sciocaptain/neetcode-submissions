class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_height = 0
        stack = []

        for i,height in enumerate(heights):
            left_index = i
            while (stack and height < stack[-1][1]):
                left_index, stack_height = stack.pop()
                max_height = max(stack_height * (i - left_index), max_height)
            stack.append((left_index, height))

        while stack:
            stack_i, stack_height = stack.pop()
            max_height = max(stack_height * (len(heights) - stack_i), max_height)

        return max_height


            
