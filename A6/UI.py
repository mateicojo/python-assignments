import functions
from copy import deepcopy
import os

def menu():
    transactions = [
        [10, 150, "out", "pizza"],
        [12, 10, "out", "soda"],
        [14, 1200, "in", "salary"],
        [10, 200, "out", "clothes"],
        [10, 150, "out", "food"],
        [10, 150, "out", "meds"],
        [13, 199, "in", "slots"],
        [11, 120, "out", "drinks"],
        [11, 350, "in", "bonus"]
    ]
    stack=[]
    l=transactions[:]
    stack.append(l)
    while True:
        print("""
        Bank Account Application
        Choose one option below:
        (A) Add transaction
        (B) Modify transactions
        (C) Display transactions having different properties
        (D) Filter
        (E) Undo
        """) #prints menu with the available options
        ans = input(">")
        try:
            match ans:
                case 'A':
                    trans=input("""
                    add <value> <type> <description>
                    insert <day> <value> <type> <description>
                    """)
                    functions.add_transaction(trans)
                    l = transactions[:]
                    stack.append(l)
                case 'B':
                    trans = input("""
                    remove <day>
                    remove <start day> to <end day>
                    remove <type>
                    replace <day> <type> <description> with <value>
                    """)
                    functions.modify_transaction(trans)
                    l = transactions[:]
                    stack.append(l)
                case 'C':
                    trans = input("""
                    list
                    list <type>
                    list [ < | = | > ] <value>
                    list balance <day>
                    """)
                    functions.display_transactions(trans)
                case 'D':
                    trans = input("""
                    filter <type>
                    filter <type> <value>
                    """)
                    functions.filter_transactions(trans)
                    l = transactions[:]
                    stack.append(l)
                case 'E':
                    functions.undo(stack)
                    functions.display_transactions("list")
                case default:
                    raise ValueError
        except ValueError:
            print("Error!")



