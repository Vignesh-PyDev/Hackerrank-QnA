# https://www.hackerrank.com/challenges/ginorts/problem


Input = "So2rGti5476n8gJ1234"

Output = "ginortS1324"

Output_Lower = [o for o in Input if (ord(str(o)) >= 97 and ord(str(o)) <=122)]


Output_Upper = [o for o in Input if (ord(str(o)) >= 65 and ord(str(o)) <=90)]


Output_Num_Even= [o for o in Input if ((ord(str(o)) >= 48 and ord(str(o)) <=57) and (int(o) % 2 == 0))]


Output_Num_Odd= [o for o in Input if ((ord(str(o)) >= 48 and ord(str(o)) <=57) and (int(o) % 2 == 1))]


print(''.join(sorted(Output_Lower)+sorted(Output_Upper)+sorted(Output_Num_Odd)+sorted(Output_Num_Even)))




