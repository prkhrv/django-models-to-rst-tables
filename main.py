row,column = 3,3

column_length = 12

for i in range((row*2)+1):
    if i % 2 == 0:
        print("+",end="")
    else:
        print("|",end="")
    for j in range(3):
        for k in range(column_length):
            if i % 2 == 0:
                print("-",end="")
            else:
                print(" ",end="")
        
        if i % 2 == 0:
            print("+",end="")
        else:
            print("|",end="")
    print()
