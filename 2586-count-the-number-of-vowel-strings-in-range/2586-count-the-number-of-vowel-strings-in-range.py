class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        words = words[left:right+1]
        for i in range(len(words)):
            if words[i][0] in 'aeiou' and words[i][len(words[i])-1] in 'aeiou':
                count += 1
        return count        