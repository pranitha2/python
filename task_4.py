'''1. Write a program to reverse a string.
Sample input: “1234abcd”
Expected output: “dcba4321”'''

def reverse(string):
    return string[::-1]
print(reverse(input("enter  a string: ")))

'''2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12'''

def string(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
string("abcSdefPghijQkl")


'''3. Create a function that takes a list and returns a new list with unique elements of the first list.'''

def list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(list([1,2,3,3,3,3,4,5])) 


'''4.Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.'''

def sort(args):
    print(args)
    args = sorted(args)
    return ("-").join(args)

print(sort(input("enter words ").split("-")))


'''5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
Sample input: Hello world Practice makes man perfect
Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT'''


myString = 'Hello world Practice makes man perfect'

convertedString = myString.capitalize()

print('The first original string is : %s' %myString)
print('The first converted string is : %s\n' %convertedString)

'''6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console.'''
p = int(input("enter a  number "))
q = int(input("enter a number"))
sum = lambda p,q : p + q
print(sum(p,q))


'''7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.'''
str1=input("enter string")
str2=input("enter string")
a=len(str1)
b=len(str2)
if a>b:
    print(str1)
elif b>a:
    print(str2)
else:
    print(str1)
    print(str2)


'''8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).'''
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)
		
printValues()



'''9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
Sample input: show Numbers(3) (where limit=3)
Expected output:
0 EVEN
1 ODD
2 EVEN
3 ODD'''

def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(f'{i} EVEN')
        elif i % 2 != 0:
            print(f'{i} ODD')

showNumbers(int(input("enter number")))

'''10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)'''

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 
eve_num = map(lambda x: x**2, filter(lambda   x: x%2==0, li))
 
print(eve_num)

'''11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.'''

li = [1,2,3,4,5,6,7,8,9,10]
 
eve_num = map(lambda x: x**2, filter(lambda   x: x%2==0, li))
 
print(eve_num)

'''12. Write a function to compute 5/0 and use try/except to catch the exceptions'''

def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")
'''13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().'''
import functools
delim  =""
reduce_num = functools.reduce(lambda x, y: str(x) + delim + str(y),list(range(1,8)))
print(reduce_num)


'''14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.'''




nl=[]
for x in range(0,100):
    if (x%3==0) and (x%7==0):
        nl.append(str(x))
print (','.join(nl))



'''15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.
'''
def multiply(list):
    return list*list

print(list(map(multiply,eval(input("enter a list: ")))))



'''16. What is the output of the following codes:
(i) def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)
(ii) def a():
try:
f(x, 4)
finally:
print('after f')
print('after f?')
a()'''


# in case 1 the output is 2
# f is not defined in case 2


