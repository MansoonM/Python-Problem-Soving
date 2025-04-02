# Access by using index

arrayForInt=[23,43,21,52,41]
arrayForString=["books","copies","pens","pencils","colors"]

print("First Index: ",arrayForInt[0]);
print("Second Index: ",arrayForInt[1]);
print("Second Index Onwards: ",arrayForInt[1:]);
print("Second Index Backwards: ",arrayForInt[:1]);
print("Last-First Index: ",arrayForInt[-1]);
print("Last-Second Index: ",arrayForInt[-2]);

print("  ")

print("First Index: ",arrayForString[0]);
print("Second Index: ",arrayForString[1]);
print("Second Index Onwards: ",arrayForString[1:]);
print("Second Index Backwards: ",arrayForString[:1]);
print("Last-First Index: ",arrayForString[-1]);
print("Last-Second Index: ",arrayForString[-2]);

# Access all elements by using for loop

for i in arrayForInt:
    print(i)

for x in arrayForString:
    print(x)