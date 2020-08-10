nums = [1, 23, 36, 456, 365, 765, 67, 45, 90, 904, 567, 894, 5493, 45, 675, 434, 968, 345, 346, 5474, 3453, 34]
largest = 0

for item in nums:
    if item > largest:
        largest = item

print(largest)
