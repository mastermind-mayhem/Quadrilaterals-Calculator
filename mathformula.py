def midpoint(ax, ay, bx, by):
    intger = ax + bx
    intger = intger / 2
    x = intger
    intger = ay + by
    intger = intger / 2
    y = intger
    print('MIDPOINT')
    print('('+str(x)+','+str(y)+')')
    print(' ')
    return x,y

def slope(ax, ay, bx, by):
    s1 = by - ay
    s2 = bx - ax
    print('SLOPE')
    print(s1)
    print('---')
    print(s2)
    print(' ')
    if s2 <= 0 and s1 >= 0:
        s1 = s1 * -1.0
        s2 = s2 * -1.0
    elif s1 <= 0 and s2 <= 0:
        s1 = s1 * -1.0
        s2 = s2 * -1.0
    if s1 == 0.0 or s1 == -0.0:
        s1 = 0
        s2 = 0
    if s2 == 0.0 or s2 == -0.0:
        s1 = 0
        s2 = 0

    return s1, s2

def distance(ax, ay, bx, by):
    one = bx - ax
    one = one * one
    two = by - ay
    two = two * two
    three = one + two
    # print('DISTANCE')
    print('sqr root of ->'+str(three))
    print(' ')
    return three

def quaddist(ax, ay, bx, by, cx, cy, dx, dy):
    print('DISTANCES')
    print('Dist: AB')
    d1 = distance(ax, ay, bx, by)
    print('Dist: BC')
    d2 = distance(bx, by, cx, cy)
    print('Dist: CD')
    d3 = distance(cx, cy, dx, dy)
    print('Dist: DA')
    d4 = distance(dx, dy, ax, ay)
    print('Dist: AC')
    d5 = distance(ax, ay, cx, cy)
    print('Dist: BD')
    d6 = distance(bx, by, dx, dy)
    return d1, d2, d3, d4, d5, d6

def quadslope(ax, ay, bx, by, cx, cy, dx, dy):
    print('SLOPES')
    print('Slope: AB')
    s11, s12 = slope(ax, ay, bx, by)
    print('Slope: BC')
    s21, s22 = slope(bx, by, cx, cy)
    print('Slope: CD')
    s31, s32 = slope(cx, cy, dx, dy)
    print('Slope: DA')
    s41, s42 = slope(dx, dy, ax, ay)
    print('Slope: AC')
    s51, s52 = slope(ax, ay, cx, cy)
    print('Slope: BD')
    s61, s62 = slope(bx, by, dx, dy)
    return s11, s21, s31, s41, s51, s61, s12, s22, s32, s42, s52, s62

def diagmid(ax, ay, bx, by, cx, cy, dx, dy):
    print('MIDPOINTS')
    print('Midpoint: AC')
    acx, acy = midpoint(ax, ay, cx, cy)
    print('Midpoint: BD')
    bdx, bdy = midpoint(bx, by, dx, dy)
    return acx, acy, bdx, bdy
