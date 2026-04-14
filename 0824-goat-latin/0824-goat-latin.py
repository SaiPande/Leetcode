class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst = sentence.split()
        finallist = []
        a_suffix = 'a'
        for i, word in enumerate(lst):
            if word[0] in 'aeiouAEIOU':
                word += 'ma'

            else:
                word = word[1:]+word[0]+'ma'

            word += a_suffix
            finallist.append(word)
            a_suffix += 'a'

        return ' '.join(finallist)
