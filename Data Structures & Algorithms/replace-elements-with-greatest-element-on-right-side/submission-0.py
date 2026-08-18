class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1,-1):
            if arr[i] >= currMax:
                current = arr[i]
                arr[i] = currMax
                currMax = max(currMax, current)
            else:
                arr[i] = currMax
        return arr


