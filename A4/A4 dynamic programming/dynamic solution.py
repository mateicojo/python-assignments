# Given an array of integers A, maximize the value of the expression A[m] - A[n] + A[p] - A[q],
# where m, n, p, q are array indices with m > n > p > q. For A = [30, 5, 15, 18, 30, 40],
# the maximum value is 32, obtained as 40 - 18 + 15 - 5. Display both the maximum value as
# well as the expression used to calculate it.
def maximizeExpression(A):
    'Uses 4 lists to find the best result for the expresion by looking up for the best 1st elemen, then first two best elements, best three and so on...'
    solution = [] #will store the solution list?
    maximum_one = [-9999999] * (len(A) + 1)
    maximum_two = [-9999999] * len(A)
    maximum_three = [-9999999] * (len(A) - 1)
    maximum_four = [-9999999] * (len(A) - 2)
    found_index=0 #tried to use this to store the index of the most recent found element, but didn't find a proper way to implement it..
    for i in reversed(range(len(A))):
        maximum_one[i] = max(maximum_one[i+1], A[i]) #pretty much finds the maximum value of the sequence
    solution.append(maximum_one[0])

    for i in reversed(range(len(A) - 1)):
        maximum_two[i] = max(maximum_two[i+1], maximum_one[i+1]-A[i]) #best result for A[m] - A[n]
    solution.append(maximum_one[0]-maximum_two[0]) #appends the found value by subtracting the previous value from the current value,
    # this should give us the new value, right?
    for i in reversed(range(len(A) - 2)):
        maximum_three[i] = max(maximum_three[i+1], maximum_two[i+1]+A[i]) #best result for A[m] - A[n] + A[p]
    solution.append(maximum_three[0]-maximum_two[0])#i tried debugging and gets weird results here i don't get it why

    for i in reversed(range(len(A) - 3)):
        maximum_four[i] = max(maximum_four[i+1], maximum_three[i+1]-A[i]) #best result for A[m] - A[n] + A[p] - A[q]
    solution.append(maximum_three[0]-maximum_four[0])

    return maximum_four[0],solution


#A = [30, 5, 15, 18, 30, 40]
A = [3, 9, 10, 1, 30, 40]

#the code above doesn't really respect the condition m > n > p > q,
# I'm not sure what to do because it will always return the same value for a sequence of the same elements, but different order, which shouldn't happen
print(maximizeExpression(A))