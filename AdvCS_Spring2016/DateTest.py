#def Date():
#    "HI!"

print " "
print "--------------------------------------"
print "date basics"
print "--------------------------------------"

d = Date(11,12,2014)
print "11/12/2014 == ", d
d2 = d.copy()#Date(11,12,2014)
print "11/12/2014 == ", d2
print "d == d2 is False == ", d == d2
print "d and d2 have the same date is True == ", d.equals(d2)
print " "

print "d's id: ", id(d)
print "d2's id: ", id(d2)
print " "
print "d2 is in a leap year is False == ", d2.isLeapYear()
print " "
d3 = Date(1,1,2020)
print "d3: ", d3

print "d3 is in a leap year is True == ", d3.isLeapYear()
print " "

print " "
print "--------------------------------------"
print "tomorrow and yesterday test"
print "--------------------------------------"

d = Date(12, 31, 2014)
print "12/31/2014 == ", d
d.tomorrow()
print "1/1/2015 == ", d


d2 = Date(1, 1, 2015)
print "1/1/2015 == ", d2
d2.yesterday()
print "12/31/2014 == ", d2


d = Date(2, 28, 2016)
d.tomorrow()
print "02/29/2016 == ",d
d.tomorrow()
print "3/1/2016 == ",d
d.yesterday()
print "02/29/2016 == ",d


print " "
print "subNDays and addNDays test \n"

print "11/12/2014 through 11/15/2014"
d = Date(11, 12, 2014)
d.addNDays(3)

print " "
print "print 11/15/2014 through 11/12/2014"
d = Date(11, 15, 2014)
d.subNDays(3)



print " "
print "--------------------------------------"
print "isAfter test"
print "--------------------------------------"
ny = Date(1,1,2015)    # New Year's
d2 = Date(11,12,2014)
print "True == ", ny.isAfter(d2)
print "False == ", d2.isAfter(ny)
print "False == ", d2.isAfter(d2)

print " "
print "--------------------------------------"
print "diff test"
print "--------------------------------------"
d = Date(3,8,2016)
d3 = Date(4,1,2016)
print "24 == ", d3.diff(d)
print "-24 == ", d.diff(d3)

d = Date(12,1,2015)
d3 = Date(3,15,2016)
d3.diff(d)
print "105 == ",d3.diff(d)

print " "
print "--------------------------------------"
print "dow test"
print "--------------------------------------"
print "Monday == ", Date(10, 28, 1929).dow()
print "Monday == ",  Date(10, 19, 1987).dow()
print "Friday == ",  Date(1, 1, 2100).dow()

"""a
d = Date(3,8,2016)    # now
d2 = Date(4,1,0000)  # break!
#d.diff(d2)

Date(3,14,2016).diff(Date(4,14,2016))
Date(3,14,2016).diff(Date(3,14,2017))
Date(3,14,2016).diff(Date(3,14,2116))
Date(3,14,2016).diff(Date(1,1,0000))
"""