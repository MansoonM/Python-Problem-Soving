#Solution 1
myList=[3,5,6,7,2,1]
print("MyList Before Swapping First and Last Elements ",myList)
(myList[0],myList[-1])=(myList[-1],myList[0])
print("MyList After Swapping First and Last Elements ",myList)

#Solution 2
MyList=[10,5,19,20]
temp=0
print("MyList Before Swapping First and Last Elements ",MyList)

temp=MyList[0]
MyList[0]=MyList[-1]
MyList[-1]=temp
print("MyList After Swapping First and Last Elements ",MyList)