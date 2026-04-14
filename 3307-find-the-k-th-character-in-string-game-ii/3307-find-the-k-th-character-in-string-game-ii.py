class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        '''word = 'a'
        i = 0
        while(len(word) <= k):
            if i >= len(operations):
                break
            if operations[i] == 0:
                word += word
            else:
                word += ''.join([chr(ord(j) + 1) for j in word])   
            i += 1    
        return word[k-1] ''' 

        k -= 1
        count = 0

        for i in range(min(len(operations),60)):
            if (k>>i) & 1:
                count += operations[i]

        return chr((count % 26) + ord('a'))
                  