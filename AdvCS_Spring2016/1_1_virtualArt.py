__author__ = 'becca.elenzil'

# python 2
#
# Homework 10, Problem 1
#
# Name:
#

import time

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def tomorrow(self):
        """changes the calling object to represent one day after the original date"""
        if not self.isLeapYear():
            days_in_a_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_in_a_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.day == days_in_a_month[self.month]:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        """changes the calling object to represent one day before the original date"""
        if not self.isLeapYear():
            days_in_a_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_in_a_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.day == 1:
            if self.month == 1:
                self.day = days_in_a_month[12]
                self.month = 12
                self.year -= 1
            else:
                self.day = days_in_a_month[self.month - 1]
                self.month -= 1
        else:
            self.day -= 1

    def addNDays(self, N):
        for i in range(N):
            print self
            self.tomorrow()
        print self

    def subNDays(self, N):
        for i in range(N):
            print self
            self.yesterday()
        print self

    def isBefore(self, d2):
        """This method should return True if the calling object is a calendar date before the argument named d2"""
        if self.equals(d2):
            return False
        elif self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def isAfter(self, d2):
        """This method should return False if the calling object is a calendar date before the argument named d2"""
        if self.equals(d2):
            return False
        elif self.year < d2.year:
            return False
        elif self.year == d2.year:
            if self.month < d2.month:
                return False
            elif self.month == d2.month:
                if self.day < d2.day:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True

    def diff(self,d2):
        """number of days between self and d2"""
        day1 = self.copy()
        day2 = d2.copy()
        counter = 0
        t0 = time.clock()

        if day1.isBefore(day2):
            while day1.isBefore(day2):
                day2.yesterday()
                counter -= 1
            t1 = time.clock()
            #print t1 - t0
            return counter
        else:
            while day2.isBefore(day1):
                day1.yesterday()
                counter += 1
            t1 = time.clock()
            #print t1 - t0
            return counter

    def dow(self):
        """returns the day of the week"""
        today = Date(2,28,2016)
        numDays = self.diff(today)
        if numDays % 7 == 0:
            self.weekday = 'Sunday'
        elif numDays % 7 == 1:
            self.weekday = 'Monday'
        elif numDays % 7 == 2:
            self.weekday = 'Tuesday'
        elif numDays % 7 == 3:
            self.weekday = 'Wednesday'
        elif numDays % 7 == 4:
            self.weekday = 'Thursday'
        elif numDays % 7 == 5:
            self.weekday = 'Friday'
        elif numDays % 7 == 6:
            self.weekday = 'Saturday'

        return self.weekday

    def dow2(self,refDate):
        """returns the day of the week"""
        numDays,t = self.diff(refDate)
        if numDays % 7 == 0:
            self.weekday = 'Sunday'
        elif numDays % 7 == 1:
            self.weekday = 'Monday'
        elif numDays % 7 == 2:
            self.weekday = 'Tuesday'
        elif numDays % 7 == 3:
            self.weekday = 'Wednesday'
        elif numDays % 7 == 4:
            self.weekday = 'Thursday'
        elif numDays % 7 == 5:
            self.weekday = 'Friday'
        elif numDays % 7 == 6:
            self.weekday = 'Saturday'

        return self.weekday

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
        d = Date(5, 25, year)   # get ny
        s = d.dow()        # get day of week
        #print 'Current date is', d, 'and the day of the week is ',s
        dowd[s] += 1       # count it

    print 'totals are', dowd

    # we could return dowd here
    # but we don't need to right now
    # return dowd

def thirteenthCounter():
    """Looking ahead to 100 years of New Year's celebrations"""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    SundayRefDate = Date(2,28,2016)
    sunday = SundayRefDate.dow()

    # live for another 100 years
    for year in range(2014, 2414):
        for month in range(1,12):
            d = Date(month, 13, year)   # get ny
            s = d.dow2(SundayRefDate)        # get day of week
            dowd[s] += 1       # count it
            if d.dow() == sunday:
                SundayRefDate = d
        #print 'The Sunday Reference date is', SundayRef
    print 'totals are', dowd

    # we could return dowd here
    # but we don't need to right now
    # return dowd

#nycounter()
#thirteenthCounter()

"""
d = Date(11,12,2014)
print "d: ", d
print 'Wednesday is', d
print " "
d2 = d.copy()#Date(11,12,2014)
print "d2: ", d2

print "d == d2: ", d == d2
print "d and d2 have the same date: ", d.equals(d2)

print " "
print "d's id: ", id(d)
print "d2's id: ", id(d2)
print " "
print "d2 is in a leap year: ", d2.isLeapYear()
print " "
d3 = Date(1,1,2020)
print "d3: ", d3

print "d3 is in a leap year: ", d3.isLeapYear()


d = Date(12, 31, 2014)
print d
d.tomorrow()
print d


d2 = Date(1, 1, 2015)
print d2
d2.yesterday()
print d2


d3 = Date(12, 12, 2016)
d3.subNDays(1000)

ny = Date(1,1,2015)    # New Year's
d2 = Date(11,12,2014)
print ny.isAfter(d2)
print d2.isAfter(ny)
print d2.isAfter(d2)

d = Date(12,1,2015)
d3 = Date(3,15,2016)
print d.diff(d3)

d = Date(11, 12, 2014)
print d.diff(Date(1, 1, 1899))
print d.diff(Date(1, 1, 2101))


d = Date(9, 22, 2020)
print d.dow()

print Date(10, 28, 1929).dow()
print Date(10, 19, 1987).dow()
print Date(1, 1, 2100).dow()


d = Date(3,8,2016)    # now
d2 = Date(4,1,0000)  # break!
#d.diff(d2)

Date(3,14,2016).diff(Date(4,14,2016))
Date(3,14,2016).diff(Date(3,14,2017))
Date(3,14,2016).diff(Date(3,14,2116))
Date(3,14,2016).diff(Date(1,1,0000))
"""