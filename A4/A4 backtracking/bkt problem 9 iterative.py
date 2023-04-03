from queue import Empty
"""The sequence a = a1, ..., an with distinct integer elements is given. Determine all subsets of at least two elements with the property:
The elements in the subset are in increasing order
Any two consecutive elements in the subsequence have at least one common digit"""
#complexity O(n^2)

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




def sublist(list):
    i = 2 #number of elements for a subset
    k=1 #number of elements already in the subset
    clist = list
    while i <= len(list):
        sublist = []
        k = k - i + 1 #reset k for next position
        while k < len(list):
            sublist.append(clist[k])
            k += 1
            if len(sublist) == i:
                break
        w=0
        ok=1
        while(w<len(sublist)-1):
            if(sublist[w]>sublist[w+1] or not common_digit(sublist[w],sublist[w+1])):
                break
            w+=1
        if ok==1:
            print(sublist)
        else:
            continue
        if k == len(list):
            k = i
            i += 1


def start():
    list = [1,51,2,25]
    sublist(list)


start()