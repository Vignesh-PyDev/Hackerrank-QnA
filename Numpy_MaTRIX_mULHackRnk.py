import numpy 

N = int(input())

# print(N)

arr_1 = [[input() for n in range(int(N))] for m in range(int(N))]

arr_2 = [[input() for n in range(int(N))] for m in range(int(N))]



Numpy_Array_1 = numpy.array(arr_1)

Numpy_Array_1 = numpy.array(arr_1, dtype=numpy.float32)


Numpy_Array_2 = numpy.array(arr_2)

Numpy_Array_2 = numpy.array(arr_2, dtype=numpy.float32)

print(numpy.dot(Numpy_Array_1,Numpy_Array_2))

# # n = int(nm[0])
# # m = int(nm[1])
# # arr = []
# # for i in range(n):
# #     m = list(map(int, input().split()))
# #     arr.append(m)
# arr = numpy.array(arr)