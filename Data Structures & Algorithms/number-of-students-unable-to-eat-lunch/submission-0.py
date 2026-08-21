class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = len(students)
        queue = deque(students)
        
        balance = count
        for sandwich in sandwiches:
            i = 0
            while i < count and queue[0] != sandwich:
                temp = queue.popleft()
                queue.append(temp)
                i += 1
            if queue[0] == sandwich:
                queue.popleft()
                balance -=1
            else:
                break
        return balance

            