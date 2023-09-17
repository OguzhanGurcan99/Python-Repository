# SEARCHING
def lineer_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return True
    return False


def smallest_item_search(arr):
    n = len(arr)
    smallest_item = arr[0]
    for i in range(1,n):
        if arr[i] < smallest_item:
            smallest_item = arr[i]

    return smallest_item


def binary_search(arr, target):
    n = len(arr)
    start = 0
    finish = n - 1

    while start <= finish:
        middle = ( start + finish ) // 2
        if arr[middle] == target:
            return True
        elif arr[middle] <  target:
            start = middle + 1
        else:
            finish = middle - 1

    return False
# Given array is sorted !


# SORTING
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range( n - (i+1)):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        smallest_index = i
        for j in range(i+1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            tmp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = tmp

    return arr


def insertion_sort(arr):
    n = len(arr)
    i = 1
    j = 1
    check = False

    while 0 < i < n:
        if arr[i] < arr[i-1]:
            tmp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = tmp
            i += -1

            if i == 0:
                i = j
            check = True

        else:
            i+= 1
            j += 1
            if check:
                i = j
    return arr


def merge_sort(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    a,b = 0,0
    sorted_array = []

    arr1_finish = False
    arr2_finish = False

    while (a < n1) or (b < n2):
        if arr1[a] < arr2[b]:
            sorted_array.append( arr1[a] )
            a += 1

            if a == n1:
                arr1_finish = True
                break
        else:
            sorted_array.append( arr2[b])
            b += 1

            if b == n2:
                arr2_finish = True
                break

    if arr1_finish:
        while b < n2:
            sorted_array.append( arr2[b])
            b += 1
    if arr2_finish:
        while a < n1:
            sorted_array.append( arr1[a])
            a += 1

    return sorted_array

ls1 = [1,5,9]
ls2 = [3,7,8,]
print(merge_sort(ls1,ls2))
