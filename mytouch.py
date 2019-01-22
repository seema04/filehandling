Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #!usr/bin/python2

import os
import sys

f=sys.argv[1:]
for i in f:
         if os.path.isdir(i):
                print "dir already exist"
        
         elif os.path.isfile(i):
                print "file already exist"
         else:
                os.mkdir(i)
