original_data = [0, 0, 5, 0, 0, 8, 1, 1]

class Triangle(object):
    x1 = original_data[0]
    y1 = original_data[1]

    x2 = original_data[2]
    y2 = original_data[3]

    x3 = original_data[4]
    y3 = original_data[5]


class M(object):
    x = original_data[6]
    y = original_data[7]


"""
Мат. часть - векторное и псевдоскалярное произведение.
Алгоритм: Считаются произведения (1,2,3 - вершины треугольника, 0 - точка):
(x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
(x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
(x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)
Если вектора одинакового знака, то точка лежит внутри треугольника, 
если какой либо вектор равен нулю, тогда точка лежит на стороне треугольника, 
иначе точка лежит вне треугольника.
"""
def solution():
    triangle = Triangle()
    point = M()

    vector1 = (triangle.x1-point.x)*(triangle.y2-triangle.y1)-(triangle.x2-triangle.x1)*(triangle.y1-point.y)
    vector2 = (triangle.x2-point.x)*(triangle.y3-triangle.y2)-(triangle.x3-triangle.x2)*(triangle.y2-point.y)
    vector3 = (triangle.x3-point.x)*(triangle.y1-triangle.y3)-(triangle.x1-triangle.x3)*(triangle.y3-point.y)

    if vector1 > 0 and vector2 > 0 and vector3 > 0:
        print("Yes")
    elif vector1 < 0 and vector2 < 0 and vector3 < 0:
        print("Yes")
    elif vector1 == 0 or vector2 == 0 or vector3 == 0:
        print("point on the side")
    else:
        print("No")


if __name__ == "__main__":
    solution()