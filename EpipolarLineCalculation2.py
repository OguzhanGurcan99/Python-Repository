import numpy as np
import scipy.io
from PIL import Image
# importing necessary libraries

mat13 = scipy.io.loadmat('Fmatrix13.mat')['F13']
mat23 = scipy.io.loadmat('Fmatrix23.mat')['F23']
im1 = Image.open('florence1.jpg')
im2 = Image.open('florence2.jpg')
im3 = Image.open('florence3.jpg')
# reading corresponding matrix files and image datas

def multiply_matrices(matrix_1 , matrix_2):

    row_1 = matrix_1.shape[0]
    column_1 = matrix_1.shape[1]
    row_2 = matrix_2.shape[0]
    column_2 = matrix_2.shape[1]
    # Defining input matrices row-column numbers

    result_matrix = np.zeros(shape= (row_1,column_2))
    for i in range(row_1):
        for j in range(column_2):
            for k in range(column_1):
                result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result_matrix
# A function is written to multiply given matrices

points_from_im1 = [(807,45, 1),
          (624,228, 1),
          (1359,534, 1),
          (1184,1607, 1),
          (219,1546, 1)]

points_from_im2 = [(1190,110, 1),
          (494,727, 1),
          (1235,537, 1),
          (890,1725, 1),
          (195,1709, 1)]

colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (187, 0, 255),
          (234, 255, 0)]

# Corresponding points from both im1 and im2 are selected

def calculateV(u, a, b, c):
    return int((-1*c - a*u)/b)


for point in points_from_im1:
    epipolar_line = multiply_matrices(mat13, np.array(point).reshape(3,1))
    for u in range(0, 1536):
        v = calculateV(u, epipolar_line[0], epipolar_line[1], epipolar_line[2])
        im3.putpixel((u,v), colors[points_from_im1.index(point)])

for point in points_from_im2:
    epipolar_line = multiply_matrices(mat23, np.array(point).reshape(3,1))
    for u in range(0, 1536):
        v = calculateV(u, epipolar_line[0], epipolar_line[1], epipolar_line[2])
        im3.putpixel((u,v), colors[points_from_im2.index(point)])

im3.save("question_2_epipolar_lines.png","PNG")

# First loop relates im1 and im3
# Second loop relates im2 and im3
# Intersection of epipolar lines are shown in the output
