import numpy

nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for i in range(n):
    m = list(map(int, input().split()))
    arr.append(m)
arr = numpy.array(arr)

mean = numpy.mean(arr, axis = 1)
var = numpy.var(arr, axis = 0)
std = numpy.std(arr)

print(mean)
print(var)

rnd = numpy.around(std, 11)
print(rnd)




# import numpy

# # 
# # 1 1 1
# # 1 1 1
# # 1 1 1


# my_array = numpy.array([ [1, 1,1], [1, 1,1],[1, 1,1] ])


# arr = numpy.std(my_array,axis = None)

# print(numpy.mean(my_array, axis = 1))         #Output : [ 1.  1.]
# print(numpy.var(my_array, axis = 0))         #Output : [ 0.5  0.5]
# print(numpy.around(arr,decimals=11))


# # 1.11803398875

# # 1.11803398875

