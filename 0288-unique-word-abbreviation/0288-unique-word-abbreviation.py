class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.seen = set()
        self.conflicts = set() 
        self.dictionary = set(dictionary)
        for i,word in enumerate(self.dictionary):
            abbr = word if len(word) <= 2 else word[0]+str(len(word)-2)+word[-1]
            if abbr in self.seen:
                self.conflicts.add(abbr)
            else:
                self.seen.add(abbr)
        #self.seen -= self.conflicts

    def isUnique(self, word: str) -> bool:
        abbr = word if len(word) <= 2 else word[0]+str(len(word)-2)+word[-1]
        if abbr in self.conflicts:
            return False
            
        if abbr in self.seen and word not in self.dictionary:
            return False
            
        return True                   


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)