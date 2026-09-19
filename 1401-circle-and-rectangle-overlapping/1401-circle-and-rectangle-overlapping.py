import math 

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # maxxcircle = xCenter+radius
        # maxycircle = yCenter+radius
        # minxcircle = xCenter-radius
        # minycircle = yCenter-radius

        # mindisx = min(abs(maxxcircle - x1), abs(minxcircle-x1),abs(maxxcircle - x2), abs(minxcircle-x2))
        # if mindisx-radius < 0:
        #     return True

        # mindisy = min(abs(maxycircle - y1), abs(minycircle-y1), abs(maxycircle - y2), abs(minycircle-y2))
        # if mindisy-radius < 0:
        #     return True    

        # return False

        x_close = max(x1, min(xCenter,x2))
        y_close = max(y1, min(yCenter, y2))

        dis = math.sqrt((xCenter-x_close)**2+(yCenter-y_close)**2)

        if dis <= radius:
            return True
        return False    