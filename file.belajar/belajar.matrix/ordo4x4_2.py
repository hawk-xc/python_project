mat = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]

"""
# output
1 2 3 4
0 2 3 4
0 0 3 4
0 0 0 4
"""

for i in range(4):
    for j in range(4):
        if i == j:
            mat[i][j] = i+1
        if i < j:
            mat[i][j] = j+1
        if i > j:
            mat[i][j] = 0


# cetak bentuk mat
for i in range(4):
    print(mat[i])