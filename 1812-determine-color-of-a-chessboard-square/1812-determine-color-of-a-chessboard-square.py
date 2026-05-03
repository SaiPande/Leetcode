class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        if ord(coordinates[0])%2 == 1:
            if int(coordinates[1])%2 == 1:
                return False
            else:
                return True
        else:
            if int(coordinates[1])%2 == 1:
                return True
            else:
                return False    