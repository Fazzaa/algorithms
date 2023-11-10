input_array = [2,3,5,7,9]
target = 7

def binary_search(input_array, target):
    start = 0
    end = len(input_array)-1

    while start <= end:
        mid = (start+end) // 2
        if input_array[mid] == target:
            return mid
        elif input_array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return -1

result = binary_search(input_array, target)

print(f"Target value is at index: {result}")