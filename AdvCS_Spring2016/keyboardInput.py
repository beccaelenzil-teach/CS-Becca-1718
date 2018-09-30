__author__ = 'becca.elenzil'

import sys, select

print "You have five seconds to answer!"

i, o, e = select.select( [sys.stdin], [], [], 5)

if (i):
  print "You said", sys.stdin.readline().strip()
else:
  print "You said nothing!"

print type(sys.stdin.readline())