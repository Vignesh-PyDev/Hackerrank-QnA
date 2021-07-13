# Probelm Statement

# https://www.hackerrank.com/challenges/python-time-delta/problem?h_r=next-challenge&h_v=zen


# !/bin/python3


# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000


import math
import os
import random
import re
import sys
from datetime import datetime, date
import calendar
from datetime import datetime

# Complete the time_delta function below.

# def get_Month_Num(Month_Name):

# 	return calendar.month_name[::].index(Month_Name)

# ma = re.search(r'(\s[0-9]+)*(\s[a-zA-z]+)(\s[0-9]{4})(\s[0-9]{2}:[0-9]{2}:[0-9]{2}\s)',"Sun 10 May 2015 13:54:36 -0700")


def time_delta(t1, t2):

	t3 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')

	t4 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')


	return abs(round((t3-t4).total_seconds()))

# tst_1 = time_delta("Sun 10 May 2015 13:54:36 -0700","Sun 10 May 2015 13:54:36 -0000")

# tst_2 = time_delta("Sat 02 May 2015 19:54:36 +0530","Fri 01 May 2015 13:54:36 -0000")




tst_1 = time_delta("Sat 24 Mar 2170 03:47:07 +0430","Mon 30 Dec 2272 20:27:41 -1000")

print(tst_1)

