'''1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.'''
str1=input("enter a string")
for i in str1:
    if i.isupper():
print(str1)

'''2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also
Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}'''

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
result = {key:values for key,values in zip(students,subjects)}
print(result)

'''3. Learn More about Yield, next and Generators'''


'''4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”'''

def reverse(str1):
    length = len(str1)
    for i in range(length - 1, -1):
        yield str[i]
input = "Consultadd training"
for x in reverse(input):
    print(x)


'''5. Write an example on decorators.'''

def inc(x):
    return x+1
def dec(x):
    return x-1
def decorator(func,x):
    result=func(x)
    return result
