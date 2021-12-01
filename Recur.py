# def Sum(current, target):
#     if current < target:
#         return current + Sum(current + 1, target)
#     else:
#         return current

# sum = Sum(1, 10)
# print(sum)


# def AllStartSubStrs(string, index):
#     substr = string[0:index]
#     print(substr)
#     index += 1
#     if index <= len(string):
#         AllStartSubStrs(string, index)

# def AllStartSubStrsIter(string):
#     for i in range(len(string)):
#         substr = string[0:i]
#         print(substr)



#AllStartSubStrs("MAAAAAAAAAT", 0)
#AllStartSubStrsIter("AllStartSubStrsIter")
