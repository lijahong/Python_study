 num1 = int(input())
 x = 1;
 for i in range(1,num1+1,1):
     if(i <= (num1//2)):
         for j in range(1,x+1,1):
             print("*",end = '')
         x += 2
     elif(i == (num1//2 + 1)):
         for j in range(1,x+1,1):
             print("*",end = '')
         x -= 2
     elif(i > (num1//2)):
         for j in range(1,x+1,1):
             print("*",end = '')
         x -= 2
     print("")
