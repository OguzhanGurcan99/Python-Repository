import numpy as np
import scipy.io
from PIL import Image
# importing necessary libraries

mat23 = scipy.io.loadmat('Fmatrix23.mat')['F23']
im3 = Image.open('florence3.jpg')
# reading corresponding matrix file and image data

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

points = [(1190,110, 1),
          (494,727, 1),
          (886,1725, 1),
          (1235,537, 1),
          (1497,1566, 1),]

colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (187, 0, 255),
          (234, 255, 0)]
# 5 points and colors selected manually.

def calculateV(u, a, b, c):
    return int((-1*c - a*u)/b)

# a-b-c variables represent coefficients of calculated epipolar line
# u represents manually selected pixel in im3
# Function returns the value of "v" in im3


for point in points:
    epipolar_line = multiply_matrices(mat23, np.array(point).reshape(3,1))
    for u in range(0, 1536):
        v = calculateV(u, epipolar_line[0], epipolar_line[1], epipolar_line[2])
        im3.putpixel((u,v), colors[points.index(point)])

im3.save("question_1_epipolar_lines.png","PNG")

# Epipolar lines are calculated for all selected points and plotted in im3
