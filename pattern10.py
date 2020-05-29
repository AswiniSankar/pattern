

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
n=int(input())
for i in range(n):
 for j in range(n):
   print('*',end=" ")
 print("\r")

'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
n=int(input())
for i in range(n):
 for j in range(n):
   print(i,end=" ")
 print("\r")

'''
1 2 3 4 5
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
n=int(input())
for i in range(n):
 for j in range(n):
   print(j+1,end=" ")
 print("\r")

'''
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
n=int(input())
t=65
for i in range(n):
 for j in range(n):
  print(chr(t),end=" ")
 t+=1
 print("\r")
'''
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
n=int(input())
t=65
for i in range(n):
 for j in range(n):
  print(chr(t),end=" ")
  t+=1
 t=65
 print("\r")
'''
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
'''
n=int(input())
t=65
for i in range(n):
 for j in range(n):
  print(chr(t+n-1),end=" ")
 t-=1
 print("\r")
'''
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
n=int(input())
t=65
for i in range(n):
 for j in range(n):
  print(chr(t+n-1),end=" ")
  t-=1
 t=65
 print("\r")
'''
4 4 4 4
3 3 3 3
2 2 2 2 
1 1 1 1
'''
n=int(input())
for i in range(n,0,-1):
 for j in range(n,0,-1):
   print(i,end=" ")
 print("\r")
4 3 2 1
4 3 2 1
4 3 2 1
4 3 2 1 


n=int(input())
for i in range(n,0,-1):
 for j in range(n,0,-1):
   print(j,end=" ")
 print("\r")
'''
* ! ! !
* * ! !
* * * !
* * * *
'''
n=int(input())
for i in range(n):
  for j in range(n):
    if  i>j or j==0 or i==j:
        print("*",end=" ")
    else:
        print(end="! ")
  print("\r")
'''
* * * *
  * * *
    * *
      *
'''
n=int(input())
for i in range(n):
  for j in range(n):
    if  i<j or i==0 or i==j:
        print("*",end=" ")
    else:
        print(end=" ")
  print("\r")
'''
1
2 2 
3 3 3
4 4 4 4
'''
n=int(input())
for i in range(n):
 for j in range(n):
   if j==0 or i>j or i==j:
     print(i+1,end=" ")
   else:
     print(end=" ")
 print("\r")

'''

1
1 2
1 2 3
'''

n=int(input())
for i in range(n):
 for j in range(n):
   if j==0 or i>j or i==j:
     print(j+1,end=" ")
   else:
     print(end=" ")
 print("\r")
'''
A
B B
C C C
D D D D
'''
n=int(input())
t=65
for i in range(n):
 for j in range(n):
   if j==0 or i>j or i==j:
     print(chr(t),end=' ')
   
   else:
     print(end='  ')
 t=t+1
 print('\r')

'''
A
B C
D E F
'''

n=int(input())
t=65
for i in range(n):
 for j in range(n):
   if j==0 or i>j or i==j:
     print(chr(t),end=' ')
     t=t+1
   else:
     print(end='  ')
 
 print('\r')
'''
A
A B
A B C

'''
n=int(input())
t=65
for i in range(n):
 for j in range(n):
   if j==0 or i>j or i==j:
     print(chr(t),end=' ')
     t=t+1
   else:
     print(end='  ')
 t=65
 print('\r')
'''
* * * *
*     *
*     *
* * * *
'''

n=int(input())
for i in range(n,0,-1):
 for j in range(n,0,-1):
  if i==n or j==n or i==1 or j==1:
    print("*",end=' ')
  else:
    print(end='  ')
 print('\r')
'''

* * * *
* * * 
* *
*

'''

n=int(input())
for i in range(n):
 for j in range(n,0,-1):
  if i==0 or j==n or i<j:
    print("*",end=' ')
  else:
    print(end='  ')
 print('\r')
'''
1 1 1 1
2 2 2 
3 3
4
'''

n=int(input())
for i in range(n):
 for j in range(n,0,-1):
  if i==0 or j==n or i<j:
    print(i+1,end=' ')
  else:
    print(end='  ')
 print('\r')
''' 
1 2 3 4
1 2 3
1 2
1
'''

n=int(input())
t=1
for i in range(n):
 for j in range(n,0,-1):
  if i==0 or j==n or i<j:
    print(t,end=' ')
    t=t+1
  else:
    print(end='  ')
 t=1
 print('\r')

'''
A B C D
A B C
A B
A
'''
n=int(input())
t=65
for i in range(n):
 for j in range(n,0,-1):
  if i==0 or j==n or i<j:
    print(chr(t),end=' ')
    t=t+1
  else:
    print(end='  ')
 t=65
 print('\r')
'''
A A A A
B B B
C C
D
'''
n=int(input())
t=65
for i in range(n):
 for j in range(n,0,-1):
  if i==0 or j==n or i<j:
    print(chr(t),end=' ')
    
  else:
    print(end='  ')
 t=t+1
 print('\r')
'''
4 4 4 4
3 3 3
2 2
1
'''


n=int(input())
for i in range(n,0,-1):
 for j in range(n):
  if i==n or j==0 or i>j:
    print(i,end=' ')
  else:
    print(end='  ')
 print('\r')
'''
4 3 2 1
4 3 2
4 3
4
'''
n=int(input())
t=n
for i in range(n,0,-1):
 for j in range(n):
  if i==n or j==0 or i>j:
    print(t,end=' ')
    t=t-1
  else:
    print(end='  ')
 t=n
 print('\r')
'''
D D D D
C C C
B B
A

'''

n=int(input())
t=65+n-1
for i in range(n,0,-1):
 for j in range(n):
  if i==n or j==0 or i>j:
    print(chr(t),end=' ')
  else:
    print(end='  ')
 t=t-1
 print('\r')











