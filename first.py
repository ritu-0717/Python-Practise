#List of city

listofcities = ['pune','mumbai','delhi','kolkata']
print(listofcities)
usercity=input('enter your city ')
print(usercity)

if usercity in listofcities :
 print('user is present in the list of cities')
else:
 print("user is not present in usercity")


#  ==============================
# ARITHMETIC OPERATORS
# ==============================

# Q1. Create two variables a = 45 and b = 8.
# Print the result of:
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Exponent
# a=45
b=8
sum=a+b
sum=print('Addition is',sum)

sub=a-b
sub=print('subtract is',sub)

mul=a*b
mul=print('Multiplication is',mul)

div=a/b
div=print('Division is',div)

FD=a//b
FD=print('Floor division is',FD)

M=a%b
M=print('modulous is',M)

EX=a**b
EX=print('exponent  is',EX)


# Q2. Find the square of 18 using the exponent operator.

a=2**18 
print(a)
# Q3. Fi nd the cube of 7 using the exponent operator.

b=3**7
print(b)
# Q4. Find the remainder when 97 is divided by 6.

a=97%6
print (a)

# Q5. Find how many complete groups can be made if 95 chocolates
# are distributed equally among 8 students.

c=95//8
print(c)
# ==============================
# ASSIGNMENT OPERATORS
# ==============================

# Q6. Create a variable x = 20.
# Add 15 using += and print the result.
x=20
x+=15
print(x)
# Q7. Create a variable y = 80.
y=80
print(y)
# Subtract 25 using -= and print the result.
x-=25
print(x)
# Q8. Create a variable z = 9.
z=9
print(z)
# Multiply it by 7 using *= and print the result.
z*=7
print(z)

# Q9. Create a variable a = 100.
# Divide it by 4 using /= and print the result.
a=100
a/=4
print(a)

# Q10. Create a variable b = 53.
# Find the remainder when divided by 6 using %=.
b=53
b%=6
print(b)

# Q11. Create a variable c = 49.
# Perform floor division by 5 using //=.
c=49
c//=5
print(c)

# Q12. Create a variable d = 3.
# Raise it to the power 5 using **=.
d=3
d**5
print(d)




# ==============================
# COMPARISON OPERATORS
# ==============================

# Q13. Create a = 25 and b = 30.
# Print the result of:
# a == b
# a != b
# a > b
# a < b
# a >= b
# a <= b
a=25
b=30
c=a==b
print(c)

d=a!=b
print(d)

h=a<b
print(h)

e=a>b
print(e)

f=a>=b
print(f)

d=a<=b
print(d)

# Q14. Check whether 100 is equal to 100.
a=100
b=100
if 100==100 :  
  print('100 is equal to 100')

# Q15. Check whether 75 is greater than 90.
if 75>90:
 print('yes')
else:
  print('No')
# Q16. Check whether 60 is less than or equal to 60.
if 100<=60:
  print('60 is less than or equal to 60.')
else:
  print('no')
  

# ==============================
# LOGICAL OPERATORS
# ==============================

# Q17. Create age = 22.
# Check if age is greater than 18 AND less than 60.
age=61
if age>18 and age<60:
 
 print('age is greater than 18 AND less than 60.')
else:
  print('no')
# Q18. Create marks = 85.
# Check if marks are greater than 90 OR equal to 85.
marks=80
if marks>90 or marks==85:
  print('true')

 
# Q19. Create x = 15.
# Use NOT to reverse the result of x > 20.

x=15
print(not(x>20))
# ==============================
# IDENTITY OPERATORS
# ==============================

# Q20. Create two variables:
# a = [10, 20, 30]
# b = a
# Check a is b and a == b.
a = [10, 20, 30]
b = a
if a is b and a == b:
  print('a is b and a == b.')

# Q21. Create:
# x = [1,2,3]
# y = [1,2,3]
# Check x == y and x is y.

x = [1,2,3]
y = [1,2,3]
if x == y and x is y:
  print(' x == y and x is y.')
else:
  print('no')
# ==============================
# MEMBERSHIP OPERATORS
# ==============================

# Q22. Create a list of 10 fruits.
# Check if "Apple" is in the list.
fruits=['apple','kiwi','mango','orange','grapes','pineapple']
print(fruits)
if 'apple' in fruits :
  print('Apple" is in the list.')
else:
  print('Apple" is not in the list.')

# Q23. Check if "Kiwi" is NOT in the list.
fruits=['apple','kiwi','mango','orange','grapes','pineapple']
print(fruits)
if 'kiwi'  not in fruits :
  print('kiwi" is  not in the list.')
else:
  print('kiwi" is in the list.')

# Q24. Create a string:
# language = "Python Programming"
# Check whether "P" is in the string.
language = "Python Programming"
if "P" in language:
  print("P is in the string.")
else:
  print('"P" is  not in the string.')

# Q25. Check whether "Java" is in this list:
# ["Python", "C", "Java", "SQL"]
list=["Python", "C", "Java", "SQL"]
print(list)
if "Java" in list:
  print('java" is  in the list.')
else:
  print('java"is not in the list')
 
# ==============================
# MIXED QUESTIONS
# ==============================

# Q26. Create a program that takes two numbers
# and prints all arithmetic operators.
a=6
b=4
sum=a+b
sum=print('Addition is',sum)

sub=a-b
sub=print('subtract is',sub)

mul=a*b
mul=print('Multiplication is',mul)

div=a/b
div=print('Division is',div)

FD=a//b
FD=print('Floor division is',FD)

M=a%b
M=print('modulous is',M)

EX=a**b
EX=print('exponent  is',EX)


# Q27. Check whether a number is even or odd using %.
num=8
if num%2==0:
 print("nummber is even")
else:
  print("Number is odd")
# Q28. Check whether a number is positive, negative or zero.
num=8
if num<0:
 print("nummber is positive")
else:
  print("Number is negative")


 
# Q28. Create a simple calculator using +, -, *, / and %.
a=int(input('enter 1st number' ))
b=int(input('enter 2nd number' ))
select=input('Choose one operand +,-,*,/')

if select  == '+':
   sum=a+b
   print('addition is ',sum)
elif  select == '-':
    sub=a-b

    print('subtraction is ',sub)
elif  select == '*':
    mul=a*b
    print('multiplication is ',mul)
elif  select == '/':
    div=a/b
    print('division is ',div)
else :
    print('invalid operands ')
#29 1-10,30-40,60-70,90-100
num=int(input('enter your number'))
if num<=10:
   print('num is in range 1 to 10',num)
elif num>=30 or num<=40:
   print('num is in range 30 to 40 ',num)
elif num>=60 or num<=70:
   print('num is in range 60 to 70 ',num)
elif num>=90 or num<=100:
   print('num is in range 90 to 100 ',num)
else :
   print('invalid')


num=int(input('enter your number'))
if num<=10 :
   print('num is in range 1 to 10',num)
elif num>=30 or num<=40:
   print('num is in range 30 to 40 ',num)
elif num>=60 or num<=70:
   print('num is in range 60 to 70 ',num)
elif num>=90 or num<=100:
   print('num is in range 90 to 100 ',num)
else :
   print('invalid')

#Method 2

num=int(input('enter your number'))

if (num>=1 and num<=10) or   (num>=20 and num<=30) or    (num>=40 and num<=50) or (num>=60 and num<=70) or     (num>=90 and num<=100):
       print('number in 1-10,20-30,40-50,60-70,90,100  ',num)
else:
    print('not in sequence')

