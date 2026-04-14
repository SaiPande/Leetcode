class Solution:
    def convertDateToBinary(self, date: str) -> str:
        lst = date.split('-')
        print(lst)
        lst2 = []
        lst2.append(bin(int(lst[0]))[2:])
        lst2.append(bin(int(lst[1]))[2:])
        lst2.append(bin(int(lst[2]))[2:])

        return '-'.join(lst2)