# matriz espiral

matriz = [
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]

top, bottom = 0, len(matriz) - 1
left, right = 0, len(matriz[0]) - 1

# print column right
for i in range(bottom + 1):
    print(matriz[i][left], end=" ")