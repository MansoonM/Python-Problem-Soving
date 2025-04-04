#Using Methods


# MyList=[1,2,3,4]
# maximum= max(MyList)
# minimum= min(MyList)
# sum=maximum+minimum

# print("MyList ",MyList)
# print("maximum ",maximum)
# print("minimum ",minimum)
# print("sum ",sum)

arr=[2,4,1,6]
max=arr[0]
min=arr[0]
n=len(arr) #number of elements


# For Maximum Number

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)


# For Minimum Number
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)