# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.
import numpy as np
n = 2
m = 3
indices = [[0,1],[1,1]]
matrix=np.zeros((n,m))

# for i,j in indices:
#     matrix[i]+=1
#     for a in range(len(matrix)):
#         matrix[a][j]+=1

# a=sum(matrix[i][j]%2!=0 for i in range(n) for j in range(m))

# print(a)

# print(" ")
# print(matrix)

# print(i, " ", j)
dic_row = {}
dic_column = {}
for (r,c) in indices:
    dic_row[r] = dic_row.setdefault(r,0) + 1
    dic_column[c] = dic_column.setdefault(c, 0) + 1
print(dic_row)
print(dic_column)

res = 0
for i in range(n):
    for j in range(m):
        count = dic_row.get(i,0) + dic_column.get(j,0)
        if count % 2 == 1:res += 1
print(res)  