'''
1. Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
'''
x,y,z= 'python',5.2, 1

'''
2. Create a variable of type complex and swap it with another variable of type integer.
'''
a=1+2j
b=7
print("values of a:",a, "and b:",b)
a,b =b,a
print("values of a:",a, "and b:", b)

'''
3. Swap two numbers using a third variable and do the same task without using any third variable.
'''
#using third variable

p=1
q=2
print( 'The values of p and q are:',p,q)
r=p
p=q
q=r
print("values of p:" ,p, "and q :", q)

#without

a=int(input("enter a number"))
b=int(input("enter a number"))
print("values of a:",a, "and b:",b)
a,b =b,a
print("values of a:",a, "and b:", b)



'''
4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version.
'''
#2.x
X= raw_input("enter a value")
print(X)
#3.x

Y= int(input("enter a number"))
print(Y)

'''
5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.
'''
print("enter a number between 1 to 10")
num1= int(input("enter a number"))
num2=int(input("enter a number:"))
z=num1+num2
print("sum:",z)
result=z+30
print("result:", result)

'''
6. Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string/etc
'''
num3=eval(input("enter a value:"))
print(type(num3))

'''
7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.
'''
Variable=('This is  an upper camelcase')
variable=('this is a lower camelcase')
variable=('this is a snakecase')
VARIABLE=('this is  an UPPERCASE')
'''
8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?
'''
#yes
a=1
a=1.2
print(a)
#output: 1.2


Variables are essentially like an empty box, that can contain something like a string, number, or other value. When you assign it a value, the box will contain that value, and when you reassign it, it will empty out the old value, and the new value will be placed inside of it.

