class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Option 1
        # create dictionary and then sort
        # time complexity is nlogn

        # Option 2
        # Create dictionary
        # Create buckets
        # go through buckets backwards

        d = Counter(nums)
        buckets = [[] for i in range(0, len(nums) + 1)]

        for key,value in d.items():
            buckets[value].append(key)
        
        res = []
        for bucket in buckets[::-1]:
            if k > 0:
                res.extend(bucket)
                k -= len(bucket)
        return res
            

        