import re
if __name__ == '__main__':

	Var_Poly = "print(2 + 5)"

	

	print(eval(Var_Poly.replace('print','')))

	# print(eval(Var_Poly[Var_Poly.index('('):Var_Poly.index(')')+1]))

	# eval()

