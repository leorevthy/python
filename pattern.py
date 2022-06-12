
rows = int(input("Enter number of rows: "))
'''
for i in range(1,rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    
    print()
'''
print("--------------------------------")
'''
for i in range(rows,0,-1) :
    for j in range(1,i+1) :
        print("*", end=" ")
    
    print()
'''
print("--------------------------------")

space=rows
for i in range(1,rows+1) :
    print(space*" " + i*("* "))
    space=space-1

print("---------------")

for i in range(1,rows+1):
    for j in range(1, i+1):
        print(i, end=" ")
    
    print()
print("---------------")

for i in range(1,rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print("---------------------------------")

for i in range(1,rows+1):
    for j in range(1, i+1):
        print("{0}{1}".format(i,j), end=" ")
    print()
print("---------------------------------")
for i in range(1,rows+1):
    for j in range(1, i+1):
        print("{0}{1}".format(j,i), end=" ")
    print()
print("-------------------------")

ascii_value=65
for i in range(1,rows+1):
    for j in range(1, i+1):
        print("{0}".format(chr(ascii_value)), end=" ")
        ascii_value=ascii_value+1
    print()
print("-------------------------------")
ascii_value=64
for i in range(1,rows+1):
    for j in range(1, i+1):

        print("{0}".format(chr(ascii_value+j)), end=" ")
     
    print()
print("----------------------")

ascii_value=64
for i in range(1,rows+1):
    for j in range(1, i+1):

        print("{0}".format(chr(ascii_value+i)), end=" ")
     
    print()
print("---------------------")

sum=0
for i in range(1,rows+1):
    for j in range(1, i+1):
        sum=sum+1
  
        print("{0}".format(sum), end=" ")
     
    print()





