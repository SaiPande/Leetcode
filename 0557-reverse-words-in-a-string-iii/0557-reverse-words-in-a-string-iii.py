class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        for i in range(0, len(lst)):
            lst[i] = lst[i][::-1]
        return ' '.join(lst)    