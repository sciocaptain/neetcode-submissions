class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        [30,38,30,36,35,40,28]
        [0,0,0,0,0,0,0]
        [(30,0), ]

        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((t, i))
        return res
                