file = open("day1.txt", "r")

# initialize variables
left_nums = []
right_nums = []
distance = 0 # this will be the total distance

# read the file and store the numbers in the lists
for line in file:
    left, right = map(int, line.strip().split())
    left_nums.append(left)
    right_nums.append(right)

print(left_nums)
# sort the lists
left_nums.sort()
right_nums.sort()

# calculate the distance
for i in range(len(left_nums)):
    if left_nums[i] > right_nums[i]:
        distance += left_nums[i] - right_nums[i]
    else:
        distance += right_nums[i] - left_nums[i]

print(distance)

file.close()

