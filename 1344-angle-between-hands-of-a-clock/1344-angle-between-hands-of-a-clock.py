class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #matrix.sort(key=lambda x: x[0])

        hoursangle = hour*30 if hour<12 else 0
        minutesangle = minutes*6 if minutes<60 else 0
        hoursangle+= (30*minutes)/60
        return min((minutesangle - hoursangle) % 360, (hoursangle - minutesangle) % 360)
