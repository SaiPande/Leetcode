class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        leap = 0
        months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        dayofweek = {
    0: "Friday",
    1: "Saturday",
    2: "Sunday",
    3: "Monday",
    4: "Tuesday",
    5: "Wednesday",
    6: "Thursday"
}

        for i in range(1971, year):
            if (i%4 ==0 and i%100 != 0) or (i%400 == 0):
                leap += 1

        daysinmonths = 0

        for key in range(1, month):
            daysinmonths += months[key]


        if month > 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            daysinmonths += 1

        daysinyear = (year - 1971)*365

        totaldays = day - 1 +daysinmonths+daysinyear+leap

        d = (totaldays)%7

        return dayofweek[d]