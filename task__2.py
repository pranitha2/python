'''1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string.'''

n=int(input("enter a number"))
if n%3==0:
    print("consultadd")
elif n%5==0:
    print("python training")
elif n%3==0 and n%5==0:
    print("consultadd - python training")
    

'''2. Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.
'''
num1=int(input("enter a number"))
num2=int(input("enter a number"))
print("enter the option")
a=int(input("enter a number from 1 to 5:"))
res=0
if a=='1':
    res=num1+num2
    print(res)
elif a=='2':
    res=num1-num2
    print(res)
elif a=='3':
    res=num1/num2
    print(res)
elif a=='4':
    res= num1*num2
    print(res)
elif a=='5':
    res= num1+num2/2
    print(res)
else:
    print("input is negative")
print(num1 ,a, num2,":",res)
            

'''3. Write a program in Python to implement the given flowchart:
'''

a=10
b=20
c=30
avg = (a + b + c)/ 3
print(f"avg = {avg}")

if avg > a and avg > b and avg > c :
    print("avg is higher than a, b, c.")
else:
    if avg > a and avg > b:
        print("avg is higher than a, b")
    else:
        if avg > a and avg > c:
            print("avg is higher than a, c.")
        else:
            if avg > b and avg > c :
                print("avg is higher than b, c")
            else:
                if avg > a :
                    print("avg is just higher than a.")
                else:
                    if avg > b:
                        print("avg is just higher than b.")
                    else:
                        if avg > c:
                            print("avg is just higher than c.")


'''4.Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”'''
while true:
    n= eval(input("enter a number: "))
    if n < 0:
        print("it's Over.")
        break
    else:
        print("Good Going.")
        continue

'''5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.'''

nl=[]
for x in range(2000, 3200):
    if (x%5==0) and (x%7==0):
        nl.append(str(x))
print (','.join(nl))



'''6. What is the output of the following code examples?

1.x=123
for i in x:
print(i)

2.i=0

while i < 5:
print(i)
i += 1
if i == 3:
break
else:
print(“error”)

3.count=0

while True:
print(count)
count += 1
if count >= 5:
Break'''
# in case 1 there will be an error in which int object will not be iterable.
# in case 2 the output is 0,error,1,error,2
# in case3 it will be 0,1,2,3,4
'''7.write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement'''
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    print(i)


'''8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2'''

str = input("enter a string")
digit=letter=0
for ch in str:
   if ch.isdigit():
      digit=digit+1
   elif ch.isalpha():
      letter=letter+1
   else:
      pass
print("Letters:", letter)
print("Digits:", digit)

print(f"letters: {count_str}\tDigits: {count_num}")

'''9. Read the two parts of the question below:
    Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
    Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct number)'''

import random
x=input()
y=random.randint[]
while True:
    if x==y:
        print("same number")
    else:
        continue

    
'''10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
counter=1

While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.'''
import random
counter = 1
while counter <=5:
    answer = random.randint(1,100)
    print(f"the lucky nuuner {answer}")
    n = eval(input("Guess  number from 1 to 100: "))
    if n == answer:
        print("Good guess.")
    else:
        print("Try again!")
    if counter == 5:
        print("Game over.")
    counter +=1

'''11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.'''
import random
counter = 1
while counter <=5:
    answer = random.randint(1,100)
    print(f"the lucky number is: {answer}")
    n = eval(input("Guess number from 1 to 100 "))
    if n == answer:
        print("Good guess")
        break
    else:
        print("Sorry but that was not very successful.")
    if counter == 5:
        print("Game over.")
    counter +=1
