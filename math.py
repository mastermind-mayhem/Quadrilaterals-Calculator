import os
import mathformula as m

def space():
    for _ in range(2):
        print(' ')

print('Point A')
ax = float(input('x: '))
ay = float(input('y: '))
print(' ')
print('Point B')
bx = float(input('x: '))
by = float(input('y: '))
print(' ')
print('Point C')
cx = float(input('x: '))
cy = float(input('y: '))
print(' ')
print('Point D')
dx = float(input('x: '))
dy = float(input('y: '))
space()
d1, d2, d3, d4, d5, d6 = m.quaddist(ax, ay, bx, by, cx, cy, dx, dy)

s11, s21, s31, s41, s51, s61, s12, s22, s32, s42, s52, s62 = m.quadslope(ax, ay, bx, by, cx, cy, dx, dy)

acx, acy, bdx, bdy = m.diagmid(ax, ay, bx, by, cx, cy, dx, dy)
# Diagonal midpoints are the same
print('Do the Diagonals share a midpoint')
if acx == bdx and acy == bdy:
    print('-------- PASSED')
    space()
    # Diagonals are purpendicular
    if s51 <= 0:
        s51 = s51 * -1.0
    if s61 <= 0:
        s61 = s61 * -1.0
    print('Are the diagonals purpendicular to each other')
    if s51 == s62 and s52 == s61:
        print('-------- PASSED')
        space()
        # Adjecent sides are purpendicular
        if s11 <= 0:
            s11 = s11 * -1.0
        if s21 <= 0:
            s21 = s21 * -1.0
        print('Are adjacent sides purpendicular to each other')
        if s11 == s22 and s12 == s21:
            print('-------- PASSED')
            space()
            print('Prediction: Square')
        else:
            print('--- FALSE -----')
            space()
            print('Prediction: Rhombus')
    else:
        print('--- FALSE -----')
        space()
        # Adjecent sides are purpendicular
        if s11 <= 0:
            s11 = s11 * -1.0
        if s21 <= 0:
            s21 = s21 * -1.0
        print('Are adjacent sides purpendicular to each other')
        if s11 == s22 and s12 == s21:
            print('-------- PASSED')
            print('Prediction: Rectangle')
        else:
            print('--- FALSE -----')
            space()
            print('Prediction: Paralellogram')
else:
    print('--- FALSE -----')
    space()
    # Diagonals are purpendicular
    if s51 <= 0:
        s51 = s51 * -1.0
    if s61 <= 0:
        s61 = s61 * -1.0
    print('Are the diagonals purpendicular to each other')
    if s51 == s62 and s52 == s61:
        print('-------- PASSED')
        space()
        print('Prediction: Kite')
    else:
        print('--- FALSE -----')
        space()
        # Are diagonals the same length
        print('Do the diagonals share the same length')
        if d5 == d6:
            print('-------- PASSED')
            space()
            print('Prediction: Isoceles Trapazoid')
        else:
            print('--- FALSE -----')
            space()
            print('Prediction: Trapazoid')
