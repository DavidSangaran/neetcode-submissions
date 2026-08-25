class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        eucl = lambda x: x[0]**2 + x[1]**2
        def partition(left, right):
            pivotIdx = right
            pivotDist = eucl(points[pivotIdx])
            i = left

            for j in range(left, right):
                if eucl(points[j]) < pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i +=1
            points[i], points[right] = points[right], points[i]
            return i

        l,r = 0,len(points) -1
        pivot = len(points)

        while pivot != k:
            pivot = partition(l,r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]
