input_array = [2,3,5,7,9]
target = 2

def binary_search(input_array, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if input_array[mid] == target:
        return mid
    elif input_array[mid] > target:
        return binary_search(input_array, start, mid-1, target)
    else:
        return binary_search(input_array, mid+1, end, target)


result = binary_search(input_array, 0, len(input_array)-1, target)

print(f"Target value is at index: {result}")