#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

	Temp = s.split(" ")

	if len(Temp) >= 2:

		for x in Temp:

			if re.match(r'^[0-1]',x):pass

			elif re.match(r'^[a-zA-Z]',x):Temp[Temp.index(x)] = x.capitalize()

		Out = ' '.join(str(d) for d in Temp)

		return Out

	else:return s

	# if re.match(r'^[0-9]',s):

	# 	return s


	# else:

	# 	if ' ' in s:

	# 		return s.capitalize()

	# 		# return "else",s[0].upper()+s[1:s.index(" ")+1]+s[s.index(' ')+1].upper()+s[s.index(' ')+2:],"else"

	# 	else:

	# 		return s

if __name__ == '__main__':

	# Str = input()

	ss = "12Hello 12world"

	# print(solve(ss))

	print(solve(ss))