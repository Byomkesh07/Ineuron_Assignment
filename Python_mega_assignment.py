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

#Q85. Write a Python program to find cumulative sum of a list.

l = [1,3,2,5,4]
m=[]
sum=0
for i in range(0,len(l)):
    sum = sum + l[i]
    m.append(sum)
print("Cumulative sum of list is ",m) 

#Q86. Write a Python program to check if a string is palindrome or not.

str1 = input("Enter the string: ")
if str1 == str1[ : : -1]:
    print(str1,"is a palindrome word")
else:
    print(str1,"is not a palindrome word") 

#Q87. Write a Python program to remove i'th element from a string.

str1 = input("Enter the string: ")
i = int(input("Enter the index which you want to remove: "))
rest_str= ""
for j in range(0,len(str1)):
    if j != i:
        rest_str = rest_str + str1[j]
print("The rest string is: ",rest_str)

#Q88. Write a Python program to check if a substring is present in a given string.

str1 = input("Enter the string: ")
substr = input("Enter the substring: ")
if substr in str1:
    print("substring is present in the string")
else:
    print("substring is not present in the string")   
    
#Q89. Write a Python program to find words which are greater than given length k. 

str1 = input("Enter the sentence: ")
l = int(input("Enter the length: "))
word = str1.split(" ")
ref_list=[]
for i in word:
    if len(i) > l:
        ref_list.append(i)
print("All words which are greater than ",l,"are ",ref_list)

#Q90. Write a Python program to extract unquire dictionary values.

test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}]
print("The original list : " + str(test_list))
res=[]
for i in test_list:
    res.extend(list(i.values()))
res=list(set(res))
print("The unique values in list are : " + str(res))

#Q91. Write a Python program to merge two dictionary.

dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
print("Dictionary No. 1 is : ", dict1) 
print("Dictionary No. 2 is : ", dict2)    
dict3 = dict1.copy()   
for k, v in dict2.items():   
    dict3[k] = v  
print("After merging of the two Dictionary ")  
print(dict3)
