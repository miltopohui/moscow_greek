from tkinter import *

xmax = 720
ymax = 600

indent = 60
indent_2 = 30
radius = 1.5
wpoint = 2.5
gline = 4
wline = 3
usline = 1

root = Tk()
c = Canvas(root, width=xmax, height=ymax, bg='white')
c.pack()

root.title('Начертательная геометрия №1 Вар. (1-10)')

c.create_line(indent, ymax // 2, xmax - indent, ymax // 2, width=gline)  # ось х
c.create_line(xmax - indent, indent, xmax - indent, ymax - indent, width=gline)  # ось z-y


def point(xp, yp, kp):
    c.create_oval(xp + radius, yp + radius, xp - radius, yp - radius, width=kp)


def point1(xp, yp, kp):
    c.create_oval(xmax - indent - xp + radius, ymax // 2 - yp + radius, xmax - indent - xp - radius,
                  ymax // 2 - yp - radius, width=kp)


def point2(xp, yp, kp):
    c.create_oval(xmax - indent - xp + radius, ymax // 2 + yp + radius, xmax - indent - xp - radius,
                  ymax // 2 + yp - radius, width=kp)


def line1(x1, y1, x2, y2, kl):  # прямые на пл-ти xOz
    c.create_line(xmax - indent - x1, ymax // 2 - y1, xmax - indent - x2, ymax // 2 - y2, width=kl)


def line2(x1, y1, x2, y2, kl):  # прямые на пл-ти xOy
    c.create_line(xmax - indent - x1, ymax // 2 + y1, xmax - indent - x2, ymax // 2 + y2, width=kl)


with open("input.txt", "r") as file:
    i1 = file.readline()
    i2 = file.readline()
    i3 = file.readline()
    i4 = file.readline()
    i5 = file.readline()
    i6 = file.readline()
    i7 = file.readline()
    i8 = file.readline()
    i9 = file.readline()

Ax = int(i1)
Ay = int(i2)
Az = int(i3)
Mx = int(i4)
My = int(i5)
Mz = int(i6)
Nx = int(i7)
Ny = int(i8)
Nz = int(i9)

print('Ax: ', Ax)
print('Ay: ', Ay)
print('Az: ', Az)
print('Mx: ', Mx)
print('My: ', My)
print('Mz: ', Mz)
print('Nx: ', Nx)
print('Ny: ', Ny)
print('Nz: ', Nz)

# попытка сделать масштаб

k = 1.5

Ax = k * Ax
Ay = k * Ay
Az = k * Az
Mx = k * Mx
My = k * My
Mz = k * Mz
Nx = k * Nx
Ny = k * Ny
Nz = k * Nz

# построение осей

line1(Nx, Nz, Mx, Mz, usline)  # прямая m''n''
line2(Nx, Ny, Mx, My, usline)  # прямая m'm'
c.create_line(xmax - indent - Ax, ymax // 2 - Az, xmax - indent - Ax, ymax // 2 + Ay)  # прямая A"A'

point1(Ax, Az, wpoint)  # точка A''
point2(Ax, Ay, wpoint)  # точка A'
point1(Nx, Nz, wpoint)  # точка N''
point1(Mx, Mz, wpoint)  # точка M''
point2(Nx, Ny, wpoint)  # точка N'
point2(Mx, My, wpoint)  # точка M'

if (Mz == Nz) and (My != Ny):

    # нахождение ура-ия прямой m"n"

    k1 = ((My - Ny) / (Mx - Nx))
    b1 = (-My - k1 * (-Mx))

    # находжение ур-ия прямой, перпендикулярной m'm'

    k2 = (-1 / k1)
    b2 = -(Ay - k2 * Ax)

    x = (b2 - b1) / (k1 - k2)
    y = (k2 * x + b2)
    print('k1: ', k1, 'b1: ', b1)
    print('k2; ', k2, 'b2: ', b2)
    print(x, y)

    # ПЕРПЕНДИКУЛЯР!

    line2(Ax, Ay, -x, -y, usline)  # прямая A0A'
    c.create_line(xmax - indent + x, ymax // 2 - Nz, xmax - indent + x, ymax // 2 - y)
    line1(-x, Nz, Ax, Az, usline)  # прямая A"K"
    point2(-x, -y, wpoint)  # точка K'
    point1(-x, Nz, wpoint)  # точка К"

    # построение нат. вел. высоты AK

    b3 = - (Ay - k1 * Ax)
    l = Az - Nz
    sin = k1 / ((1 + k1) ** (1 / 2))
    cos = 1 / ((1 + k1) ** (1 / 2))
    ly = sin * l
    lx = cos * l

    line2(Ax, Ay, Ax + lx, Ay + ly, usline)  # прямая l( A0A')
    point2(Ax + lx, Ay + ly, wpoint)  # точка А0
    line2(Ax + lx, Ay + ly, -x, -y, usline)  # прямая K'A0
    l1 = (l ** 2 + (b3 - b1) ** 2) ** (1 / 2)
    KC = l1 * (1 / (3 ** (1 / 2)))

    print('b3: ', b3)
    print('l: ', l)
    print('lx: ', lx)
    print(('sinx: ', sin))
    print('l1 :', l1)
    print('x:', x)

    # построение вспомогательного треугольника

    point(indent_2, indent_2, wpoint)  # верхняя точка A
    point(indent_2, indent_2 + l1, wpoint)  # точка K
    point(indent_2 + KC, indent_2 + l1, wpoint)  # точка C

    c.create_line(indent_2, indent_2, indent_2, indent_2 + l1)  # прямая AK
    c.create_line(indent_2 + KC, indent_2 + l1, indent_2, indent_2 + l1)  # прямая KC
    c.create_line(indent_2, indent_2, indent_2 + KC, indent_2 + l1)  # прямая AC

    # откладываем K'B' и K'C'

    KC_x = KC * cos
    KC_y = KC * sin

    point2(-(x - KC_x), - y + KC_y, wpoint)  # точка B'
    point2(-(x + KC_x), - y - KC_y, wpoint)  # точка C'
    point1(-(x - KC_x), Mz, wpoint)  # точка B''
    point1(-(x + KC_x), Mz, wpoint)  # точка C''

    c.create_line(xmax - indent + x - KC_x, ymax // 2 - y + KC_y, xmax - indent + x - KC_x, ymax // 2 - Mz)  # B'B"
    c.create_line(xmax - indent + x + KC_x, ymax // 2 - y - KC_y, xmax + KC_x - indent + x, ymax // 2 - Mz)  # C'C"

    line2(-x + KC_x, -(y - KC_y), Ax, Ay, wline)  # A'B'
    line2(Ax, Ay, -(x + KC_x), - y - KC_y, wline)  # A'C'
    line1(-(x - KC_x), Mz, Ax, Az, wline)  # A"B"
    line1(-(KC_x + x), Mz, Ax, Az, wline)  # A"C"
    line1(-(x - KC_x), Mz, -(x + KC_x), Mz, wline)  # B"C"
    line2(-(x - KC_x), -y + KC_y, -(x + KC_x), -y - KC_y, wline)  # прямая B'C'

elif (My == Ny) and (Nz != Mz):

    # нахождение ура-ия прямой m"n"

    k1 = ((Mz - Nz) / (Mx - Nx))
    b1 = (-Mz - k1 * (-Mx))

    # находжение ур-ия прямой, перпендикулярной m'm'

    k2 = (-1 / k1)
    b2 = -(Az - k2 * Ax)

    x = (b2 - b1) / (k1 - k2)
    y = (k2 * x + b2)
    print('k1: ', k1, 'b1: ', b1)
    print('k2; ', k2, 'b2: ', b2)
    print(x, y)

    # ПЕРПЕНДИКУЛЯР!

    line1(Ax, Az, -x, -y, usline)  # прямая A0A'
    c.create_line(xmax - indent + x, ymax // 2 + Ny, xmax - indent + x, ymax // 2 + y)
    line2(-x, Ny, Ax, Ay, usline)  # прямая A"K"
    point1(-x, -y, wpoint)  # точка K'
    point2(-x, Ny, wpoint)  # точка К"

    # построение нат. вел. высоты AK

    b3 = - (Az - k1 * Ax)
    l = Ay - Ny
    sin = k1 / ((1 + k1) ** (1 / 2))
    cos = 1 / ((1 + k1) ** (1 / 2))
    ly = sin * l
    lx = cos * l

    line1(Ax, Az, Ax + lx, Az + ly, usline)  # прямая l( A0A')
    point1(Ax + lx, Az + ly, wpoint)  # точка А0
    line1(Ax + lx, Az + ly, -x, -y, usline)  # прямая K'A0
    l1 = (l ** 2 + (b3 - b1) ** 2) ** (1 / 2)
    KC = l1 * (1 / (3 ** (1 / 2)))

    print('b3: ', b3)
    print('l: ', l)
    print('lx: ', lx)
    print(('sinx: ', sin))
    print('l1 :', l1)
    print('x:', x)

    # построение вспомогательного треугольника

    point(indent_2, indent_2, wpoint)  # верхняя точка A
    point(indent_2, indent_2 + l1, wpoint)  # точка K
    point(indent_2 + KC, indent_2 + l1, wpoint)  # точка C

    c.create_line(indent_2, indent_2, indent_2, indent_2 + l1)  # прямая AK
    c.create_line(indent_2 + KC, indent_2 + l1, indent_2, indent_2 + l1)  # прямая KC
    c.create_line(indent_2, indent_2, indent_2 + KC, indent_2 + l1)  # прямая AC

    # откладываем K'B' и K'C'

    KC_x = KC * cos
    KC_y = KC * sin

    point1(-(x - KC_x), - y + KC_y, wpoint)  # точка B'
    point1(-(x + KC_x), - y - KC_y, wpoint)  # точка C'
    point2(-(x - KC_x), My, wpoint)  # точка B''
    point2(-(x + KC_x), My, wpoint)  # точка C''

    c.create_line(xmax - indent + x - KC_x, ymax // 2 + y - KC_y, xmax - indent + x - KC_x, ymax // 2 + My)  # B'B"
    c.create_line(xmax - indent + x + KC_x, ymax // 2 + y + KC_y, xmax + KC_x - indent + x, ymax // 2 + My)  # C'C"

    line1(-x + KC_x, -(y - KC_y), Ax, Az, wline)  # A'B'
    line1(Ax, Az, -(x + KC_x), - y - KC_y, wline)  # A'C'
    line2(-(x - KC_x), My, Ax, Ay, wline)  # A"B"
    line2(-(KC_x + x), My, Ax, Ay, wline)  # A"C"
    line2(-(x - KC_x), My, -(x + KC_x), My, wline)  # B"C"
    line1(-(x - KC_x), -y + KC_y, -(x + KC_x), -y - KC_y, wline)  # прямая B'C'


else:

    print('Слишком простой случай :D')

root.mainloop()
