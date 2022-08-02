num_ini: int = int(5)
num_fin: int = int(25)
nums: [int] = []

for i in range(num_ini, num_fin+1):
    if(i % 2 == 1):
        nums.append(i)
print(nums)