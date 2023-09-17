def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a<b:
            return a
        elif a>b:
            return b
        else:
            return " Even numbers are equal"

    else:
        if a<b:
            return b
        elif a>b:
            return a
        else:
            return "Odd numbers are equal"


def animal_crackers(text):
    if text.split(" ")[0][0] == text.split(" ")[1][0]:
        return True
    else:
        return False


def makes_twenty(n1,n2):
    if n1+n2 == 20:
        return True
    elif n1 ==20 or n2 ==20:
        return True
    else:
        return False


def old_macdonald(name):
    first = name[0:3:1]
    second = name[3::1]
    a = first.capitalize()
    b = second.capitalize()
    return a+b


def find_33(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] == 3:
            if arr[i+1] == 3:
                return True
    return False


def summer_69(arr):
    x = 0
    summ = 0
    while x<len(arr):

        if arr[x]!=6:
            summ += arr[x]
        else:
            while True:
                if arr[x]==9:
                    summ+=0
                    break
                else:
                    summ+=0
                    x+=1
        x+=1
    return summ


def spy_game(nums):
    if nums.count(0)<2 or nums.count(7)<1:
        return False

    seven = 1
    search=1
    x = 0
    while x<len(nums) and (x+search+seven)<len(nums):
        if nums[x]==0:
            if nums[x+search]==0:
                if nums[x+search+seven]==7:
                    return True
                else:
                    seven+=1
            else:
                search+=1
        else:
            x+=1
    return False


def count_primes(num):
    primes=[]
    a = 2
    while a<=num:
        approve=[]
        check=[x for x in range(1,a)]
        for i in check:
            if a % i==0:
                approve.append(i)

        if len(approve)==1:
            primes.append(a)
        a+=1

    return len(primes)

