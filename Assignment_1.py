#16. Write a code that gives following as an output.
    #iNeuroniNeuroniNeuroniNeuron
    
    print("iNeuron"*4)

#17. Write a code to take a number as an input from the user and check if the number is odd or even.

#Decalaring Variables

a=int(input("Enter a No.: "))
if (a%2==0):
    print("The No. ",a," is an Even Number")
else:
    print("The No. ",a," is an odd Number")   

#22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

#Declaring Variables

age= int(input("Enter Your Age: "))
if (age>=18):
    print("I can vote")
else:
    print("I can't vote")

#23. Write a code that displays the sum of all the even numbers from the given list.

num = [12, 75, 150, 180, 145, 525, 50]
sum=0
for i in num:
   if (i%2==0):
    sum=sum+i
print("The sum of the given even numbers is ",sum)

#24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))
c = int(input("Enter third no.: "))
if(a>b and a>c):
    print(a," is the greatest no among three numbers")
elif(b>a and b>c):
    print(b," is the greatest no among three numbers")
elif(c>a and c>b):
    print(c," is the greatest no among three numbers")
else:
    print("All are equal")

#25. Write a program to display only those numbers from a list that satisfy the following conditions
#- The number must be divisible by five.

a=[10,24,30,45,51,60,65]
for i in a:
    if(i%5==0):
        print(i)