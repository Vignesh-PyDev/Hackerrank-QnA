# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:

# 123...n


# Note that "" represents the consecutive values in between.

# Example

# n = 5

# Print the string:12345


if __name__ == '__main__':
    n = int(input())

    Temp_List = []

    for Iter in range(1,n+1):

    	Temp_List.append(Iter)

    print(''.join(str(i) for i in Temp_List))