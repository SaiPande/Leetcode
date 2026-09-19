from collections import defaultdict


class Solution:

    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        # Step 1: Group scores by student ID
        student_scores = defaultdict(list)
        for student_id, score in items:
            student_scores[student_id].append(score)

        result = []

        # Step 2: Calculate the top 5 average for each student
        for student_id, scores in student_scores.items():
            # Sort scores in descending order
            scores.sort(reverse=True)
            # Take the sum of the first 5 scores and use integer division (//)
            top_five_avg = sum(scores[:5]) // 5
            result.append([student_id, top_five_avg])

        # Step 3: Sort the final result by student ID in increasing order
        result.sort(key=lambda x: x[0])

        return result