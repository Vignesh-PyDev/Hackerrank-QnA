# # Probelm Statement


# # https://www.hackerrank.com/challenges/input/problem

import re

if __name__ == '__main__':

	Var_Poly = "1 4"

	Var_Poly_Expr = "x**3 + x**2 + x + 1"

	Temp_Var = re.findall(r'[0-9]*',Var_Poly)

	Eval = Var_Poly_Expr.replace('x',Temp_Var[0])

	# Temp_Store = 0

	# print(Temp_Var[2])

	# print(eval(Eval))

	if(eval(Eval) == int(Temp_Var[2])):

		print(True)

	else:

		print(False)

	

	



#     Temp = 0

#     for x in range(int(Var_Poly[2])):

#     	Temp += int(Var_Poly[0])**int(x)

#     if int(Var_Poly[2]) == Temp:

#     	print(True)

#     else:print(False)

# import re

# Var_Poly = "2 15"

# Temp = 0


# # print(re.findall(r'[0-9]*',Var_Poly.strip())[0])

# for x in range(int(re.findall(r'[0-9]*',Var_Poly.strip())[2])):

# 	Temp += int(re.findall(r'[0-9]*',Var_Poly.strip())[0])**int(x)

# if int(re.findall(r'[0-9]*',Var_Poly.strip())[2]) == Temp:

# 	print(True)

# else:print(False)    