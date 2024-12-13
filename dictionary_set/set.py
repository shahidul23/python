# collection = {1, 3, 4, 5, 7, 5, "hello", "world"}


# # print(collection)
# # print(len(collection))
# # print(type(collection))

# # Accessing empty set
# newSet = set()

# # print(newSet)  # Output: set()
# # print(type(newSet)) # Output: <class 'set'>

# newSet.add(2)
# newSet.add(1)
# newSet.add(5)
# newSet.add(1)
# # newSet.remove(1)

# newSet.add((2,3,4,5))
# newSet.add("Shaidul Ialam")
# newSet.add('A')
# # newSet.clear()

# print(len(newSet))

# print(newSet.pop())
# print(newSet)

# union set

set1 = {1,2,3,6,4}
set2 = {1,2,5,3,6,8,2}

unionSet = set1.union(set2)
print(unionSet)
# print(set1)
# print(set2)

#intersection
intersectionSet = set1.intersection(set2)
print(intersectionSet)