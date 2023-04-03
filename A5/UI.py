import functions

# List = [[1,3],[-1,2],[2,2],[0,3],[5,0],[3,3],[0,1],[8,8],[1,4],[4,1]]
List = [{'Real':1,'Imaginary':-2},{'Real':0,'Imaginary':4},{'Real':3,'Imaginary':-2},{'Real':2,'Imaginary':5},{'Real':-1,'Imaginary':4},{'Real':2,'Imaginary':0},{'Real':0,'Imaginary':2},{'Real':-1,'Imaginary':1},{'Real':-3,'Imaginary':1},{'Real':-5,'Imaginary':2},]

def menu():
    print("""
    Choose one of the options below:
    1.Read a list of complex numbers (in z = a + bi form) from the console.
    2.Display the entire list of numbers on the console.
    3.Length and elements of a longest subarray of distinct numbers.
    4.The length and elements of a longest increasing subsequence, when considering each number's real part
    0.Exit the application
    """)
    ans=int(input(">"))
    return ans

def print_longest_subarray(L:list):
    "takes the parameter L, a list, and prints the length and elements of the longest subarray of distinct numbers."
    print(functions.longest_subarray(L))

def print_longest_subseq_real(L:list):
    "takes the parameter L, a list, and prints the length and elements of a longest increasing subsequence, when considering each number's real part"
    print(functions.longest_subseq_real(L))

def read_list():
    "reads n, number of elements of the list and it's elements, returns the list C"
    C=[]
    n = int(input("How many complex numbers do you want to enter?"))
    for i in range(0, n):
        real = functions.set_real()
        imaginary = functions.set_imaginary()
        C.append({'Real':real,'Imaginary': imaginary})
    return C

# def read_list():
    # "reads n, number of elements of the list and it's elements, returns the list C"
    # C = []
    # n = input("How many complex numbers do you want to enter?")
    # for i in range (0,n):
    #     real = input("Enter the real part: ")
    #     imaginary = input("Enter the imaginary part: ")
    #     C.append([real,imaginary])
    # return C

def print_list(C:list):
    "takes parameter C, which is a list of pairs and prints it as 'a + b*i'"
    for i in range(len(C)):
        if functions.get_real(C[i])==0 and functions.get_imaginary(C[i])==0:
            print(0)
        elif functions.get_real(C[i])==0:
            print(f"{functions.get_imaginary(C[i])}*i")
        elif functions.get_imaginary(C[i])==0:
            print(f"{functions.get_real(C[i])}")
        else:
            print(f"{functions.get_real(C[i])} + {functions.get_imaginary(C[i])}*i")

def exit_program():
    quit()

while True:
    answer = menu()
    while answer != 0:
        if answer == 1:
            List = read_list()
            answer = menu()
        elif answer == 2:
            print_list(List)
            answer = menu()
        elif answer == 3:
            # functions.dict_to_list(List)
            print_longest_subarray(List)
            answer = menu()
        elif answer == 4:
            # functions.dict_to_list(List)
            print_longest_subseq_real(List)
            answer = menu()
    exit_program()

