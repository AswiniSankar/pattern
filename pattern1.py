'''
    *
   * *
  * * *
 * * * *
'''
n=int(input())
for i in range(1,n+1):
 for j in range(i,n):
   print(end=" ")
 for k in range(1,i+1):
   print("*",end=" ")
 print("\r")
'''
   1
  1 2 
 1 2 3 
1 2 3 4
'''
n=int(input())
for i in range(1,n+1):
 for j in range(i,n):
   print(end=" ")
 for k in range(1,i+1):
   print(k,end=" ")
 print("\r")
'''
   1
  2 3
 4 5 6
7 8 9 10
'''
n=int(input())
t=1
for i in range(1,n+1):
 for j in range(i,n):
   print(end=" ")
 for k in range(1,i+1):
   print(t,end=" ")
   t=t+1
 print("\r")
'''
     A
    B C
   D E F
  G H I J
'''
n= int(input())
t=65
for i in range(1,n+1):
 for j in range(i,n):
  print(end=" ")
 for k in range(1,i+1):
  u=chr(t)
  print(u,end=' ')
  t=t+1
 print("\r")


