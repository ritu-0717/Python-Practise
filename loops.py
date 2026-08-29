

# 1. while loop
# while loop
# true
# while condition :
#code execute
# -----------------------------------------------------------------
# i=1
# while i<=5:
    
    # 1st iteration
    # i=1,i<=5 true

    # 2nd iteration
    # i=2,i<=5 true

    # 3rd
    # i=3,i<=5 true

    # 4th
    # i=4,i<=5 true

    # 5th
    # i=5,i<=5 true

    # 6th
    # i=6 ,i<=5 false

    
    # print(i)
    # i+=1
# -----------------------------------------------------------------------------------------------------------------------
#  2. for loop
# a=[1,2,3,4,5]
# for i in a :
#     # i variable
#     # a sequence
#     i=1
#     i=2
#     i=3
#     i=4
#     i=5
#     print(i)
# ------------------------------------------------------------------------------------------------------------------------

# 3.infinite loop

while True :
     print('hi')

# -----------------------------------------------------------------------------------------------------------------------------

# 4. RANGE FUNCTION

# range(start,stop,step)
# start - 1
# stop - 100
# step - 1

# a=list(range(1,100,1))
# print(a)
# --- ------------------------------------------------------------------------------------------------------------------------
# 5.nested loop

# for i in range (1,3):
      
#       i=1
#       i=2
      
#       j=3
#       j=4
#       j=5
      
#       for j in range(3,6) :
#           print(f'{i},{j}')
# n=10
# i=1
# while i<n:
#     print(i)
#     i+=1
# for i in range (1,10,1):
#     print(i)
#     if i==5 :
#         continue
# for i in range(1,10,1):
#     print(i)
#     if i==5:
#         break

# for i in range(1,10,1):
#     print(i)
#     if i==5 :
#         pass

# i=1
# n=10
# while i<n:
#      if i==5:
#          i=i+1
#          continue
#      print(i)
#      i = i + 1


# for i in range(1,10,1):
#     if i==5:
#         print('equal')
#     print(i)
# -------------------------------------------------------------------------------------------------------------------
# 6.Greater number 
# a=56
# b=19
#  if a>b:
#     print('a is greater than b')
# else:

#     print("b is greater than a")
#     '''
# if a%5==0:
#    print('a is divisible by 5')
# else:
#     print("a is not divisible by 5")
# print(a/5)

# -------------------------------------------------------------------------------------------------------------------

# 7. Check whether a student has passed (marks >= 40).
# marks=76
# if marks>=40:
#     print('student is pass')
# else:
#     print('student is fail')

# ---------------------------------------------------------------------------------------------------------------------
# 8. Find the largest among three numbers using if-elif-else.
# a=2
# b=4
# c=5
# if a>b&a>c:
#     print('a is greater')
# elif b>a&b>c:
#     print("a is greater ")
# else:
#     print("c is greater ")

# ---------------------------------------------------------------------------------------------------------------------------
# 9. Display grade based on marks:
#    90+  -> A
#    80-89 -> B
#    70-79 -> C
#    Below 70 -> Fail

# marks=int(input('enter your marks'))
#
# if marks<=90:
#     print("A")
# elif marks<=80:
#     print('B')
# elif marks<=70:
#     print('C')
# else :
#     print('student is fail')

# --------------------------------------------------------------------------------------------------------------------
# 10. Create a simple calculator using if-elif-else.
#  num1=int(input('enter a number'))
# num2=int(input('enter another number'))
# choice=input("enter your choice + ,*,/")
# if choice=='+':
#     print(num1+num2)
# elif choice=='*':
#     print(num1*num2)
# elif choice=='/':
#     print(num1/num2)
# else:
#     print("invalid choice")

# --------------------------------------------------------------------------------------------------------------------------

# 11. Print numbers from 1 to 50,
#     skip multiples of 5,
#     and stop at 40.

 # i=1
# n=50
#
# while i<=n:
#
#     if i==40:
#         break
#     if i % 5 == 0:
#         i = i + 1
#         continue
#     print(i)
#     i=i+1

# for i in range(1,50,1):
#     if i%5==0:
#         continue
#     print(i)


#  -----------------------------------------------------------------------------------------------------------------------
# 12. Create a menu-driven program:
#     1 -> Addition
#     2 -> Subtraction
#     3 -> Multiplication
#     4 -> Division

# num_1= float(input('enter your number '))
# num_2=float(input('enter your number '))
# choice=input("enter operators +,-,*,/ ")
# if choice=='+':
#     print(f'addition {num_1+num_2}')
# elif choice==('-'):
#     print (f'subtarction {num_1-num_2}')
# elif choice==('*'):
#     print(f'mulitiplication {num_1*num_2}')
# elif choice==('/'):
#     print(f'division {num_1/num_2}')
# else :
#     print('invalid operator')


