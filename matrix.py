def multiplication (a,b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
      print "Cannot multiply the two matrices"
      return

    C = [[0 for col in range(cols_b)] for row in range(rows_a)]
    

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                C[i][j] += a[i][k] * b[k][j]
    return C



x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

y = [[5,8],
    [6,7],
    [4,5]]

print(multiplication(x,y))