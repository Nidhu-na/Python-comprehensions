matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even=[n*n for r in matrix for n in r if n%2==0]
print(even)