'''
# 1*n matrix
a=[2,3,5]
print(a)
print(a[0])
'''
'''
# n*n matrix
a=[[2,3,5],[3,6,5]]
print(a)
print(a[1][1])
'''
'''
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][3] =", A[0][3])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])   # append is the keyword...

print("3rd column =", column)

'''


# following is the code for the matrix addition with use of nested loop 

# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

#print(X)

