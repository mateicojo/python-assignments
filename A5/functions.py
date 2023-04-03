#set A: 1  set B: 10
import sys


def set_imaginary():
    imaginary=int(input("enter imaginary part:"))
    return imaginary

def set_real():
    real=int(input("enter real part:"))
    return real

def get_imaginary(z):
    return z['Imaginary']

def get_real(z):
    return z['Real']

# def get_real(z):
#      return z[0]
#
# def get_imaginary(z):
#      return z[1]

def dict_to_list(dict):
    "return a list converted from a dictionary"
    L=[]
    for i in dict.values():
        L.append(i)
    return L


def longest_subarray(L:list):
    #takes the parameter L, a list, and returns the length and elements of the longest subarray of distinct numbers.
    i=1
    leng=1
    prev=0
    maxim=0
    while i< len(L):
        while i<len(L) and L[i]!=L[i-1]:
            i+=1
        leng=i-prev+1
        if leng>maxim:
            maxim=leng
            sol = L[prev:i]
        prev = i+1
        i+=2
    return sol,len(sol)



def longest_subseq_real(L):
    #takes the parameter L, a list, and returns the
    #length and elements of a longest increasing subsequence, when considering each number's real part
    n = len(L)
    l_real=[]
    solution=[]
    maxim=0
    for i in range(len(L)): #l_real contains only the real part of the numbers in L
        l_real.append(L[i][0])
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if l_real[i] > l_real[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maxim = 0
    print(lis)
    for i in range(n):
        maxim = max(maxim, lis[i])
    x=maxim
    for i in range(len(L)-1,-1,-1):
        if lis[i]==x:
            solution.append(L[i])
        x-=1

    return maxim,solution[::-1]

List = [[1,3],[1,3],[-1,2],[-1,2],[2,2],[2,2],[0,3],[5,0]]
print(longest_subarray(List))