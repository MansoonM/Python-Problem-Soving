#using third variable

a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
print("Before swapping a is ",a,",   b is ",b)

temp=a
a=b
b=temp

print("After swapping a is ",a,",    b is ",b)



#without using third variable

# x,y =y,x
x= int(input("Enter a number: "))
y= int(input("Enter a number: "))
print("Before swapping x is ",x,",   y is ",y)

x,y=y,x
print("After swapping x is ",x,",   y is ",y)