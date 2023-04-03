"""The sequence a = a1, ..., an with distinct integer elements is given. Determine all subsets of at least two elements with the property:
The elements in the subset are in increasing order
Any two consecutive elements in the subsequence have at least one common digit"""
#complexity O(2^n)


def common_digit(a,b):
    #checks if a and b have at least one common digit
    freq_a=10*[0]
    freq_b=10*[0]
    while(a!=0):
        freq_a[a%10]=1
        a//=10
    while(b!=0):
        freq_b[b%10]=1
        b//=10
    for j in range(10):
        if freq_a[j]==freq_b[j] and freq_a[j]==1:
            return True
    return False

array=[1,51,2,25]
x=(len(array)+1)*[0]

def valid(k):
    global x
    global array
    if k < 2:
        return True
    if (x[k] > x[k-1] and (array[x[k-1]]<array[x[k]] and common_digit(array[x[k]],array[x[k-1]]))):
        return True
    return False

def solution(k):
    global i
    if (k==i):
        return True
    else:
        return False

def print_solution(k):
    global x
    print([array[j] for j in x[1:k+1]])

def back(k):
    global x
    global i
    x[k]=-1
    while x[k]<len(array)-1:
        x[k]+=1
        if valid(k):
            if solution(k):
                print_solution(k)
            else:
                back(k+1)

i=2
while i<=len(array):
    x = (len(array)+1) * [0]
    back(1)
    i+=1

