class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                k += 1
            else:
                j = i
                while j < len(nums)-1 and nums[j] == val:
                    j += 1
                if nums[i] != nums[j]:
                    nums[i] = nums[j]
                    k += 1
                nums[j] = val
            i += 1
        return k