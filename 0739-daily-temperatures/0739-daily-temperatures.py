from queue import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n<1:
            return []
        if n == 1:
            return [0]
        output = [0]*n
        answerqueue = deque()

        for i in range(n):
            while len(answerqueue) > 0 and temperatures[answerqueue[-1]]<temperatures[i]:
                prev = answerqueue.pop()
                output[prev] = i-prev
            answerqueue.append(i)           
        return output      
