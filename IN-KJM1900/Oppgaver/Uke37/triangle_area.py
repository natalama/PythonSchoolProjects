import math


def test_triangle_area():
    v1 = (0, 0)
    v2 = (1, 0)
    v3 = (0, 2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg


def triangle_area(vertices):
    v1 = vertices[0]
    v2 = vertices[1]
    v3 = vertices[2]

    x1 = vertices[0][0]
    x2 = vertices[1][0]
    x3 = vertices[2][0]

    y1 = vertices[0][1]
    y2 = vertices[1][1]
    y3 = vertices[2][1]



    print("area = (1/2) * |(x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)+(x2*y1)|")
    print(f"area = (1/2) * |({x2}*{y3})-({x3}*{y2})-({x1}*{y3})+({x3}*{y1})+({x1}*{y2})+({x2}*{y1})|")
    area = (1/2) * abs((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)+(x2*y1))
    print(f"leaving function triangle_area(). returning area = {area}")
    return area


test_triangle_area()

r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke37> python .\triangle_area.py
Entered function triangle_area(). Getting vertices from vertices: [(0, 0), (1, 0), (0, 2)]
area = (1/2) * |(x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)+(x2*y1)|
area = (1/2) * |(1*2)-(0*0)-(0*2)+(0*0)+(0*0)+(1*0)|
leaving function triangle_area(). returning area = 1.0
"""
