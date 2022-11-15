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
