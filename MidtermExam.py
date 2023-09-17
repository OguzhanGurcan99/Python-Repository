# Question 1
nums=["1","2","3","4"]
copy=["1","2","3","4"]
second_nums =[]
goal = []
for i in nums:
    nums = ["1","2","3","4"]
    nums.remove(i)
    second_nums = nums

    for j in second_nums:
        copy=["1","2","3","4"]
        collect = i+j
        copy.remove(i)
        copy.remove(j)
        for a in copy:
            final = collect + a
           # print(final)
            goal.append(final)
print(goal)

# Question 2
def order():
    x = int(input("Please enter your number:"))
    y = int(input("Please enter your number:"))
    z = int(input("Please enter your number:"))
    a = []
    a.append(x)
    a.append(y)
    a.append(z)
    return sorted(a)
order()

# Question 3
first_st = (input("string 1:"))
second_st = (input("string 2:"))
new_string = first_st + " " + second_st
print(new_string)

# Question 4
km = int(input("km value:"))
mile = (km)*(0.6214)
print(mile)
print(str(km)+" km is equal to "+str(mile)+ " miles")

# Question 5
km = (input("km value:"))
if km.isnumeric() and int(km)>0:
    mile = int((km))*(0.6214)
    print(mile)
else:
    print("invalid input")

# Question 6) A
myid= [2,1,9,6,7,5,6,9]
for i in myid:
    if i>4:
        print(i)

# Question 6) B
a = 0
while a<4:
    print(myid[a])
    a+=1
print("--------")

# Question 6) C
x = 0
for i in myid:
    if x!=5 and x<(len(myid)):
        print(myid[x])
    x+= 1

# Question 7
a = open("fruits.txt","w")
a.write("pear\napple\norange\nmandarin\nwatermelon\npomegranate")
a.close()

b = open("fruits.txt","r")
c = b.readlines()
for i in c:
    fruit = i.rstrip()
    print(len(fruit))
b.close()

# Question 8
dct = {"x":[i for i in range(11,21)],"y":[i for i in range(21,31)],"z":[i for i in range(31,40)]}
print(dct["x"][4])
print(dct["y"][4])
print(dct["z"][4])

# Question 9
sample_list = [2,4,6,7,11]
square = lambda x:x*x
cube = lambda x:x*x*x

squared_numbers = list(map(square, sample_list))
cubed_numbers = list(map(cube, sample_list))

print(squared_numbers)
print(cubed_numbers)

# Question 10
#Because of its attribute, we cant change or assign a new value to a tuple.
