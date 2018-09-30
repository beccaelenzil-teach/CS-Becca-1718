import cmath as math
import time

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __repr__(self):
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s

    def isLeapYear(self):
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def tomorrow(self):
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        if self.day == 31 and self.month == 12:
            self.year += 1
            self.month = 1
            self.day = 1
        elif self.day == DIM[self.month]:
            self.month += 1
            self.day = 1
        else:
            self.day += 1
        #print(self)

    def yesterday(self):
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        if self.day == 1 and self.month == 1:
            self.day = 31
            self.month = 12
            self.year -= 1
        elif self.day == 1:
            self.month -= 1
            self.day = DIM[self.month]
        else:
            self.day -= 1
        #print(self)

    def addNdays(self, N):
        a = 1
        while a <= N:
            self.tomorrow()
            a += 1

    def subNdays(self, N):
        a = 1
        while a<= N:
            self.yesterday()
            a += 1

    def isBefore(self, d2):
        if self.year < d2.year: return False
        if self.year > d2.year: return True
        elif self.month < d2.month: return False
        elif self.month > d2.month: return True
        elif self.day <= d2.day: return False
        else: return True


    def isAfter(self, d2):
        if self.year > d2.year: return False
        if self.year < d2.year: return True
        elif self.month > d2.month: return False
        elif self.month < d2.month: return True
        elif self.day >= d2.day: return False
        else: return True

    def equals(self, d2):
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else: return False

    def copy(self):
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def diff(self, d2):
        a = 0
        dnew = self.copy()
        if dnew.isAfter(d2) == False:
            while dnew.equals(d2) == False:
                dnew.yesterday()
                a += 1
        else:
            while dnew.equals(d2) == False:
                dnew.tomorrow()
                a += 1
        return a

    def dow(self):
        dstart = Date(11,12,2014) #Wednesday
        DOWF = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        DOWB = ["Wednesday", "Tuesday", "Monday", "Sunday", "Saturday", "Friday", "Thursday"]
        if self.isBefore(dstart):
            return(DOWF[self.diff(dstart) % 7])
        else:
            return(DOWB[self.diff(dstart) % 7])

    def dow2(self, refDate):
        """
        optimization is cool
        """
        DOWF = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        DOWB = ["Wednesday", "Tuesday", "Monday", "Sunday", "Saturday", "Friday", "Thursday"]
        if self.isBefore(refDate): return(DOWF[self.diff(refDate) % 7])
        else: return(DOWB[self.diff(refDate) % 7])

    def dowcounter(self, a, b):
        print("Counting:",self.month, "/", self.day)
        dowd = {}              # dowd == 'day of week dictionary'
        dowd["Sunday"] = 0     # a 0 entry for Sunday
        dowd["Monday"] = 0     # and so on
        dowd["Tuesday"] = 0
        dowd["Wednesday"] = 0
        dowd["Thursday"] = 0
        dowd["Friday"] = 0
        dowd["Saturday"] = 0
        refDate = findrefDate(self.day, a)

    # live for another 100 years
        if a > b:
            print("ERROR: start year must be less than the end year.")
        for year in range(a, b):
            d = Date(self.month, self.day, year)
            s = d.dow2(refDate)        # get day of week
            dowd[s] += 1       # count it
            if s == "Wednesday":
                refDate = d
            if year % 10 == 0: print('Current date is', d)

        print("Totals for", self.month, "/", self.day, "are", dowd)

def findrefDate(daycount, yearstart):
    d = Date(1, daycount, yearstart)
    while d.dow() != "Wednesday":
        d.tomorrow()
    return d

def datedowcounter(daycount, yearstart, yearend):
    print("counting day:", daycount)
    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0
    refDate = findrefDate(daycount, yearstart)
    if yearstart > yearend: print("ERROR: start year must be less than the end year.")
    for year in range(yearstart, yearend):
        for month in range (1,13):
            d = Date(month, daycount, year)
            s = d.dow2(refDate)        # get day of week
            dowd[s] += 1       # count it
            if s == "Wednesday":
                refDate = d
            if year % 10 == 0 and month == 1:
                print('Current date is', d)


    print("Totals for day", daycount, "are", dowd)

# we could return dowd here
# but we don't need to right now
# return dowd

def nycounter():
    """Looking ahead to 100 years of New Year's celebrations"""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # live for another 100 years
    for year in range(2014, 2115):
        d = Date(1, 1, year)   # get ny
        print('Current date is', d)
        s = d.dow()        # get day of week
        dowd[s] += 1       # count it

    print('totals are', dowd)

    # we could return dowd here
    # but we don't need to right now
    # return dowd





print(" ")
print("--------------------------------------")
print("date basics")
print("--------------------------------------")

d = Date(11,12,2014)
print("11/12/2014 == ", d)
d2 = d.copy()#Date(11,12,2014)
print("11/12/2014 == ", d2)
print("d == d2 is False == ", d == d2)
print("d and d2 have the same date is True == ", d.equals(d2))
print(" ")

print("d's id: ", id(d))
print("d2's id: ", id(d2))
print(" ")
print("d2 is in a leap year is False == ", d2.isLeapYear())
print(" ")
d3 = Date(1,1,2020)
print("d3: ", d3)

print("d3 is in a leap year is True == ", d3.isLeapYear())
print(" ")

print(" ")
print("--------------------------------------")
print("tomorrow and yesterday test")
print("--------------------------------------")

d = Date(12, 31, 2014)
print("12/31/2014 == ", d)
d.tomorrow()
print("1/1/2015 == ", d)


d2 = Date(1, 1, 2015)
print("1/1/2015 == ", d2)
d2.yesterday()
print("12/31/2014 == ", d2)


d = Date(2, 28, 2016)
d.tomorrow()
print("02/29/2016 == ",d)
d.tomorrow()
print("3/1/2016 == ",d)
d.yesterday()
print("02/29/2016 == ",d)


print(" ")
print("subNDays and addNDays test \n")

print("11/12/2014 through 11/15/2014")
d = Date(11, 12, 2014)
d.addNdays(3)

print(" ")
print("print(11/15/2014 through 11/12/2014")
d = Date(11, 15, 2014)
d.subNdays(3)




print(" ")
print("--------------------------------------")
print("isAfter test")
print("--------------------------------------")
ny = Date(1,1,2015)    # New Year's
d2 = Date(11,12,2014)
print("True == ", ny.isAfter(d2))
print("False == ", d2.isAfter(ny))
print("False == ", d2.isAfter(d2))

print(" ")
print("--------------------------------------")
print("diff test")
print("--------------------------------------")
d = Date(3,8,2016)
d3 = Date(4,1,2016)
print("24 == ", d3.diff(d))
print("-24 == ", d.diff(d3))

d = Date(12,1,2015)
d3 = Date(3,15,2016)
d3.diff(d)
print("105 == ",d3.diff(d))

print(" ")
print("--------------------------------------")
print("dow test")
print("--------------------------------------")
print("Monday == ", Date(10, 28, 1929).dow())
print("Monday == ",  Date(10, 19, 1987).dow())
print("Friday == ",  Date(1, 1, 2100).dow())

"""a
d = Date(3,8,2016)    # now
d2 = Date(4,1,0000)  # break!
#d.diff(d2)

Date(3,14,2016).diff(Date(4,14,2016))
Date(3,14,2016).diff(Date(3,14,2017))
Date(3,14,2016).diff(Date(3,14,2116))
Date(3,14,2016).diff(Date(1,1,0000))
"""
