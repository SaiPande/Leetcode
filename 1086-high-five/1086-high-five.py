from collections import defaultdict
class Solution:

    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        studentscore = {}
        output = []

        for i in items:
            if i[0] in studentscore:
                studentscore[i[0]].append(i[1])
            else:
                studentscore[i[0]] = [i[1]]  

        for key, value in studentscore.items():
            value.sort(reverse = True)
            avg = sum(value[:5])//5
            output.append([key,avg])

        output.sort(key=lambda x:x[0])

        return output    