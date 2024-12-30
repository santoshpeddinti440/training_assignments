
# programs

# 1.check the number is even or odd
# 2. largest number
# 3. factorial of a number
# 4. fibonacci number
# 5. check prime number
# 6. reverse string
# 7. palindrome check
# 8. swap two numbers
# 9. smallest number
# 10. sort number
# 11. sum of numbers
# 12. count the repeated numbers
# 13. simple star pyramids
# 14. right-angled triangle (left-aligned)
# 15. ring-angled triangle (right-aligned)
# 16.number triangle
# 17. find the percentage
# 18.find a string
# 19. capitalize the first letter of each string
# 20. concatenate the strings


#  1. check the number is even or odd
num=int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 2. largest number
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

print("Largest number is:",max(a,b,c))

# input: 10, 9,2   output: 10


# 3. Factorial of a number
def factiorial(n):
    return 1 if n==0 else n* factiorial(n-1)

num=int(input("Enter a number: "))
print("Factorial:",factiorial(num))

# input: 5  output: 120


# 4. fibonacci series

n=int(input("Enter number of terms: "))

a=0
b=1

for i in range(n):
     print(a,end=" ")
     a,b=b,a+b

# input : 3
# output: 0 1 1

# 5. check if a number is prime

num=int(input("Enter a number: "))

if num>1:
    for i in range(2,int(num*0.5)+1):
        if num%i == 0:
            print(f"{num} is not prime")
            break
    else:
       print(f"{num} is prime")
else:
    print(f"{num} is not prime")

# input: 6
# output: 6 is not prime

# 6. reverse a string

string=input("Enter a string: ")
print("Reversed string:", string[::-1])

# input: santosh
# output: hsotnas


# 7. palindrome check

string=input("Enter a string: ")

if string == string[::-1]:
    print(f"{string} is Palindrome")
else:
    print(f"{string} is Not a Palindrome")

# 8. swap two numbers

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

a,b=b,a

print("After swapping: a =", a, "b =", b)

# input a=10, b=20   output: a=20, b=10

# 9. smallest number

a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
c=int(input("Enter number c: "))

print("smallest number is: ",min(a,b,c))

# input:

# Enter number a: 112
# Enter number b: 56
# Enter number c: 27

# output: smallest number is: 27

# 10. sort the number

sort_numbers=[4,22,666,4,232,44,1,5353,55,33,20,10,2]

result=sorted(sort_numbers)

print(result)

# opt: [1, 2, 4, 4, 10, 20, 22, 33, 44, 55, 232, 666, 5353]

# 11.sum of numbers

sum=0

for i in range(1,15):

  sum+=i

print(sum)

# input 1, 15 numbers
# output: 105


# 12. count the repeated numbers

count_numbers=[2,3,2,3,4,3,4,4,3,11,12,15]

print(count_numbers.count(3))

# opt : 4

# 13. simple star pyramid

def star_pyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*" * (2*i-1))

star_pyramid(5)

# output:

#     *
#    ***
#   *****
#  *******
# *********

# 14. right-angled triangle (left-aligned)

def left_aligned_triangle(n):
    for i in range(1,n+1):
        print("*"* i)

left_aligned_triangle(5)

# output:

# *
# **
# ***
# ****
# *****

# 15. ring-angled triangle (right-aligned)

def right_aligned_triangle(n):
    for i in range(1,n+1):
        print(" "* (n-i)+"*" * i)

right_aligned_triangle(5)

# output:

#     *
#    **
#   ***
#  ****
# *****

# 16.number triangle

def number_traingle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")

        print()

number_traingle(5)

# output:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 17. find the percentage

def calculate_percentage(marks, total_marks):
    return (sum(marks) / total_marks) * 100

# Example usage
subjects = [85, 90, 78, 92, 88]
total_marks = 500

percentage = calculate_percentage(subjects, total_marks)
print(f"Percentage: {percentage:.2f}%")


# opt: 86.60%

# 18.find a string

def find_string(m_str, s_str):
    if s_str in m_str:
        return m_str.index(s_str)
    else:
        return -1

# Example usage
m_str = "Hello, welcome to the world santosh"
s_str = "santosh"



position = find_string(m_str, s_str)
if position != -1:
    print(f"'{s_str}' found at position {position}")
else:
    print(f"'{s_str}' not found in the string.")

# opt: 'santosh' found at position 28


# 19. capitalize the first letter of each string

def cap_first_letter(str):
    return str.title()

# Example usage
text = "hello santosh!"
result = cap_first_letter(text)
print(result)

# Hello Santosh!

# 20. concatenate the multiple strings

def cont_mul_str(*str):

    return ' '.join(str)

data = ["Python", "is", "awesome"]

result = cont_mul_str(*data)

print(result)

# opt: Python is awesome
