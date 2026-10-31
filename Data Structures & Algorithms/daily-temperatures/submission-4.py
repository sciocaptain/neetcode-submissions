class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []  # Stores (temperature, accumulated_count)
        
        for t in temperatures[::-1]:
            count = 0
            while stack and stack[-1][0] <= t:
                popped_temp, popped_count = stack.pop()
                count += popped_count + 1
                
            if stack:
                res.append(count + 1)
            else:
                res.append(0)
                
            stack.append((t, count))
            
        return res[::-1]