variable1= "Hello"
variable2= "World "
result=variable1+variable2
result = result*2
print("#"*10)
print(result)
print("#"*10)

print(result.upper())
print(result.lower())
print(result.title())
# length of the string
print(len(result))
#replace char
print (result.replace("" ," _"))
#stripping in function
print(result.strip().replace(" ", " _"))

#find operation
print(result.find("World"))
#slicing
print(result[5:10])

#list
list1=[1,2,3,4,5,6] or list (1,2,3,4,5,6)
list1_1=list()

print(list1)
print(list1_1)

list2=["Hello", "World", "Yourname"]
list3= [1,2,3,"Hello"]
print(len(list1))


#append

list1.append(10)
print(list1)

result_list=list2+list3
print(result_list)


#extend

list2.extend(list3)
print(result_list)
print(list2)

resulted="-".join(result)
print(resulted)
#split

splited_resultc=result.split(" h")
print(splited_resultc)


#slicing lsit

list[:]
list[:5]
list[5:]
list[-2]
print(list1[5:])



print(list45[2:3])

list45[2:3]= variable1;



print(list45[-3:-2])
list45[-3:-2]= variable2;
result123= list45[2:3] + list45[-3:-2]
print(variable1 + variable2)

# add value not solved

#loop

listqwe =[]


for i in range(0,10,1):
        listqwe.append(i)
print(listqwe)



listasd=[]
for x in range(10):
    listasd.append(x)
print(listasd)
list45=[1,2,3,4,5,6,7]
value1 = list45[2]  # Extract the value at index 2 (which is now 8)
value2 = list45[-3]
sum_values = value1 + value2  # Add the two values together
print(sum_values)