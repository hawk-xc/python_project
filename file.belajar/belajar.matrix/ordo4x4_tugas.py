# WAHYU TRI CAHYONO
# 12.1A.18
# UBSI KAMPUS SURAKARTA

mat = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]

"""
# output
1 4 4 4
3 1 3 3
2 2 1 2
1 1 1 1
"""

for i in range(4):
    for j in range(4):
        if i <= j:
            mat[i][j] = 1
        if i < j:
            mat[i][j] = 4 - i
        if i > j:
            mat[i][j] = 4 - i


# cetak bentuk mat
for i in range(4):
    print(mat[i])