class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Dictionary with number: count

        # Go left<-pick any number in nums-> Go right

        # (3,2,4)

        visited = set()
        sequence = set(nums)
        max_count = 0

        for num in nums:
            count = 1
            base = num
            if num in visited:
                continue
            while (base - 1) in sequence:
                count += 1
                base -= 1
                visited.add(base)

            base = num
            while (base + 1) in sequence:
                count += 1
                base += 1
                visited.add(base)

            max_count = max(max_count, count)
            visited.add(num)
        
        return max_count

