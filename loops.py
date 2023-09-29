value =1 

while value < 10:
    print(value)
    value+=1

names = ["Dave","Sara","jonny"]
for name in names:
    print(name)
    if name == "Sara":
        break

# for x in "Mississippi":
#     print(x)

actions = ["code","eat"]

for name in names :
    for action in actions:
        print(name + " " + action)