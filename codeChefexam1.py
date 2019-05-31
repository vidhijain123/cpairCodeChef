#name:vidhijain
#date:30/05/19
#Problem Statement:Count number of pairs of even and odd index such that i<j
#author:vidhijain123
'''
Algorithm:
1. Start 
2. Read number of testcases
3. For each testcase read an number of integer
4. Read an array
5. loop i and j such that i<j
6. Make pair of even and odd indexed
7. Increament the count
8. Print the number of counts
9. Stop
'''

import array
arr=[]
t=int(input("Enter t"))
c=0
i=0
j=i+1
p=0
for p in range (t):
    n=int(input("Enter n"))
    arr=list(map(int,input().split()))
    for i in range (n):
        for j in range (i,n):
            if (arr[i]%2==0 and arr[j]%2!=0):
                c=c+1
    print(c)           
