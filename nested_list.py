nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[0][1])
print(nested_list[1][-1])

print("----iterating nested list----")

for x in nested_list:
    for y in x:
        print(y)

print("----nested list comprehension----")

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)
board2 = [["X" if num%2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(board2)

print("----exercise----")

answer = [[x for x in range(1,4)] for y in range(1,4)]    
print(answer)  

answer2 = [[x for x in range(10)] for y in range(10)]
print(answer2)