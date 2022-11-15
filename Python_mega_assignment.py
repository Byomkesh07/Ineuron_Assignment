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
