band = {
    "vocals":"John",
    "guitar": True
}

band2 = dict(vocals = "john",guitar = "Steve")

print(band)
print(band2)

band["vocals"] = "Piter"
band.update({"guitar":False})

member1 = {
    "name":"Steve"
}

member2 = {
    "name":"jonny"
}
bandWithMember = {
    "member1": member1,
    "member2": member2
}

print(bandWithMember["member1"]["name"])

#sets 

nums = {1,2,3,4}

nums2 = set((1,2,3,4,5))

numsWithDuplicates = {1,2,2,3,4,5,5}
print(numsWithDuplicates)