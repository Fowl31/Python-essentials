#!/usr/bin/env python3

#1 Even or odd

inp = int(input("Enter a num: "))

if inp%2 == 0:
    print(f"Number {inp} is even")
else:
    print(f"Number {inp} is odd")

#2 Positive, negative or zero
num = int(input("Enter a number: "))
if num > 0 :
    print(f"Number {num} is positive")
elif num == 0:
    print(f"Number {num} is 0")
elif num < 0 :
    print(f"NUmber {num} is negative")

#3 Voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#4 Grading system
student_score = int(input("Enter your score: "))
if student_score >= 90:
    print("Grade is an A")
elif 80<= student_score <= 89:
    print("Grade is a B")
elif 70<= student_score <= 79:
    print("Grade is a C")
elif 60<= student_score <= 69:
    print("Grade is a D")
elif student_score < 60:
    print("Grade is an F")

#5 Maximum of Two numbers
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))

if a > b:
    print(f"Number {a} is > {b}")
elif a == b:
    print(f"Both num1 and 2 are equal")
else:
    print(f"Number {b} is  > {a}")


#6 Personalized greeting

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")


#7 Calculating Area
length = int(input("Enter length of shape: "))
width  = int(input("Enter Width of shape: "))

area = length * width 

print(f"Area of the rectangle is {area} units^2")


#8 Formatting a price
price = float(input("Enter the price of item: "))
print(f"Formatted price is {price: .2f}")

#9 Creating a Table Row
name = input("Enter the name of item: ")
quantity = int(input("Enter quantity of item "))
print(f"|Item: [{name}] |Quantity: [{quantity}]|")

#10 Combining strings and numbers
string = input("Enter string: ")
num = int(input("Enter number: "))

print(f"{num} {string + 's' if num > 1 else string}")

#11 Full Name

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")

full_name = f"{first_name} {second_name}"
print(full_name)

#12 Creating a sentence 
word1 = input("Enter a word1: ")
word2 = input("Enter a word2: ")
word3 = input("Enter a word3: ")
print(word1 + word2 + word3, sep=' ', end = '\n')

#13 Adding a prefix

word = input("Enter a word: ")
new_word = 'pre' + word
print(f"New word: {new_word} ")


#14 Joining list elements
lst = ['Apples','Grapes','Pears','Mangoes','Oranges']
final_string = ''
for i in lst:
    final_string += i + ' '
print(final_string, end = '\n')


#15 Combining two sentences 
sentence1 = input("Enter sentence 1: ")
sentence2 = input("Enter sentence 2: ")

print(sentence1 + "\n" + sentence2, end = '\n' )

