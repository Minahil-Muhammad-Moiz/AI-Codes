# Using in-built functions
mylist = [3, 1, 5, 2, 7, 9, 4]
print('Task01')
print("Minimum value:", min(mylist))
print("Maximum value:", max(mylist))

# Without using in-built functions.
mylist = [3, 1, 5, 2, 7, 9, 4]
minVal = maxVal = mylist[0]
for i in range(len(mylist)-1):
    if mylist[i] < minVal:
        minVal = mylist[i]
    elif  mylist[i] > maxVal:
        maxVal = mylist[i]
print('Task02')
print("Minimum value:", minVal)
print("Maximum value:", maxVal)

# Linear Search 
# def linear_search(array, target):
#     for i in range(len(array)):
#         if array[i] == target:
#             print("Target is found at index ", i)


# array = [2, 4, 0, 1, 9]
# target = 1
# result = linear_search(array, target)

# Binary Search
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

arraySorted = [0, 1, 2, 4, 5, 8, 9]
target = 5
result = binary_search(arraySorted, target)

if result is not None:
    print("Target found at index: ", result)
else:
    print("Target not found in list")