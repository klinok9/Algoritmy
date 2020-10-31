def bin_search(list1, item):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high)
        guess = list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [11, 2, 7, 1, 12]
print(bin_search(my_list, 12))
