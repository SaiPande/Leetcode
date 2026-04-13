class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst1 = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lst2 = [chr(i) for i in range(ord('a'),ord('z')+1)]
        set1 = set()
        zipper = dict(zip(lst2,lst1))
        
        for i in words:
            morsewords = ''
            for j in i:
                if j in zipper:
                    morsewords += zipper[j]
            set1.add(morsewords)

        return len(set1)             