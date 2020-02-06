# 1
temp = 38
f_temp = temp * 1.8 + 32

temp = f_temp

print(temp)

x = 9.5
y = 6
x = x + y
print(x)

x = 6
x += x - x
print(x)

# z = 4*--------8
# 8 = students
print((((3 ** 6))))

print(-(-(-(-(9)))))


# print(3+=5/2)

# abs

def abs_diff(a, b):
    diff = a - b
    if diff < 0:
        diff = -(diff)
    return diff


print(abs_diff(-3, -7))


def avg_grade(g1, g2, g3):
    return (g1 + g2 + g3) / 3


print(avg_grade(100, 50, 30))


def avg_top_3(g1, g2, g3, g4):
    if g1 < g2 and g1 < g3 and g1 < g4:
        return avg_grade(g2, g3, g4)
    elif g2 < g1 and g2 < g3 and g2 < g4:
        return avg_grade(g1, g3, g4)
    elif g3 < g1 and g3 < g2 and g3 < g4:
        return avg_grade(g1, g2, g4)
    else:
        return avg_grade(g1, g2, g3)


print(avg_top_3(40, 20, 30, 40))
