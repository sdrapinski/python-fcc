def squered(num): return num*num
print(squered(2))

sum = lambda a,b : a+b

print(sum(1,2))

def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
print(addTen(7))



numbers = [3,4,5,6,12,23,21,22,56]

squered_nums = map(lambda num : num * num,numbers)

print(list(squered_nums))

filtered = filter(lambda num:num % 2 !=0,numbers)

from functools import reduce

total = reduce(lambda acc, curr:acc + curr,numbers)
print(total)