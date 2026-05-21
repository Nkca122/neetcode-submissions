class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]; res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    res[stack[-1]] = i - stack[-1]; stack.pop()
                stack.append(i)
        return res
