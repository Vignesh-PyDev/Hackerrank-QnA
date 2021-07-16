# Task

# You are given a space separated list of integers. 
# If all the integers are positive, then you need to check if any integer is a palindromic integer.



if __name__ == '__main__':

	# Input = input()

	Input = "5"

	Input_1 = "12 9 61 5 14".strip().split(' ')

	Cond_1 = [(int(i) > 0 and int(i) < 100) for i in Input_1]

	Cond_2 = [i == i[::-1] for i in Input if Input in Input_1]

	print(all

			(
				[
				all(Cond_1) == True,

				any(Cond_2)  == True
				]
				)
		)


print(Cond_1,"1")

print(Cond_2,"2")