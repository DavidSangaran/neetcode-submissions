class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {key : value for value, key in enumerate(nums)}
        return len(nums) > len(dictionary)