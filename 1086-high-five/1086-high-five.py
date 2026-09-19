from collections import defaultdict
class Solution:

    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        student_scores = defaultdict(list)
        for student_id, score in items:
            student_scores[student_id].append(score)

        result = []

        for student_id, scores in student_scores.items():
            scores.sort(reverse=True)
            top_five_avg = sum(scores[:5]) // 5
            result.append([student_id, top_five_avg])
        result.sort(key=lambda x: x[0])

        return result