class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        for i in range(len(nums)):
            p = target-nums[i]
            if p in nums:
                a=nums.index(p)
                if a==i:
                    continue
                break
        return i,a

"""
The code uses one loop to iterate over the number and subtract from target and if that subtracted number is present in list then return the index of both number.
(here if condition of a==i means that possibly the target is 10 and present number in list might be [5,5] but it will return the same index so we need to skip)
"""
