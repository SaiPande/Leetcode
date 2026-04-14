class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        msgstr = ''        
        dict1 = {}
        num = 97
        for i in key:
            if i == ' ':
                continue
            elif i not in dict1:
                dict1[i] = chr(num)
                num+=1

        for i in message:
            if i == ' ':
                msgstr += ' '
            else:
                msgstr += dict1[i]

        return msgstr        