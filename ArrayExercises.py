# 1
def second_smallest(arr):
    n = len(arr)
    smallest = min( arr[0] , arr[1]  )
    second_small = max( arr[0] , arr[1] )
    for i in range( 2,n):
        if arr[i] < smallest:
            second_small = smallest
            smallest = arr[i]
        else:
            if arr[i] < second_small:
                second_small = arr[i]
    return second_small

test_array = [3,1,4,5,2]
print(second_smallest(test_array))


# 2
def find_33(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] == 3:
            if arr[i+1] == 3:
                return True
    return False

print(find_33(test_array))


# 3
def find_pair(arr,target):
    pairs = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                pairs.append( (i,j) )
    return pairs


# 4
def recursive(arr1, ls):
    for i in arr1:
        if type(i) == int:
            ls.append(i)
        elif type(i) == list:
            recursive(i, ls )


def flatten_list(arr2):
    flat_list = []
    recursive(arr2 , flat_list)

    return flat_list
nested_list = [1, [2, 3], [4, [5, 6, [7]]]]
print(flatten_list(nested_list))


# 5
def find_smallest_missing_positive(nums):
    n = len(nums)
    # Step 1: Move all non-positive integers to the beginning of the array
    i = 0
    while i < n:
        if 1 <= nums[i] <= n and nums[ nums[i] - 1] != nums[i]:
            nums[ nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            #print(nums)
        else:
            i += 1
    #print(nums)

    # Step 2: Find the first missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            #print("first return")
            return i + 1

    # Step 3: If all positive integers are present, return the next one
    return n + 1
print(find_smallest_missing_positive([8,6,2,3,1]))

# 6
def biggest(arr):
    bigger = arr[0]
    n = len(arr)
    for i in range(n):
        if bigger < arr[i]:
            bigger = arr[i]
    return bigger

print(biggest([4,3,5,2,7]))

# 7
def reverse(arr):
    n = len(arr)
    for i in range(n//2):
        temp_store =  arr[i]
        arr[i] = arr[ n - (i +1) ]
        arr[ n - (i +1) ] = temp_store

    return arr

print(reverse( [3,4,2,6,0]) )
