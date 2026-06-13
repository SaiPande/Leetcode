class Solution:
    def generateTag(self, caption: str) -> str:
        output = []
        caption = caption.strip(' ')
        if len(caption) == 0:
            return '#'
        output.append('#')
        output.append(caption[0].lower())
        for i in range(1,len(caption)):
            if caption[i] == ' ':
                continue
            if caption[i-1] == ' ':
                output.append(caption[i].upper())
            else:
                output.append(caption[i].lower())   
        finalcaption = ''.join(output)        
        return finalcaption[:100]
