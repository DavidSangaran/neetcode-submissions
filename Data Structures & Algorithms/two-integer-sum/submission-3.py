class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}
        for index,value in enumerate(nums):
            remainder = target - value
            if remainder in prevDict:
                return [prevDict[remainder], index]
            prevDict[value] = index