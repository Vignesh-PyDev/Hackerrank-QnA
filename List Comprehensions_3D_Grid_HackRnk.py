# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    x,y,z,n = 2,2,2,2

    print(n)

    L_Com = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]

    # L_Com = [[i,j,k] for i in range(3) for j in range(3) for k in range(9)]


    print(L_Com)

