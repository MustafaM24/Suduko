from dokusan import generators
import numpy as np

initial_b= [ 
        [7, 8, 0, 4, 0, 0, 1, 2, 0], 
        [6, 0, 0, 0, 7, 5, 0, 0, 9], 
        [0, 0, 0, 6, 0, 1, 0, 7, 8], 
        [0, 0, 7, 0, 4, 0, 2, 6, 0], 
        [0, 0, 1, 0, 5, 0, 9, 3, 0], 
        [9, 0, 4, 0, 6, 0, 0, 0, 5], 
        [0, 7, 0, 3, 0, 0, 0, 1, 2], 
        [1, 2, 0, 0, 0, 7, 4, 0, 0], 
        [0, 4, 9, 2, 0, 6, 0, 0, 7] 
    ]

arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))
print("New Array Gen:")
new = arr.reshape(9,9)
print(new)
print(' ')
print("Old Array:")
print(initial_b)
newform = []
print("New in old format:")
# for i in new:
#     newform.append(i)
for i in range(0,len(new)):
    for j in range(0,len(new)):
        new[i][j] = int(new[i][j])
print(new)
test_list = ['1', '4', '3', '6', '7']
for i in range(0, len(test_list)):
    test_list[i] = int(test_list[i])
print(test_list)