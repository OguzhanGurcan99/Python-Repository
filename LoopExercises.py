# 1
a = 0
while 0 <= a < 10:
    print(a)
    a+= 1

# 2
x = 1
while x<6:
    for i in range(1,x+1):
        print(i,end=" ")
    x+=1

# 3
number = int(input("Enter a number please:"))
sum_value = 0
for x in range(1,number+1):
    sum_value += x
print(sum_value)

# 4
number = int(input("Enter a number please:"))
for x in range(2,number+1):
    divide_ok = []
    for i in range(1,x+1):
        if x % i ==0:
            divide_ok.append(i)
    if len(divide_ok)==2:
        print(x)

# 5
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
position = 0
while position < len(my_list):
    print(my_list[position])
    position += 2

