class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = 0
        ans = []
        for i in range(0, n):
            res = target - nums[i]
            for j in range(i + 1, n):
                if nums[j] == res:
                    return [i, j]