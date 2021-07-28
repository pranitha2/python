'''
1. Create a list of 10 elements of four different data types like int, string, complex and float.'''
my_list= [1,2,3,4,5.2,1+2j,'hi','python',9,10]

'''
2. Create a list of size 5 and execute the slicing structure
'''
my_list =[1,2,3,4,5]
print(my_list[1:5])
'''
3. Write a program to get the sum and multiply of all the items in a given list.
'''
l1=[1,2,2]
print(l1[0]+l1[1]+l1[2])
print(l1[0]*l1[1]+l1[2])
'''
4. Find the largest and smallest number from a given list.
'''
l2=[1,2,3]
print("the smallest is:",min(l2))
print("the largest is:" ,max(l2))
'''
5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list.
'''
my_list= [1,2,3,4,5,6]
print (my_list)
for i in my_list:
    if(i%2 ==0):
        my_list.remove(i)
print(my_list)

'''
6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included).
'''
def val():
    l=list()
    for i in range(1,31):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
val()
    
'''
7. Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]
'''
l1=[1,3,5,7,9,10]
l2=[2,4,6,8]
l1[-1:]=l2
print(l1)

'''
8. Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}
'''
def merge(a,b):
    res=a | b
    return res
a={1:10, 2:20}
b={3:30,4:40}
c=merge(a,b)
print(c)
'''
9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
'''
dct={x: x**2 for x in [1,2,3,4,5]}
print(dct)
'''
10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
'''
val=input("34,67,55,33,12,98")
list= val.split(",")
tuple=tuple(list)
print('list:',list)
print('tuple:',tuple)

