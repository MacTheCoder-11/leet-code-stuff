class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
         m = {}
         for i, x in enumerate(nums):
            y = target - x
            if y in m:
                return [m[y], i]
            m[x] = i
