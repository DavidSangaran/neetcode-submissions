class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, score = [], 0
        for op in operations:
            if op == "+":
                score += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                score += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif op == "C":
                score -= stack.pop()
            else:
                score += int(op)
                stack.append(int(op))
        return score