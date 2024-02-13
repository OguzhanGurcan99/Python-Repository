omega_gon = 2.05968
phi_gon = 0.67409
kappa_gon = 199.23470

omega_radian = omega_gon * 0.0157079633
phi_radian = phi_gon * 0.0157079633
kappa_radian = kappa_gon * 0.0157079633
# Since the built-in " math library " of python works with radian values by default, rotation angles converted to the radian

import math
r11 = ( math.cos(phi_radian) * math.cos(kappa_radian) )  + ( math.sin(phi_radian) * math.sin(omega_radian) + math.sin(kappa_radian) )
r12 = math.cos(omega_radian) * math.sin(kappa_radian)
r13 = ( -math.sin(phi_radian) * math.cos(kappa_radian) ) + ( math.cos(phi_radian) * math.sin(omega_radian) * math.sin(kappa_radian) )
r21 = ( -math.cos(phi_radian) * math.sin(kappa_radian) )  + ( math.sin(phi_radian) * math.sin(omega_radian) * math.cos(kappa_radian) )
r22 = math.cos(omega_radian) * math.cos(kappa_radian)
r23 = (math.sin(phi_radian) * math.sin(kappa_radian) ) + (math.cos(phi_radian) * math.sin(omega_radian) + math.cos(kappa_radian) )
r31 = math.sin(phi_radian) * math.cos(omega_radian)
r32 = - math.sin(omega_radian)
r33 = math.cos(omega_radian) * math.cos(phi_radian)
# Rotation matrix elements are defined

Tx = 497113.220 - 497049.238
Ty = 5419946.461 - 5420301.525
Tz = 287.650 - 1163.806
# Translation parameters are calculated by taking difference between "projection centre coordinates " and any given point coordinates

rotation_translation_elements = [ [r11,r12,r13,Tx] ,[r21,r22,r23,Ty]  ,[r31,r32,r33, Tz]  ]

focal_length = 120   # milimeter
row_pixel_number = 6912
column_pixel_number = 3840
f_pixel_number = 10000
pixel_size = 0.012    # milimeter
# Given values

Sx = ( row_pixel_number * pixel_size ) / f_pixel_number
Sy = ( column_pixel_number * pixel_size ) / f_pixel_number
# Scale factor of pixels are defined using given values

f11 = focal_length / Sx
f12 = 0
f13 = 0     # Ox = 0
f21 = 0
f22 = focal_length / Sy
f23 = 0     # Oy = 0
f31 = 0
f32 = 0
f33 = 1
# Perspective projection matrix elements are defined

perspective_elements = [ [f11,f12,f13] ,[f21,f22,f23], [f31,f32,f33]   ]

# GENERATING MATRICES
import numpy as np

world_coordinates_matrix  = np.zeros(shape= (4,1))
rotation_translation_matrix = np.zeros(shape=(3,4) )
perspective_projection_matrix = np.zeros(shape= (3,3) )
image_coordinates_matrix = np.zeros(shape=(3,1))
image_coordinates_matrix[2][0] = 1


row_rotation_translation_matrix = rotation_translation_matrix.shape[0]
column_rotation_translation_matrix = rotation_translation_matrix.shape[1]

row_perspective_projection_matrix = perspective_projection_matrix.shape[0]
column_perspective_projection_matrix = perspective_projection_matrix.shape[1]
# Row and column numbers of matrices are defined using  "shape " attribute

for i in range(row_rotation_translation_matrix):
    for j in range(column_rotation_translation_matrix):
        rotation_translation_matrix[i][j] = rotation_translation_elements[i][j]        # retrieve data from line 27

# Rotation - Translation matrix generation is completed

for i in range(row_perspective_projection_matrix):
    for j in range(column_perspective_projection_matrix):
        perspective_projection_matrix[i][j] = perspective_elements[i][j]          # retrieve data from line 51

# Perspective Projection matrix generation is completed


# MULTIPLYING MATRICES WITH FUNCTION
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

camera_coordinates = multiply_matrices(rotation_translation_matrix, world_coordinates_matrix )
image_coordinates_matrix = multiply_matrices( perspective_projection_matrix, camera_coordinates)

# image matrix = ( perspective_projection_matrix) x ( rotation_translation_matrix x world_coordinates_matrix ) procedure is implemented.
