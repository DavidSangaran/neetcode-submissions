class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {element: index for index, element in enumerate(nums)}
        return len(nums) > len(hashmap)