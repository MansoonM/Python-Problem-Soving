#i row , j column

""" 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

print("First Pattern")

for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()


print("Second Pattern")
"""
*
* *
* * *
* * * *
* * * * *
"""
r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


print("Third Pattern")
"""
* * * * *
* * * *
* * *
* *
*
"""
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("Forth Pattern")
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
"""
m=6
for i in range(0,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
   

print("Fifth Pattern")
"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
k=5
for i in range(k,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


# for space
print(" ")


    # Print a square pattern n=5
n=5
for i in range(n):
    for j in range(n):
        print(" * ",end="")
    print()


# for space
print(" ")


#Increasing Triangle Pattern
n=5
for i in range(n):
    for j in range(0,i+1):
        print(" * ",end="")
    print()


# for space
print(" ")


#decreasing Triangle Pattern
n=5
for i in range(n):
    for j in range(i,n):
        print(" * ",end="")
    print()
    