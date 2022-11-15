                                                              Assignment-1

1. Why do we call Python as a general purpose and high-level programming language?

Ans. Python language designed to be used for building software in a wide variety of application domains, across a multitude of hardware
 configurations and operating system, that's why it is called general purpose programming language.
- And also python is considered a high level programming language because it is highly abstracted from the Assembly Language used to provide
 instructions to the CPU.

2. Why is Python called a dynamically typed language?

Ans. Python is a dynamically typed language because the type of the variable is determined only during runtime.

3. List some pros and cons of Python programming language?

Ans. Pros - a. It's Simple.
                    b.It's Free.
                    c.It's Easy to Use.
                    d.It's Highly Compatible.
                    e.It is Object-Oriented.
                    f.It has Lots of Libraries.
                    g.It has Built-in Data Structures.
                    h.It's Widely Applicable.
        Cons-a. Poor Memory Efficiency.
                  b.Database Access.
                  c.Weak in Mobile Computing.
                  d.Runtime Errors.

4. In what all domains can we use Python?

Ans. a.Web development.
         b.Data science.
         c.OS development.
         d.Scientific programming.
         e.Gaming.

5. What are variable and how can we declare them?

Ans. A variable is a name which is given to a memory location i.e. a=5.
 
6. How can we take an input from the user in Python?

Ans. By using 'input( )' i.e. Name= input("Enter the name: ") or Age= int(input("Enter the age: ")) [int is used to typecast]

7. What is the default datatype of the value that has been taken as an input using input() function?

Ans. String

8. What is type casting?

Ans. Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

Ans. No. Because, python user input() function takes only one argument. 

10. What are keywords?

Ans. Keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes.

11. Can we use keywords as a variable? Support your answer with reason.

Ans. Keywords are some predefined and reserved words in python that have special meanings. Keywords are used to define the syntax of the coding. The keyword cannot
 be used as a variable name.

12. What is indentation? What's the use of indentaion in Python?

Ans. Indentation refers to the spaces at the beginning of a code line.
- Python indentation is a way of telling the Python interpreter that a series of statements belong to a particular block of code.

13. How can we throw some output in Python?

Ans. Name = Byomkesh
         print("The user name is ", Name)
  output : Byomkesh

14. What are operators in Python?

Ans. In Python, operators are special symbols that designate that some sort of computation should be performed.
e.g. + , - , * , / e.t.c.

15. What is difference between / and // operators?

Ans.  / is an assignment operator and // is a comparison operator. / operator is used to assign value to a variable and //operator is used to compare two-variable
 or constants.

18. What are boolean operator?

Ans. Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search, resulting in more focused
 and productive results.

19. What will the output of the following?
```
1 or 0 - 1

0 and 0 - 0

True and False and True - False

1 or 0 or 0 - 0
```

20. What are conditional statements in Python?

Ans. A conditional statement is used to handle conditions in the program. These statements guide the program while making decisions based on the conditions 
encountered by the program.

21. What is use of 'if', 'elif' and 'else' keywords?

Ans. 'if' , 'elif' , 'else' are conditional statements that is required when we want to execute code based on a particular condition.  If the condition for if is False ,
 it checks the condition of the next elif block and so on. If all the conditions are False , the body of else is executed.
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
