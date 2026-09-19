class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        def overlapsByRadius(p1x: int, p1y: int, p2x: int, p2y: int) -> bool:
            """returns True if distance between p1-p2 is smaller than radius, else False"""
            return sqrt(pow(abs(p1x-p2x),2)+pow(abs(p1y-p2y),2)) < radius

        # situation side - vertical
        if xCenter >= x1 and xCenter <= x2:
            if y2 < yCenter - radius or y1 > yCenter + radius:
                return False
        
        # situation side - horizontal
        elif yCenter >= y1 and yCenter <= y2:
            if x2 < xCenter - radius or x1 > xCenter + radius:
                return False

        # situation corner - all - check by radius
        else:
            if xCenter > x2 and yCenter > y2:
                c1, c2 = x2, y2
            elif xCenter < x1 and yCenter > y2:
                c1, c2 = x1, y2
            elif xCenter < x1 and yCenter < y1:
                c1, c2 = x1, y1
            elif xCenter > x2 and yCenter < y1:
                c1, c2 = x2, y1
            else:
                return True
            
            return overlapsByRadius(c1, c2, xCenter, yCenter)

        return True

        