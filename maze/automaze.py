# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 19:52:12 2017

@author: Sahba
"""

import random

matrix=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
row=0
col=0
c=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
way=[['','','',''],
   ['','','',''],
   ['','','',''],
   ['','','','']]

for k in range(10):
    x=random.randint(0,3)      #make barriers
    y=random.randint(0,3)
    matrix[x][y]=1
matrix[3][3]=0
matrix[0][0]=0
        
print (matrix)


for i in range (len(matrix)):
    for j in range (len(matrix)):
        c[i][j]=matrix[i][j]


for i in range (len(c)-1,0,-1):
    for j in range (len(c)-1,0,-1):
        if c[i-1][j]<= c[i][j-1]:
            c[i][j] +=c[i-1][j]
            way[i][j]='up'
        else:
            c[i][j] +=c[i][j-1]
            way[i][j]='left'
print (c)
print (way)
if c[3][3]==0:
    print("there is a way")
else:
    print("there is not any way")