nums = [n for n in range(1,6)] #номер 1
print(nums)

nums = [a for a in range(500)] #номер 2
print(nums)

world = 'Jordan' #номер 3
n = [a for a in world]
print(n)

numbers = [4, -2, 7, -4, 19] #номер 4 
new_nums = []
for num in numbers:
    if num > 0:
        new_nums.append(num)
print(new_nums)

nums = [1, 2, 3, 4, 5] #номер 5
squares = [n*n for n in nums]
print(squares)

names = ['Pavel','Jordan','Sasha'] #номер 6
names2 = [name for name in
names if 'l' in name]

matrix = [ #номер 7
    [x for x in range(1, 4)] 
    for y in range(1, 4)
]
print(matrix)

numbers = [13, 21, 14, 24, 53, 62] #номер 8
  
filtered_nums = set() 
  
for num in numbers: 
    if num % 2 == 0: 
        filtered_nums.add(num) 
  
print(filtered_nums)

