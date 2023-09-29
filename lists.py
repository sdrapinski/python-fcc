users = ['Dave','John','Sara']

print( "Dave" in users)

print(users.index('John'))
users.append("Steve")
print(users[0:2])

users.extend(['Piter',"jacob"])

users.remove('Dave')
print(users.pop())

del users[1]

users.sort(key=str.lower)


nums = [1,2,11,34,8,3,4,5,6,7]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

numsCopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

nums.sort()
print("-----------")
print(nums)
print(numsCopy)
print(mynums)
print(mycopy)

#tuples to są niezmienialne listy

myTuple = tuple(('Dave',42,'True'))
anotherTuple = (1,2,3,4,5,2,3,2,2)

print(anotherTuple)
(one,two,*hey) = anotherTuple
print(hey)
print(anotherTuple.count(2))