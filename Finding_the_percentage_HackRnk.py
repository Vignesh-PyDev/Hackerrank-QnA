# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

from functools import reduce

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores	
    query_name = input()


    print("{:.2f}".format(reduce(lambda x,y: x + y,(student_marks[query_name]))/len(student_marks[query_name])))