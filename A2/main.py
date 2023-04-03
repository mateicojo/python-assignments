# cocktail sort, strand sort
import random
import timeit
def cocktail_sort_steps(a, step):
    c=0
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                c+=1
                if step&c==0:
                    print(a)

                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                c+=1
                if step&c==0:
                    print(a)

                swapped = True


        start = start + 1

def cocktail_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):


        swapped = False

        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]

                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]

                swapped = True
        start = start + 1
    return a


def strand_sort_step(inp, step):
    output = strand(inp)
    while len(inp):
        output = merge_step(output, strand(inp), step)
    return output

def strand_sort(inp):
    output = strand(inp)
    while len(inp):
        output = merge(output, strand(inp))
    return output

def merge_step(a, b, step):
    output = []
    c=0
    while len(a) and len(b):
        if a[0] < b[0]:
            output.append(a.pop(0))
            c+=1
            if step%c==0:
                print(a," ",b)
        else:
            output.append(b.pop(0))
            c+=1
            if step%c==0:
                print(a," ",b)
    output += a
    output += b
    return output


def merge(a, b):
    output = []
    while len(a) and len(b):
        if a[0] < b[0]:
            output.append(a.pop(0))
        else:
            output.append(b.pop(0))
    output += a
    output += b
    return output

def strand(inp):
    element, sub = 0, [inp.pop(0)]
    while element < len(inp):
        if inp[element] > sub[-1]:
            sub.append(inp.pop(element))
        else:
            element += 1
    return sub
def seca(l):
    k = int(input("Enter a number of steps: "))
    while True:
        if k>0:
            break
        else:
            k=int(input("Please enter a valid number of steps! "))
    cocktail_sort_steps(l, k)
    print("The sorted list: ",l)

def timer(lista):
    start1 = timeit.default_timer()
    cocktail_sort(lista)
    time1 = format(timeit.default_timer() - start1, '.5f')
    start2 = timeit.default_timer()
    strand_sort(lista)
    time2 = format(timeit.default_timer() - start2,'.5f')
    print(f"""cocktail sort time: {time1}      strand sort time: {time2}""")


def generate_best_case():
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    for _ in range(1,300):
        a.append(random.randint(1,100))
    a.sort()
    timer(a)
    for _ in range(1,600):
        b.append(random.randint(1,100))
    b.sort()
    timer(b)
    for _ in range(1,1200):
        c.append(random.randint(1,100))
    c.sort()
    timer(c)
    for _ in range(1,2400):
        d.append(random.randint(1,100))
    d.sort()
    timer(d)
    for _ in range(1,4800):
        e.append(random.randint(1,100))
    e.sort()
    timer(e)

def generate_avg_case():
    a = []
    b = []
    c = []
    d = []
    e = []
    for _ in range(1, 300):
        a.append(random.randint(1, 100))
    timer(a)
    for _ in range(1, 600):
        b.append(random.randint(1, 100))
    timer(b)
    for _ in range(1, 1200):
        c.append(random.randint(1, 100))
    timer(c)
    for _ in range(1, 2400):
        d.append(random.randint(1, 100))
    timer(d)
    for _ in range(1, 4800):
        e.append(random.randint(1, 100))
    timer(e)


def generate_worst_case():
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    for _ in range(1,300):
        a.append(random.randint(1,100))
    a.sort(reverse=True)
    timer(a)
    for _ in range(1,600):
        b.append(random.randint(1,100))
    b.sort(reverse=True)
    timer(b)
    for _ in range(1,1200):
        c.append(random.randint(1,100))
    c.sort(reverse=True)
    timer(c)
    for _ in range(1,2400):
        d.append(random.randint(1,100))
    d.sort(reverse=True)
    timer(d)
    for _ in range(1,4800):
        e.append(random.randint(1,100))
    e.sort(reverse=True)
    timer(e)


def print_menu():
    menu_options = {
        1: 'Generate a random list',
        2: 'Sort the list using Cocktail Sort',
        3: 'Sort the list using Strand Sort',
        4: 'Best case',
        5: 'Average case',
        6: 'Worst case',
        0: 'Exit',
    }
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def generate(a):
    n = int(input("Enter the number of elements in your list: "))
    for _ in range(0,n):
        a.append(random.randint(0,100))
    print(a)

def seca2(l):
    k = int(input("Enter a number of steps: "))
    while True:
        if k > 0:
            break
        else:
            k = int(input("Please enter a valid number of steps! "))
    b = strand_sort_step(l, k)
    print(b)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l=[]
    while (True):
        print_menu()
        option = int(input('Enter your choice: '))
        if option == 1:
            generate(l)
        elif option==2:
            seca(l)
        elif option==3:
            seca2(l)
        elif option==4:
            generate_best_case()
        elif option==5:
            generate_avg_case()
        elif option==6:
            generate_worst_case()
        elif option== 0:
            exit()