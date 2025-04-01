#!/usr/bin/env python3

import sys

A = 0
B = 0
#B is amount of times to display "O"
C = 0
#C is number of spaces based on input
choice = " "

def get_input():
    global A,B,C,choice
    # Checks the arguments from terminal
    try:
        A = int(sys.argv[1])
    except ValueError:
        print("Must be an interger/float")

    if len(sys.argv) < 3:
        print("Missing direction argument")
        sys.exit(1)

    choice = sys.argv[2]
    if choice != "up" and choice != "down":
        print("Invalid input must be up or down")
        sys.exit(1)

    #Based on the choice these steps are take
    if choice == "up":
        C = A//2
        B = 1
    elif choice == "down":
        C = 0
    


#display "O", cut line, got to new line
def output1():
    global A, B, choice 
    if choice == "up":
        for i in range(B):
            print("O", end = "")
        print()
    elif choice == "down":
        print("O"*A)
        
# No. of spaces to begin with is base amnt/2 end is cut so that  "O" is
# displayed
def output2():
    global C
    for i in range(C):
        print(" ", end = "")
    
#Spaces are decreased by 1
#No of "O" increase by 
def adjust():
    global A, C, B, choice
    if choice == "up":
        C -= 1
        B += 2
    elif choice == "down":
        C += 1
        A -= 2


get_input()
if choice == "up":
    while B < A:
        output2()
        output1()
        adjust()
elif choice == "down":
    while A > 0:
        output2()
        output1()
        adjust()

