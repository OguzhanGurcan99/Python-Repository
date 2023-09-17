import cv2

img0 = cv2.imread('image0.png',0)
img1 = cv2.imread('image1.png',0)

x = img0.shape[0]
y = img0.shape[1]

step_size = 2
square_size = 10
coefficent = round(square_size / step_size)
threshold = 2500

for i in range(0,x,step_size):
  for j in range(0,y,step_size):
    total_difference = 0

    for k in range(square_size):
      for t in range(square_size):
        try:
          value1= img1[i*coefficent +k, j*coefficent+ t]
          value0 = img0[i*coefficent +k, j*coefficent+ t]
          total_difference += abs(int(value1) - int(value0))

        except IndexError:
          break

# (IMAGE1 - IMAGE0 ) view  is not much clear to determine differences.
# BY USING  THIS 4 FOR LOOPS , I TAKE ALL (10 x 10) SUBSETS OF IMAGE0 AND IMAGE1
# total_difference <<<  VARIABLE REFERS TO DIFFERENCE BETWEEN IMAGE0 AND IMAGE1 (in 10x10 subset)
# FOR EXAMPLE  <<< IMAGE0 : 15500 <<<  IMAGE1: 20000 <<<  TOTAL_DIFFERENCE : 4500 ( in 10x10 subset )

    if total_difference > threshold:

# If this condition is provided (total_difference > threshold)
# I would have reliable information about car's existence in that part of image .

      for k in range(square_size):
        for t in range(square_size):
          try:
            img1[i*coefficent +k, j*coefficent+ t] = 255

# img1[i*coefficent +k, j*coefficent+ t] = 255
#  PAINT THAT PART WHITE TO SEE IT OBVIOUSLY.

          except IndexError:
            break

    else:

#if total_difference > threshold    IS NOT PROVIDED
# IT MEANS THERE IS NO SIGNIFICANT DIFFERENCE BETWEEN IMAGES !!!

      for k in range(square_size):
        for t in range(square_size):
          try:
            img1[i*coefficent +k, j*coefficent+ t] = 0

#img1[i*coefficent +k, j*coefficent+ t] = 0
#  PAINT THAT PART BLACK TO SEE IT OBVIOUSLY.

          except IndexError:
            break
cv2.imwrite("questions2_cars.jpg",img1)

# IN FINAL "img1" IS A GOOD REPRESENTATION AND APPROXIMATION of REAL IMAGE.
# WHITE AREAS REPRESENTS CARS.

# --------------------------------------------------------------------------------

# PART 1 IS OVER    >>>   CAR"S ARE DETECTED
# PART 2 >>>>  AN ALGORITHM TO COUNT NUMBER OF CARS
lst = []
for i in range(x):
  for j in range(y):
    if img1[i,j] == 255:
      lst.append((i,j))

top_left_corner = 0
top_right_corner = 0
bottom_left_corner = 0
bottom_right_corner = 0

for pair in lst:

  left = (pair[0], pair[1] - 1 )
  up = (pair[0] - 1, pair[1])

  right = (pair[0], pair[1] + 1 )
  down = (pair[0] + 1, pair[1])

  if right not in lst:
    if down not in lst:
      bottom_right_corner += 1
    elif up not in lst:
      top_right_corner += 1
  elif left not in lst:
    if down not in lst:
      bottom_left_corner += 1
    elif up not in lst:
      top_left_corner += 1

print("NUMBER OF CARS: ", min([top_left_corner,top_right_corner,bottom_right_corner,bottom_left_corner]))

