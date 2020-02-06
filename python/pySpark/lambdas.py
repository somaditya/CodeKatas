from functools import reduce

nums = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

filtered_list = list(filter(lambda x: (x % 2 != 0), nums))
print(filtered_list)

double_list = list(map(lambda x: x*2, filtered_list))
print(double_list)

sum = reduce((lambda x, y: x+y), double_list)
print(sum)
