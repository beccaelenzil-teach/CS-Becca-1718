# Dates
#
# Name:
#

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
        """
        Returns a new object with the same month, day, year
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
        fdays = 28
        if self.isLeapYear() == True:
            fdays = 29

        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]

        if self.month == 12 and self.day == 31:
            self.year += 1
            self.day = 1
            self.month = 1
        elif self.day == DIM[self.month]:
            self.day = 1
            self.month +=1
        else:
            self.day+=1

    def yesterday(self):
        fdays = 28
        if self.isLeapYear() == True:
            fdays = 29

        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]

        if self.month == 1 and self.day == 1:
            self.year -= 1
            self.day = 31
            self.month = 12
        elif self.day == 1:
            self.month -=1
            self.day = DIM[self.month]
        else:
            self.day-=1

    def addNDays(self,N):
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self,N):
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):

        if self.equals(d2) == True:
            return None

        elif self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        else:
            if self.month < d2.month:
                return True
            elif self.month > d2.month:
                return False
            else:
                if self.day < d2.day:
                    return True
                elif self.day > d2.day:
                    return False

    def isAfter(self,d2):

        before = self.isBefore(d2)
        if before == True:
            return False
        elif before == False:
            return True
        else:
            return None





ny = Date(1,1,2015)
d2 = Date(1,1,2015)

print(ny.isAfter(d2))
'''
d = Date(11, 12, 2014)
d.addNDays(1278)
print(" ")
print(d)
'''


