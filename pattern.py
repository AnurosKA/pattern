
row=int(input("Enter the number of rows:"))
col=int(input("Enter the number of columns:"))
r=row*2
c=col*4
for i in range(r+1):
    if (i==0):
        for j  in range(c+1):
            if (j==0):
                print(" ", end=" ")
            elif(j!=0 and j%4==0):
                print(" ",end=" ")
            elif(j%8==1 or j%8==2 or j%8==3):
                print("_", end=" ")
            else:
                print(" ", end=" ")
        print()

    elif( i%2==1):
        for j in range(c+1):
            if((col%2==0 and i==1 and j==c)):
                print("",end=" ")
            elif(j%8==0):
                print("/",end=" ")
            elif(j%4==0):
                print("\\",end=" ")
            elif(j%8==1 or j%8==2 or j%8==3):
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print()
    else:

        for j in range(c+1):
            if ((col % 2 == 0 and i ==r and j == c)):
                print("", end=" ")
            elif(j%8==0):
                print("\\",end=" ")
            elif(j%4==0):
                print("/",end=" ")
            elif (j % 8 == 5 or j % 8 == 6 or j % 8 == 7):
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print()





