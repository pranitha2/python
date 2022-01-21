'''1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list: [1, 2, 3, 4]
Access list: [600, 700]
Access list: [100, 300, 500, 600, 800]
Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list: [10]
Access list: [ ]'''

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[-3:-1])
print(x[::2])
print(x[::-1])
print(x[5][5][0])
print(list())


'''2. Create a list of thousand numbers using range and xrange and see the difference between each
other.'''

print(list(range(1001)))
    
print(list(xrange(1001)))

'''3. How Tuple is beneficial as compared to the list?'''
#tuples are faster than lists because of constant set of values. tuples can be used as dict keys because of immutable values like strings, numbers.we can change elements in list.

'''4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
the number which is divisible by 3 and is a multiple of 2.'''
l1=[]
for i in range(1,101):
    if(i%3==0) and (i%2):
        l1.append(str(i))
print(','.join(l1))

'''5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index.'''
class Solution:
   def reverseVowels(self, s):
      chars = list(s)
      index = []
      vowels = []
      for i in range(len(chars)):
         if chars[i] in ['a','e','i','o','u']:
             vowels.append(chars[i])
         index.append(i)
      vowels = vowels[::-1]
      final = []
      ind = 0
      for i in range(len(chars)):
          if i in index:
              final.append(vowels[ind])
          ind += 1
      else:
         final.append(chars[i])
   str1 = ""
   return str1.join(final)
ob1 = Solution()
print(ob1.reverseVowels("hello"))
print(ob1.reverseVowels("programming"))

'''6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length.'''

def even_string(str):
    str = str.split(" ")
    for i in str:
        if len(i) % 2 == 0:
            print(len(i))

strings = "hello my name is abcede"
even_string(strings)

'''7. Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.'''


x=[1,2,3,4,5,6,7,8,9,-1]

def pairsum(x):
    n = len(x)
    final_sum = 8
    for i in range(0,n):
        for j in range(1,n):
            if x[i]+x[j] == final_sum :
                print((x[i],x[j]))
            
pairsum(x)
               

'''8. Write a program in Python to complete the following task:
    -->Create two lists such as even_list and odd_list
    -->Ask user to enter a number in the range of 1,50 and make sure if the entered number is
       even, append it to the even_list and if the entered number is odd append it to the odd_list.
    -->Keep that in mind you can only add 5 items in each list
   --> Make sure once you enter all the 5 elements, calculate the sum of the list and return the
      maximum of the list.'''

def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 
  

A=list()
n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First  List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
splitevenodd(A) 
      
'''9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab
Expected output: a=5 b=5 c=2'''

inp_str= "12abcbacbaba344ab"
out={x:inp_str.count(x) for i in set(inp_str)}
print("occuranceof all characters in 12abcbacbaba344ab is:\n" + str(out))


'''10. Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10).'''
def etuple(num):
    return tuple(filter(lambda x: x % 2 == 0,num))

print(etuple(range(1,11)))


