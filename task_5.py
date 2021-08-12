'''1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError'''
try:
    f1=open("testfile","w")
    f1.write("this is my file")
except syntaxerror:
    print("error: can\'t find file ")
    
'''2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.'''
import sys
def file1(temp):
    try:
        if sys.argv[0] == temp:
            with open(temp, 'r') as o:
                o.read()
        raise FileExistsError("incorrect, enter the  again: ")
    except FileExistsError:
        raise
file1(input('input:  '))


'''3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”'''

def multi_digits(x):
    try:
        if len(str(x))>4:
            raise ValueError(" enter only 4 digit number")
        elif len(str(x))<=3:
            raise ValueError("4 digits required")
        print(x)
    except:
        print("Please provide only four digits number.")
        raise


multi_digits(eval(input('enter number: ')))                


'''4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.'''

print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Hytu76E' and username=='bank_admin':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

'''5. Go through the link provided below to understand finally and raise concept:
https://www.programiz.com/python-programming/exception-handling'''

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)



'''6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present.'''

with open('doc.txt','w') as text:
    text.write("Hello I am a file \nWhere you need to return the data string \nwhich is of even length")
    text.write('\nMake sure you return the same link as it is present')
with open("doc.txt") as text:
    result = ""
    for i in text:
        read = i.split()
        for j in read:
            if len(j) % 2 == 0:
                result = result + " " + j

print(result)






