rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))
matrix = []
print('enter the elements row wise:' )

for i in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)
transpose = [[matrix[j][i] for j in range(rows)] for i in range(columns)]

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTranspose of the Matrix:")
for row in transpose:
    print(row)   
    
