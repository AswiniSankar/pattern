/*
1
1 2
3 5 8
13 21 34 55
*/
#include<stdio.h>
int main()
{
 int n,i,j,a=0,b=1,c;
 scanf("%d",&n);
 printf("         %d\n",b);
 for(i=1;i<n;i++)
 {for(j=0;j<n;j++)
  {
    if(j<=i)
    {
    c=a+b;
    a=b;
    b=c; 
      printf("%10d",c);
    }
    else
     printf(" ");
 } 
 printf("\n");
 }
 return 0;
}
/*
0
0 1
0 1 1
0 1 1 2
0 1 1 2 3
*/
#include<stdio.h>
int main()
{
 int n,i,j,a=0,b=1,c=0;
 scanf("%d",&n);
 
 for(i=1;i<=n;i++)
 {for(j=1;j<=i;j++)
  { 
 
   
    a=b;
    b=c; 
    printf("%3d",c);
    c=a+b; 
  
 }
   a=0;
   b=1; 
   c=0;
 printf("\n");
 }
 return 0;
}
/*
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
*/
#include<stdio.h>
int main()
{
 int n,i,j,k;
 scanf("%d",&n);
 
 for(i=1;i<=n;i++)
 { k=i;
  for(j=1;j<=i;j++)
  { 
   printf("  %d",k);
    k=k+(n-j);
 }
  
 printf("\n");
 }
 return 0;
}

/*
1
2 4
1 3 5
2 4 6 8
1 3 5 7 9
*/
#include<stdio.h>
int main()
{
 int n,i,j,k;
 scanf("%d",&n);
 
 for(i=1;i<=n;i++)
 {if(i%2!=0)
  {k=1;
   for(j=1;j<=i;j++)
   { 
   printf("  %d",k);
    k=k+2;
   }
  }
  else
  { k=2;
    for(j=1;j<=i;j++)
    {
   
     printf("  %d",k);
    k=k+2;
    }
  }
  
 printf("\n");
 }
 return 0;
}
/*
     *
    ***
   *****
*/
#include<stdio.h>
int main()
{
 int n,i,j,k=1;
 scanf("%d",&n);
 for(i=0;i<n;i++)
 {
  for(j=n-1;j>=i;j--)
  {printf(" ");}
  for(j=0;j<k;j++)
  {printf("*");
  }
  k=k+2;
 printf("\n");
 }
 return 0;
}
/*
      1
   3  8  5
 7 9 40 11 13
*/
#include<stdio.h>
int main()
{
 int n,i,j,g,k=1,x=1;
 scanf("%d",&n);
 for(i=0;i<n;i++)
 {
  for(j=n-1;j>=i;j--)
   printf("   ");
  for(j=0;j<k;j++)
  {
    if(i==j)
    {g=(x+1)*(i+j);
     g=(g==0)?1:g;
     printf("%3d",g);
     continue;
    }
    x=x+2;
     printf("%3d",x);
  }
  k=k+2;
 printf("\n");
 }
 return 0;
}

/*
A
A B
A B C
A B C
A B
A
*/
#include<stdio.h>
#include<string.h>
int main()
{
 char str[20],c,d;
 scanf("%s",str);
 for(c=0;c<strlen(str);c++)
  {d=c+1;
   printf("%.*s\n",d,str);
  }
 for(c=strlen(str)-2;c>=0;c--)
   {d=c+1;
    printf("%.*s\n",d,str);
   }
 printf("\n");
 return 0;
}
