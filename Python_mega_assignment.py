# Q28. Write a code to get the desired output of the following

# string = "Big Data iNeuron"
# desired_output = "iNeuron"

str1 = "Big Data iNeuron"
for i in range((len(str1)-7),16,+1):
    print(str1[i],end="")
    or 
str1 = "Big Data iNeuron"
print(str1[9 : 16])

# Q29. Write a code to get the desired output of the following

# string = "Big Data iNeuron"
# desired_output = "norueNi"

str1 = "Big Data iNeuron"
for i in range((len(str1)-1),8,-1):
    print(str1[i],end="")

# Q33. How can you print the below string?

# 'iNeuron's Big Data Course'

str2="'iNeuron's Big Data Course'"
print(str2) 

# Q37. Write a code to access the word "iNeuron" from the given list.

# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]

lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]     
new=lst[4]
print(new[2])

# Q39. Add the word "Big" in the 3rd index of the given list.

# lst = ["Welcome", "to", "Data", "course"]

lst = ["Welcome", "to", "Data", "course"]
lst.insert(3, "Big")
print(lst)

# Q76. Write a Python program to find the factorial of a given number.

def fact(a):
    fact2=1
    for i in range(1, a+1):
        fact2=fact2*i
    return fact2
num=int(input("Enter a no.: "))
ans=fact(num)
print(ans)

# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100

p=int(input("Enter the priciple amount: "))
r=float(input("Enter the rate of interest: "))
t=int(input("Enter the time in year: "))
float_SI= (p*r*t)/100
print("The Simple Interst is: ",float_SI)

# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

p=int(input("Enter the priciple amount: "))
r=float(input("Enter the rate of interest: "))
t=int(input("Enter the time in year: "))
float_CI= p*(1+ r/100)**t
print("The Compund Interst is: ",float_CI)

# Q79. Write a Python program to check if a number is prime or not.

int_a=int(input("Enter the no.: "))
if (int_a==2):
    print("This is an even prime no.")
elif (int_a%2==0):
    print("This is not a prime no.")
else:
    print("This is a prime no.")

#Q80. Write a Python program to check Armstrong Number.

sum=0
num=int(input("Enter a no.: "))
temp=num
while temp>0:
    a=(temp%10)
    sum=sum+(a**3)
    temp=(temp//10)
if sum == num:
    print(num,"is an armstrong no.")
else:
    print(num,"is not an armstrong no.")     

#Q81. Write a Python program to find the n-th Fibonacci Number.

I cannot get it

#Q82. Write a Python program to interchange the first and last element in a list.

numbers = [12, 75, 150, 180, 145, 525, 50]
numbers[0]=50
numbers[6]=12
print(numbers)    

#Q83. Write a Python program to swap two elements in a list.

numbers = [12, 75, 150, 180, 145, 525, 50]
numbers[1]=numbers[3]
numbers[2]=numbers[5]
print(numbers)

#Q84. Write a Python program to find N largest element from a list.

n = int(input('Which largest you want? ')) 
l = [1,3,2,5,4] 
l.sort(reverse = True) 
print(l[n-1])    
