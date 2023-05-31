import math
import numpy as np
import sys

with open(sys.argv[1]) as file_1:
    arr1 = file_1.read().split() 
arr1 = [float(num) for num in arr1]
with open(sys.argv[2]) as file_2:
    arr2 = file_2.read().split() 
arr2 = [float(num) for num in arr2]
#Разбиение координат на x и y
x_point = np.array([])
y_point = np.array([])
if len(arr2)>100:
    exit()
for i in range(len(arr2)):
    if (i%2 == 0):
        x_point = np.append(x_point, arr2[i])
    else:
        y_point = np.append(y_point, arr2[i])

#координаты точки и радиус круга
x_circle = arr1[0]
y_circle = arr1[1]
r_circle = arr1[2]

# Параллельный перенос системы координат
for i in range(len(x_point)):
    x = x_point[i]-x_circle
    y = y_point[i]-y_circle
    # Теорема Пифагора
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    if (hypotenuse < r_circle):
        print("1")
    elif (hypotenuse == r_circle):
        print("0")
    else:
        print("2")