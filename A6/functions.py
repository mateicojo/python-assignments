transactions=[
    [10,150,"out","pizza"],
    [12,10,"out","soda"],
    [14,1200,"in","salary"],
    [10,200,"out","clothes"],
    [10,150,"out","food"],
    [10,150,"out","meds"],
    [13,199,"in","slots"],
    [11,120,"out","drinks"],
    [11,350,"in","bonus"]
]

def get_day(n):
    return transactions[n][0]
def get_value(n):
    return transactions[n][1]
def get_type(n):
    return transactions[n][2]
def get_description(n):
    return transactions[n][3]

def set_day(n,a):
    transactions[n][0]=a
def set_value(n,a):
    transactions[n][1]=a
def set_type(n,a):
    transactions[n][2]=a
def set_description(n,a):
    transactions[n][3]

def lower(lis):
    '''
    turns upper case chars into lower case chars
    :param lis: list
    :return: lower case list
    '''
    i=0
    while i<len(lis):
        if lis[i].isnumeric()==False:
            lis[i]=lis[i].lower()
        i+=1
    return lis

def print_transaction(n):
    '''
    prints the nth transaction
    '''
    print(*n)

def add_transaction(trans):
    '''
    parses the user input string (a)
    :param trans: the input string from the user
    '''
    command = [i for i in trans.split() if i not in ['', ' ']]
    lower(command)
    try:
        if command[0]!=None:
            match command[0]:
                case 'add':
                    if command[1].isnumeric():
                        if command[2]=='in' or command[2]=='out':
                            aux=[str(21),command[1],command[2],command[3]]
                            transactions.append(aux)
                        else:
                            print("Error!")
                case 'insert':
                    if  command[1].isnumeric() and command[2].isnumeric():
                        if command[3]=='in' or command[3]=='out':
                            aux=[command[1],command[2],command[3],command[4]]
                            transactions.append(aux)
                        else:
                            print("Error!")
    except:
        print("Error!")

def test_add_transaction():
    comm = "add 300 in money"
    initial_len = len(transactions)
    add_transaction(comm)
    assert(initial_len+1)==len(transactions)
    assert(transactions[len(transactions)-1])==["21","300","in","money"]

test_add_transaction()

def search_transaction(search:list):
    '''
    searches for a transaction with a given day, type and description
    :param search: contains day, type, description of the element to search for
    :return: the index of the transaction in the transactions list, or "Not found"
    '''
    for i in transactions:
        if i[0]==search[0] and i[2]==search[1] and i[3]==search[2]:
            return i
    return "Transaction not found!"


def modify_transaction(trans):
    '''
    remove <day>
    remove <start day> to <end day>
    remove <type>
    replace <day> <type> <description> with <value>

    modifies a certain transaction, all the data should be available in the parameter trans
    :param trans: the input string from the user
    '''
    command = [i for i in trans.split() if i not in ['', ' ']]
    try:
        if command[0] != None:
            match command[0]:
                case 'remove':
                    if len(command) == 2:
                        if command[1].isnumeric():
                            i = 0
                            while i < len(transactions):
                                if int(transactions[i][0]) == int(command[1]):
                                    del transactions[i]
                                    i -= 1
                                i += 1
                        else:
                            match command[1]:
                                case 'in':
                                    i = 0
                                    while i < len(transactions):
                                        if transactions[i][2] == command[1]:
                                            del transactions[i]
                                            i -= 1
                                        i += 1
                                case 'out':
                                    i = 0
                                    while i < len(transactions):
                                        if transactions[i][2] == command[1]:
                                            del transactions[i]
                                            i -= 1
                                        i += 1
                    elif command[2] == 'to' and command[3].isnumeric():
                        i = 0
                        while i < len(transactions):
                            if int(transactions[i][0]) > int(command[1]) and int(transactions[i][0]) < int(command[3]):
                                del transactions[i]
                                i -= 1
                            i += 1
                    else:
                        print("Syntax Error!")
                case "replace":
                    search=[]
                    search.append(command[1])
                    search.append(command[2])
                    search.append(command[3])
                    value = int(command[5])
                    try:
                        transactions[search_transaction(search)][1]=value
                    except:
                        pass
    except:
        print("Error!")

def display_transactions(str):
    '''
    list
    list <type>
    list [ < | = | > ] <value>
    list balance <day>

    list – display all transactions
    list in – display all in transactions
    list > 100 - display all transactions having an amount of money >100
    list = 67 - display all transactions having an amount of money =67
    list balance 10 – compute the account’s balance at the end of day 10. This is the sum of all in transactions, from which we subtract out transactions occurring before or on day 10
    :param str:
    :return:
    '''
    command = [i for i in str.split() if i not in ['', ' ']]
    try:
        if len(command)>1:
            match command[1]:
                case "in":
                    for i in transactions:
                        if i[2]=="in":
                            print_transaction(i)
                case "out":
                    for i in transactions:
                        if i[2] == "out":
                            print_transaction(i)
                case ">":
                    value = int(command[2])
                    for i in transactions:
                        if i[1]>value:
                            print_transaction(i)
                case "=":
                    value = int(command[2])
                    for i in transactions:
                        if i[1] == value:
                            print_transaction(i)
                case "<":
                    value = int(command[2])
                    for i in transactions:
                        if i[1] == value:
                            print_transaction(i)

                case "balance":
                    day = int(command[2])
                    balance = 0
                    for i in transactions:
                        if get_day(i)==day:
                            if get_type(i)=="in":
                                balance+=get_value(i)
                            else:
                                balance-=get_value(i)
                    print(balance)
        else:
            for i in transactions:
                print_transaction(i)
    except:
        print("Error!")

def filter_transactions(str):
    '''
    filter <type>
    filter <type> <value>

    filter in – keep only in transactions
    filter in 100 – keep only in transactions having an amount of money smaller than 100 RON
    :param str: the user command to be parsed
    '''
    command = [i for i in str.split() if i not in ['', ' ']]
    try:
        match command[1]:
            case "in":
                if len(command)==2:
                    k=0
                    for i in range(len(transactions)):
                        if transactions[i-k][2]=="in":
                            del transactions[i-k]
                            k+=1
                else:
                    value=int(command[2])
                    k=0
                    for i in range(len(transactions)):
                        if transactions[i-k][2]=="in" and transactions[i-k][1]<value:
                            del transactions[i-k]
                            k+=1
            case "out":
                if len(command)==2:
                    k=0
                    for i in range(len(transactions)):
                        if transactions[i-k][2] == "out":
                            del transactions[i-k]
                            k+=1
                else:
                    value = int(command[2])
                    k=0
                    for i in range(len(transactions)):
                        if transactions[i-k][2] == "out" and transactions[i-k][1] < value:
                            del transactions[i-k]
                            k+=1
    except:
        print("Error!")

def undo(stack):
    '''
    undos the last command
    :param stack: the stack stores all the versions of the transactions list throughout the program
    :return:
    '''
    try:
        transactions = stack[len(stack)-2][:]
        del stack[len(stack)-1]
        print("Last command has been reverted!")
    except:
        print("Error!")