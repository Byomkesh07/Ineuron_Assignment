# Q28. Write a code to get the desired output of the following

# string = "Big Data iNeuron"
# desired_output = "iNeuron"

str1 = "Big Data iNeuron"
print(str1[9 : 16])

# Q29. Write a code to get the desired output of the following

# string = "Big Data iNeuron"
# desired_output = "norueNi"

str1 = "Big Data iNeuron"
for i in range((len(str1)-1),8,-1):
    print(str1[i],end="")
