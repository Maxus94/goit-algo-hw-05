def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter = 0
    closest_high = high
    
    if x < arr [0]:
        return (1, arr[0])
    if x > arr [len(arr) - 1]:
        return (1, None)
    
    while low <= high:
        iter +=1
        mid = (high + low) // 2
        
        if arr[mid] < x:
            low = mid + 1
        
        elif arr[mid] > x:
            high = mid - 1
            closest_high = mid

        else:
            return (iter, arr[mid])
    
    return (iter, arr[closest_high])

arr = [2.9, 3.9, 4.1, 10.8, 40.7]
x = 7
result = binary_search(arr, x)
print(result)