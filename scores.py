#!/usr/bin/python3

HS = 75

score = int(input("Enter num: "))
score2 = int(input("Enter num: "))
score3 = int(input("Enter num: "))


avg = (score + score2 + score3)/3
if avg>= HS:
    print("Congratulations total is greater than 75")
else:
    print(f"Average is {avg: ,.2f} is lower than {HS}") 
