# Given an array of integers A, maximize the value of the expression A[m] - A[n] + A[p] - A[q],
# where m, n, p, q are array indices with m > n > p > q. For A = [30, 5, 15, 18, 30, 40],
# the maximum value is 32, obtained as 40 - 18 + 15 - 5. Display both the maximum value as
# well as the expression used to calculate it.

A = [30, 5, 15, 18, 30, 40]
n = len(A)
x = len(A)*[-1]
max = -A[0]+A[1]-A[2]+A[3]
solution_array = []

def solution(k):
    global max
    global solution_array
    expression = 0
    sign = 1
    D = []
    if sum(x[:k+1]) == 4:
        for j in range(k+1):
            if x[j]== 1:
                expression += (-1)**sign * A[j]
                sign += 1
                D.append(A[j])
        if expression > max:
            max = expression
            solution_array = D
            D=[]


def back(k):
    for i in range (0,2):
        x[k]=i
        solution(k)
        if k != n-1:
            back(k+1)

back(0)
print(max , solution_array , sep = '\n')