
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high + low) // 2
        guess = arr[middle]
        if guess == item:
            return middle
        elif guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return None




my_list = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
print(binary_search(my_list, 10))
