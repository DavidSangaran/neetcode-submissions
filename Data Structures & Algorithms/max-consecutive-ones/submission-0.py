class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            maxCount = count if count > maxCount else maxCount
        return maxCount